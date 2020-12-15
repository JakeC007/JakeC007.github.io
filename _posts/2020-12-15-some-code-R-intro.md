---
layout: post
title: A Brief Primer on R For Intro Stats
subtitle: What You Need To Know Transitioning From Other Coding Languages
tags: [R, how-to]
---

## Introduction

This post is a light adaptation of a document that I wrote for my statistical methods II course. Before entering the course sequence I had coding experience but knew nothing about R. I wrote this quick introduction so that people who have some background in CS can get up to speed on how to use R quickly.  

If you have no CS background -- which is totally okay!-- I have also written a ["no code" introduction to R](https://jakec007.github.io/2020-12-15-no-code-R-intro). 



## Comments, Variables, and the Assignment Operator

### Comments and Variables

Anything in R with a `#` in front of it is a comment. Variables in R work similarly to most other OOP languages. Namely:

* Variable names must be a contiguous set of alphanumeric characters 
* Variable names should not have special characters in them with the exception of dot (`.`) and underscore (`_`)
* Variable names can start with an alphabet character or a dot (`.`)
  * If the variable name starts with a dot , then the next symbol should not be a number

The following are some acceptable variable names:

```R
cats
cats2
furry_cats
fuzzy.cats
.sleepy_cats
```

### The Assignment Operator 

The assignment operator `<-` stores the data to the right of the arrow into the variable sitting on the left. For example: 

```R
Swarthmore <- 1864
```

As you can see, you only have to follow the direction of the arrow to see what is getting stored where. 



## Data Types

There are 3 data types that you will need to know about for this class:

### Data types that deal with words and letters

* *Character* (abbreviated as chr) - are R's version of strings. Unlike C, multiple characters together aren't treated as chr arrays. Everything within quotes (`"`) is treated as type chr. 
  * Examples: `"wug"`, `"problem7" `, `"Stat_21"`  

```R
my_str <- "nature has forced my hand" # a quote from Ralph Thayer, former Director of Maintenance at Swarthmore
typeof(my_str)
```

> [1] "character"



### Data types that deal with numbers

* *Double* (abbreviated as dbl) - in R these are floats with double precision. Anecdotally, R casts almost all numeric data as a dbl by default.
  * Examples: `1.6783`, `1`, `-32`,`-15.0000034`
* *Integer* (abbreviated as int) - same as any other language. Anecdotally, R seems resistant to casting whole numbers as integers. If for some reason it is really important to have an int, you may use the `as.integer()` function. See below

```R
x1 <- 7
x2 <- as.integer(7)
typeof(x1)
typeof(x2)
```

> [1] "double"
> [1] "integer"



## Data Objects

There are five main data structures in R:

- *Atomic vector* - an array of data where everything inside the array is of the same data type
  - when we say *atomic* we mean that everything in the vector must be of the same data type (e.g. all chrs or all dbls) 
- *List*/*vector* - a more robust array that can have elements of mixed data types 
- *Matrix* - this is simply an atomic vector with multiple dimensions; all elements in the matrix must be of the same type
- *Data frame* - this is a special type of vector that has multiple dimensions 
- *Factor* - This is different than the previous four and we will expand on it later.

We will focus on the three data types that you will most commonly encounter: lists, data frames, and factors.

### Lists 

Lists, also known as vectors, are simple 1D arrays that can have multiple types of data within them. This doesn't mean that they will always contain a mix of different data types. Rather, R will accept a list that contains `7` and `"seven"`.   

The following lines of code make legal lists:

```R
L1 <- c(1,"1",2,"2",3,"3") # a mixed-type list
L2 <- c("cow", "sheep", "horse") # a list of just chrs
L3 <- c(11.0, 1.2, 77.039, 96.030) # a list of just dbls
```

#### How Lists are Different in R as Compared to Other Languages You Have Used

<u>**Indexing starts at 1 in R.**</u> Thus if you wanted to index to `1.2` in `L3` you would write `L3[2]` **not** `L3[1]`

```R
L3 <- c(11.0, 1.2, 77.039, 96.030)
L3[0]
L3[1]
```

> numeric(0)
> [1] 11

Note how `L3[0]` produces garbage while `L3[1]` produces the first element in the list. 

### Data Frames

The data frame is what you will be dealing the most with in R. It is the object that will store any data that you read into R. Think of a data frame as a table (or list of lists if you just came from cs21). Each column in the table is a different variable and each row in the table is an observational unit. 

There are a couple important functions that can be used on data frames:

* `head(my_data)` - shows the first 6 rows of the data frame
* `names(my_data)` - displays the names of the variables within the data frame
* `summary(my_data)`- displays a summary of the data -- min, max, median, etc. --  for each variable contained within the data set. 

#### Accessing Variables Within a Data Frame

The dollar sign (`$`) allows you to extract variables from within a data set. Let's do a short example with the `mtcars` data set which is built into R. 

`mtcars` is stored in a data frame. `mtcars` has a variable named `mpg ` (something we can find out by using the `names()` function). The following code extracts the variable `mpg` from the data frame `mtcars`.

```R 
mtcars$mpg
```

> [1] 21.0 21.0 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 17.8 16.4 17.3 15.2 10.4 10.4 14.7 32.4 30.4 33.9 21.5 15.5 15.2

I modified the output to keep it short, but as you can see the code above returns the contents of the variable `mpg`. 

 ### Quick Summary Of The Section So Far

| Dimensions | **Homogenous** | **Heterogeneous** |
| ---------- | -------------- | ----------------- |
| 1D         | atomic vector  | list              |
| 2D+        | matrix         | data frame        |

### Factors

Factor (abbreviated as fctr) is used to represent categorical variables in R. Once created, factors can only contain a preset collection of values known as levels. These levels are discretized from the data you inputted when creating the factor. 

Oftentimes your categorical variables will already be imported into the data frame and will be stored as a list. You must use the `factor(cat_varb)` function to turn your categorical variable into a factor. By default, R will store your factor's levels in alphabetical order. Later on in the course you will learn how to relevel a factor to change the ordering of the levels.

##### Advanced note on factors

On the surface factors may seem to be a special type of list, or an atomic chr vector, they are neither. Factors are stored as integers with labels associated with each level. When working with categorical data R excepts a factor data object and will do unexpected things if it doesn't receive one. This is why you need to ensure that your categorical variables are stored in a factor object. 



## Basic Operations

### Performing Arithmetic Operations On Data

Basic arithmetic operators are the same as in other languages.

* Addition: `+`
* Subtraction: `-`
* Multiplication: `*`
* Division: `/`
* Exponentiate: `^`  or `**`  

We see these basic operations on the following lines: 

```R
#Set up our x and y variables
x <- 10
y <- 2
#Do some basic math
x+y
x-y
x*y
x/y
x**y
x^y
```

> [1] 12
> [1] 8
> [1] 20
> [1] 5
> [1] 100
> [1] 100

#### A small note on lists 

The operations listed above (`+`,`-`,`*`,`/`,`^`) are *element-wise* operators. This means that when you perform these functions on lists, R goes element by element performing the given operation on each corresponding set of elements in each of the lists. Lets look an example, say we have two lists with three elements each. List A contains the numbers $$1,2,3$$ and list B contains the numbers $$40,50,60$$. We would expect $$[1,2,3]+[40,50,60] \rightarrow [1+40, 2+50, 3+60] \rightarrow [41, 52, 63]$$. Lets see that in R.

```R
# set up our lists 
A <- c(1,2,3)
B <- c(40,50,60)
#perform addition 
A+B
```

> [1] 41 52 63

Exactly as we expected! We can do the same for `-`,`*`, `/` and `^`.

```R
# set up our lists 
A <- c(1,2,3)
B <- c(40,50,60)
#perform arithmetic operations    
A-B
A*B
A/B
B^A
```

>[Line 5] -39 -48 -57
>[Line 6]  40 100 180
>[Line 7] 0.025 0.040 0.050
>[Line 8]     40   2500 216000

I have slightly modified the R output so that it is easier to see see which line of code produced which output.

#### The VERY IMPORTANT implications of "a small note on lists"

As discussed in the [previous section](#A-small-note-on-lists ) basic operators perform element-wise operations. This means that **you should not use a for loop**  when combining two lists together. R is a vectorized language; this is just a fancy way of saying that R naturally stores data in columns[^1] and R's complier is designed to optimize operations that manipulate vectors, not elements within vectors. Thus, if you aren't coding to take advantage of this, you're fighting the R every step of the way. 

#### Vector Recycling 

In the examples above, lists `A` and `B` are of the same length. R allows you to perform vector operations on two or more vectors of unequal length. Rather than truncate the longest vector, R recycles elements of the shorter vector(s) to match the length of the longest vector. Let's look at an example using `L3` from before and a new vector called `L4` which is shorter than `L3`:

```R
L3 <- c(11.0, 1.2, 77.039, 96.030)
L4 <- c(-1, 3)
L3+L4
```

> [1] 10.000  4.200 76.039 99.030



[^1]: To quote Tim Smith, "All naked numbers [in R] are double-width floating-point atomic vectors of length one." 

### Order of Operations

R follows the standard PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction) order of operations when evaluating an expression. 

```R
7+3/2^0
```

> [1] 10

### Evaluating Expressions

R evaluates lines of code sequentially. In the following code below `x1` is 12 in line 3.

```R 
x1 <- 3
x1 <- 0
x1 <- 12
```

R also evaluates the right side of the assignment operator (`<-`) before storing it in the left side. `x2` on line 2 is 14

```R
x2 <- 7
x2 <- x2*2 # here we do 7*2 = 14 and then store it in x2
```

This has important implications that we will see in the next section . 

### Moving Data

#### The Pipe

The pipe (`%>%`) allows you to move your data through a litany of operations. The following two lines of code are equivalent:

```R
head(scale(my_data))
my_data %>% scale() %>% head()
```

Especially as you start doing more complex operations in R, using the pipe to move your data from one function to the next makes reading your code -- and understanding what is going on -- much easier. 

Please note that "pipes (`%>%`), unlike assignment operators (`<-`), are read from left to right. It's easy enough to keep track of this, just follow the direction of the carrots!" See the example below:

```R
my_scaled_data <- my_data %>% scale()
```

In this example we scaled `my_data` and then saved it in `my_scaled_data`. However, recalling what we learned in the previous section [Evaluating Expressions](#Evaluating-Expressions), we can leverage pipes and the way R evaluates lines of code to modify existing data frames. 

Say you wanted to remove `year` from your data frame but didn't want to create a new data frame[^2]. You could simply do the following:

```R
my_data <- my_data %>% select(-year)
```

Instead of saving the modified `my_data` in a new variable we overwrote the preexisting data frame. Obviously, this is a powerful but dangerous technique and should be used in very limited circumstances in this class.  

[^2]: It is strongly recommended that you create a new data frame every time you modify it.

## Packages & Libraries

Like Python, C++, and Java, R has packages that you can download and install. To include a package in your working enviroment simply use the function `library(package)`. 

In this class we will be using several packages. Most commonly we will be using the packages  `tidyverse` and `ggplot2`. As such, near the top of every R or R markdown file you wrote make sure the following lines of code appear.

```R
library("tidyverse")
library("ggplot2")
```



## Common Mistakes With Data Types

Consider the code below to plot a graph. (Don't worry if the code doesn't mean anything to you. Your professor will go over how to plot graphs in class)

```R
# broken code
mtcars #built in data set with the following varbs: mpg, cyl disp, hp, drat, wt, qsec, vs, am, gear, carb
ggplot(mtcars, aes(x="wt", y=mpg)) + 
  geom_point(shape=18, color=blue)+
  geom_smooth(method=lm, se=FALSE, linetype="dashed")
```

On line 3 `"wt"` shouldn't be a chr because its a variable in `mtcars`, not a chr. On line 3 `blue` should be a chr because its a chr parameter passed into the `geom_point` function not a variable you created. 

```R
# fixed code
mtcars #built in data set with the following varbs: mpg, cyl disp, hp, drat, wt, qsec, vs, am, gear, carb
ggplot(mtcars, aes(x=wt, y=mpg)) + 
  geom_point(shape=18, color="blue")+
  geom_smooth(method=lm, se=FALSE, linetype="dashed")
```



## Works Referenced

Adler, J. (2012). *R in a Nutshell*. O'Reilly.

John Blischak, Daniel Chen, Harriet Dashnow, and Denis Haine (eds): "Software Carpentry: Programming with R".  Version 2016.06.

R Documentation and manuals: www.rdocumentation.org

Smith and Ushey. (2012). *aRrgh: a newcomer’s (angry) guide to R*. 

Thornton, S. (2020). *Class 5 Part 2* [Stat 021 F'2020 Class Slides]. Retrieved from [Professor Thornton's Website](http://www.swarthmore.edu/NatSci/sthornt1/Stat021/Class5_files/class5-part2.html)

