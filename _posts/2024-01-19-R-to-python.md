---
layout: post
title: A Brief Primer on Python For R Users
subtitle: What You Need To Know Transitioning From R
tags: [R, Python, how-to]
---

## Introduction

This post is the mirror image of an [R primer I wrote](https://jakec007.github.io/2020-12-29-R-coding-intro) for people coming from other languages. If you already know R and find yourself needing Python, this is for you. The usual reasons: you want `seaborn` for plotting, or you've hit a wall where the machine learning ecosystem (`scikit-learn`, `PyTorch`, `TensorFlow`) lives in Python and not R.

A warning up front. R has essentially one dialect for data work: base R plus the tidyverse. Python does not. The Python you'll write for ML and plotting lives in NumPy and pandas, and those libraries behave differently from base Python in ways that matter. This post teaches base Python first, then flags where pandas and NumPy diverge, because that divergence is exactly what trips up R users.

## Comments, Variables, and Assignment

### Comments and Variables

Anything after a `#` is a comment, same as R. Variable naming rules are close to R's, with one difference worth knowing:

* Names are alphanumeric plus underscore
* Names cannot start with a number
* The dot (`.`) is **not** legal in names. In R, `fuzzy.cats` is a fine variable. In Python, the dot means attribute access, so `fuzzy.cats` reads as "the `cats` attribute of object `fuzzy`" and will error if `fuzzy` doesn't exist.

So the R habit of dot-separated names has to go. Use underscores everywhere:

```python
cats
cats2
furry_cats
fuzzy_cats     # not fuzzy.cats
sleepy_cats    # not .sleepy_cats
```

### Assignment

This is the first real adjustment. R's assignment is `<-` and points at its target. Python uses `=` and reads left to right:

```python
swarthmore = 1864
```

The arrow is gone. One consequence: in R, `<-` and `=` are different operators with different scoping behavior. In Python, `=` is the only assignment, and `==` is the equality test. Mixing them up is the most common early bug. `x = 5` sets x to 5; `x == 5` asks whether x equals 5.

There's no `ALT` + `-` shortcut to miss, because there's only one character to type.

## Data Types

The three types you need map cleanly onto R's, with different names.

### Text

* **str** is Python's string type, R's character. Single or double quotes both work, R only really uses double.

```python
my_str = "nature has forced my hand"
type(my_str)
```

> <class 'str'>

Note `type()` instead of R's `typeof()`, and note the output is an object class, not a quoted string. One real difference: Python strings are indexable and sliceable like sequences. `my_str[0]` gives `'n'`. In R, `"nature"[1]` gives you back the whole string, because R has no scalar type and treats that as a length-one vector. This catches R users constantly.

### Numbers

* **float** is R's double. Same double precision.
* **int** is R's integer.

The casting behavior is reversed from what you're used to. R fights you when you want an integer and casts almost everything to double. Python defaults a bare whole number to `int` and only promotes to `float` when a decimal or division forces it:

```python
x1 = 7
x2 = 7.0
type(x1)
type(x2)
```

> <class 'int'>
> <class 'float'>

The gotcha that bites R users: in Python 3, `/` always returns a float, even `4 / 2` gives `2.0`. If you want integer division use `//`. R has no such split.

## Data Objects

R organizes its containers around a homogeneous/heterogeneous and 1D/2D grid. Python's built-in containers don't line up on that grid, because base Python has no array type at all. Here's the honest mapping:

| R object | Closest base Python | Notes |
| -------- | ------------------- | ----- |
| list / vector | `list` | both heterogeneous |
| atomic vector | `numpy.ndarray` | not in base Python, needs NumPy |
| matrix | `numpy.ndarray` (2D) | needs NumPy |
| data frame | `pandas.DataFrame` | needs pandas |
| factor | `pandas.Categorical` | needs pandas |

The thing to absorb: **the workhorses you actually want are not built in.** R ships with vectors, matrices, data frames, and factors as primitives. Python ships with `list`, `dict`, `tuple`, `set`, and you import NumPy and pandas to get the rest. This is why a Python data session always starts with `import` lines.

### Lists

Python's `list` is the everyday container, and it behaves like R's `list` (the `c(...)` that mixes types), not like an atomic vector:

```python
L1 = [1, "1", 2, "2", 3, "3"]   # mixed types, fine
L2 = ["cow", "sheep", "horse"]
L3 = [11.0, 1.2, 77.039, 96.030]
```

Square brackets, not `c()`. Commas inside, same idea.

#### How Lists Differ From R

**Indexing starts at 0.** This is the single biggest day-one adjustment. To reach `1.2` in `L3` you write `L3[1]`, not `L3[2]`:

```python
L3 = [11.0, 1.2, 77.039, 96.030]
L3[0]
L3[1]
```

> 11.0
> 1.2

`L3[0]` is the first element, not garbage. There's no "1 returns the first" convention to unlearn; just shift everything down by one.

Two more list features R doesn't have:

Negative indices count from the end. `L3[-1]` is the last element, `L3[-2]` the second-to-last. In R, `L3[-1]` means "drop the first element," a completely different operation. This reversal of meaning is worth burning into memory.

Slicing uses `start:stop` inside brackets, and the stop is exclusive. `L3[0:2]` gives the first two elements, indices 0 and 1, not three. R's `L3[1:2]` is inclusive on both ends.

#### The arithmetic trap

Here's where base Python and R diverge hardest. In R, lists and vectors do element-wise math:

```python
A = [1, 2, 3]
B = [40, 50, 60]
A + B
```

> [1, 2, 3, 40, 50, 60]

`+` on Python lists **concatenates**, it does not add element-wise. `*` repeats: `A * 2` is `[1, 2, 3, 1, 2, 3]`. There is no element-wise arithmetic on base lists at all. If you want R's behavior in pure Python you'd write a comprehension, `[a + b for a, b in zip(A, B)]`, or, far more likely, you'd reach for NumPy. Which brings us to the note that R users actually need.

> **Where it differs: NumPy.** The reason you're probably here, ML and seaborn, means you'll spend your time in NumPy arrays, not lists. And NumPy arrays behave like R vectors:
>
> ```python
> import numpy as np
> A = np.array([1, 2, 3])
> B = np.array([40, 50, 60])
> A + B
> ```
>
> > array([41, 52, 63])
>
> Element-wise, just like R. So the R intuition is correct again, but only once you've explicitly converted to an array. The lesson for R users is precise: **base Python lists are not R vectors; NumPy arrays are.** When element-wise math silently concatenates, you forgot to make it an array.

#### Vector recycling vs broadcasting

R recycles a shorter vector to match a longer one. NumPy has a related but stricter mechanism called **broadcasting**. It will stretch a scalar or a length-1 dimension across a larger array, but it will **not** recycle a length-2 array to fit a length-4 one the way R does:

```python
L3 = np.array([11.0, 1.2, 77.039, 96.030])
L3 + 100        # scalar broadcasts, fine
L3 + np.array([-1, 3])   # length 2 into length 4: ERROR
```

R would happily recycle `[-1, 3]` into `[-1, 3, -1, 3]`. NumPy raises a shape mismatch. This is a place where the R reflex produces a bug, so unlearn the recycling habit. Broadcasting only fills dimensions of size 1.

### DataFrames

The pandas DataFrame is R's data frame, and most of your mental model carries over. A DataFrame is a table; columns are variables, rows are observations.

The common operations have direct analogs:

* `df.head()` is R's `head(df)`, first 5 rows by default, not 6
* `df.columns` is R's `names(df)`
* `df.describe()` is R's `summary(df)`, min/max/quartiles per column

Note the syntax flip. R wraps the data in a function, `head(df)`. Python calls a method on the object, `df.head()`. The data comes first and the operation hangs off it with a dot. You'll see this pattern everywhere in pandas.

#### Accessing Columns

R's `$` becomes bracket or dot access. To pull `mpg` out of a cars table:

```python
import seaborn as sns
mpg = sns.load_dataset("mpg")   # seaborn ships this dataset
mpg["mpg"]        # preferred
mpg.mpg           # works, but breaks on names with spaces or that clash with methods
```

The bracket form `df["col"]` always works. The dot form `df.col` is the closer visual analog to `$` but fails on column names with spaces or names that collide with DataFrame methods, so prefer brackets when it matters.

### Categoricals

R's factor is pandas' `Categorical`. Same purpose: a categorical variable stored as integers under a set of labeled levels, not as raw strings. The motivation is identical, plotting and modeling functions expect it and misbehave on plain strings.

```python
import pandas as pd
cat_var = pd.Categorical(["b", "a", "c", "a"])
```

By default pandas sorts levels alphabetically, same as R. Reordering levels (R's relevel) is done with `cat_var.reorder_categories(...)` or by passing `ordered=True` with an explicit order. As in R, the stored values are integer codes with a label lookup, which you can see via `cat_var.codes`.

## Basic Operations

### Arithmetic

The operators match R, with the integer-division wrinkle noted earlier:

* Addition `+`
* Subtraction `-`
* Multiplication `*`
* Division `/` (always float in Python 3)
* Integer division `//` (no R equivalent)
* Exponent `**` (R's `^` does **not** work in Python; `^` is bitwise XOR and will silently give wrong answers)

```python
x = 10
y = 2
x + y
x - y
x * y
x / y
x ** y
```

> 12
> 8
> 20
> 5.0
> 100

Watch `x / y` returning `5.0`, a float, where R gives `5`. And do not reach for `^` out of habit; `10 ^ 2` is `8` in Python, not `100`, because it's bitwise XOR.

### Order of Operations

Python follows PEMDAS like R:

```python
7 + 3 / 2 ** 0
```

> 10.0

### How Expressions Evaluate

Sequential, like R. The right side resolves before assignment, so `x = x * 2` computes the old `x` times 2 then rebinds:

```python
x = 7
x = x * 2     # 14
```

No surprise here for an R user. One thing to flag: Python has compound operators R lacks. `x *= 2` is shorthand for `x = x * 2`, and you'll see `+=`, `-=`, `/=` constantly in Python code.

### Moving Data: Chaining vs the Pipe

R's `%>%` (or newer `|>`) threads data through a sequence of functions. Pandas does the same thing with **method chaining**, dotting operations together left to right:

```python
# R:        my_data %>% scale() %>% head()
# pandas:
my_data.apply(zscore).head()
```

The reading direction is the same as the pipe, left to right, follow the dots. And the overwrite trick you use in R works identically:

```python
# R:      my_data <- my_data %>% select(-year)
# pandas:
my_data = my_data.drop(columns="year")
```

Same caution as in R: reassigning over your original DataFrame is powerful and easy to regret. Keep an unmodified copy around while you're learning.

One real difference. R's pipe passes the left side as the first argument to any function. Python method chaining only works for methods that exist on the object and return something chainable. You can't pipe a DataFrame into an arbitrary standalone function with a dot. When you need that, you either nest calls, `head(scale(df))` style, or use `.pipe()`: `df.pipe(my_func).head()`.

## Packages and Imports

R uses `library(pkg)` to load an installed package, dumping all its functions into your namespace. Python uses `import`, and crucially, it keeps the package namespaced:

```python
import numpy as np
import pandas as pd
import seaborn as sns
```

After `library(ggplot2)` in R you call `ggplot()` bare. After `import pandas as pd` you call `pd.DataFrame()`, with the prefix. That `pd.`, `np.`, `sns.` prefix is not optional clutter; it's how Python keeps two packages from clobbering each other's function names. The `as np` part is just a community-standard short alias.

Installation is also separate from import. R's `install.packages("x")` then `library(x)` becomes `pip install x` (run once, in the terminal) then `import x` (in your script). The install step is not Python code; it's a shell command.

## A Common Mistake: Quoting Column Names

The R primer's closing example was about when to quote things in `ggplot`. The Python version of that confusion shows up in seaborn, and it's almost the inverse.

```python
# common error
import seaborn as sns
mpg = sns.load_dataset("mpg")
sns.scatterplot(data=mpg, x=weight, y=mpg)   # broken
```

Here `weight` and `mpg` are bare names, so Python looks for variables called `weight` and `mpg` and either errors or, worse, finds the `mpg` DataFrame and uses the whole thing. Seaborn wants the column names as **strings**:

```python
# fixed
sns.scatterplot(data=mpg, x="weight", y="mpg")
```

This is the trap reversed from R. In `ggplot`'s `aes()` you write column names bare and quoting them is the error. In seaborn's function call you quote them and leaving them bare is the error. Same underlying question, "is this a name in the data or a literal value," opposite answer in each ecosystem. If you internalize one thing from this section: ggplot `aes` wants bare, seaborn wants quoted.

## Quick Reference

| You know (R) | You want (Python) |
| ------------ | ----------------- |
| `<-` | `=` |
| `==` for equality | `==` (same) |
| `c(1, 2, 3)` | `[1, 2, 3]` or `np.array([1, 2, 3])` |
| index from 1 | index from 0 |
| `x[-1]` drops first | `x[-1]` is last element |
| `typeof(x)` | `type(x)` |
| `head(df)` | `df.head()` |
| `names(df)` | `df.columns` |
| `summary(df)` | `df.describe()` |
| `df$col` | `df["col"]` |
| `factor(x)` | `pd.Categorical(x)` |
| `^` for power | `**` (`^` is XOR) |
| `%>%` | `.method()` chaining or `.pipe()` |
| `library(x)` | `import x` |
| element-wise on vectors | only on NumPy arrays, not lists |

## Works Referenced

McKinney, W. (2017). *Python for Data Analysis*. O'Reilly.

NumPy documentation: numpy.org/doc

pandas documentation: pandas.pydata.org/docs

seaborn documentation: seaborn.pydata.org

VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly.