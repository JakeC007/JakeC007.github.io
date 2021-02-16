---
layout: post
title: Helpful R Functions and What They Do
tags: [R, how-to, code, code-ref]
---

A collection of R functions that I found helpful. Some of these functions require the `tidyverse` package.

### Getting info on variables

* `str(my_varb)` - displays the content of an R object (*i.e.,* any variable)
* `class(my_varb)` - displays the class of an R object (*i.e.,* any variable)

### Getting info on data sets 

* `head(my_data)` - displays the first six lines of a data set
* `names(my_data)` - displays the names of the variables within a data set
* `summarize(mydata)`- summarizes data into single row of values
* `count()`  - lets you count the unique values of one or more variables within each group of a categorical variable 
  * ex. `my_data %>% count(large_cats)`

### Manipulating data sets

* `filter(my_data, condition)` - keeps the data that matches the condition

  * ex. Assuming you have a data set `my_data` that has a variable named `num_cats` you could filter out all rows that saw no cats with the following code `filter(my_data, num_cats>0)` 

* `select(my_data, vars)` - can return a specified subset of the data or remove a set of variables from the data 

  * ex. `select(my_data, A, B, C)` - selects the variables `A`, `B`, `C` from `my_data` data set
  * ex. `select(my_data, -B)` - remove's variable `C` from `my_data` data set

* `mutate()` - appends a new column of data to the original data set

  * ex. Assuming you have a data set `my_data` that had a variable named `num_cats` you could add a variable named `cats_per_hour` with the following code: `my_data %>% mutate(cats_per_hour = (num_cats/60))`

* `mutate_if(if_statement, mutation)` - affects only the columns that satisfy the if statement

* `mutate_at(c(col1, col2, col3), mutation)` - edits the specific columns with the mutation 

* `group_by(my_data, var)` - groups the data according to different "levels" of a categorical variable of your choice.

* `relevel(fct_vect, new-reference-level)` - the levels of a factor are re-ordered so that the level specified by `new-reference-level`is first and the others are moved down

* `fct_infreq(cat_varb)` - factor order so that the category with the most observational units is the reference variable 

* `fct_rev(cat_varb)` - reverses the order of the factor levels

* `fct_recode(cat_varb)` - manually choose what you want the reference level to be

  * ex. from R documentation: 

  * ```R
    x <- factor(c("apple", "bear", "banana", "dear"))
    fct_recode(x, fruit = "apple", fruit = "banana")
    ```

* `factor(cat_varb)` - factor levels are arranged in alphabetical order

### Standardizing Data

Uses the `mutate_at` and `scale` function to standardize the data

```R
my_data_standard <- my_data %>% 
                     mutate_at(vars("var1", "var2", "var3", "var4"), funs(scale))  
```

### Miscellaneous

* `cor(data_object$xvariable, data_object$yvariable)` -  calculates the correlation (strength of the linear relationship) between two quantitative  variables

  * Recall correlation is the standardized (is on the domain of [-1,1]) version of the covariance

* `dim(my_data)` - spits out the dimensionality --- i.e. how big -- a table or dataset is 

  