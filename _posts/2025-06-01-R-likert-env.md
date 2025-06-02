---
layout: post
title: An Update To Likert Scales In R
gh-repo: JakeC007/likert-R-examples
gh-badge: [star, fork, follow]
tags: [R, how-to, R-tips, code]
---

In the summer of 2021, I wrote a blog post on how to make Likert-scale charts in R because  I just wanted future-me to have a clear reference instead of spending another afternoon endlessly poking around stackoverflow for how to center diverging bars.

That post ended up getting a lot more attention than I expected. It was surprising and  humbling. I wrote it for myself so I wouldn’t forget how it worked.

Now it’s 2025 -- almost four years to the day since I wrote that post -- and the original code doesn’t work anymore. The `likert` and `HH` packages have changed, and I’ve heard from plenty of people that the examples are broken. Thank you for telling me. Sorry for the hassle.

### I’m Not Rewriting The Guide

I've got studies to run, papers to write, and students to teach. I don’t have time to write a new version of the likert guide. These days I would probably just make the chart in Python using `matplotlib` or [`plot-likert`](https://github.com/nmalkin/plot-likert/blob/master/docs/guide.ipynb), which I know is not helpful to anyone working in R.

But I can give you something that might still help.


### Here’s The Exact Environment I Used Back In 2021

The code still runs fine on my machine. That’s because I haven’t updated any of those packages. They’re frozen in time. What I should have done back then is save the package environment properly, like Python users do with `venv`.

Turns out R has something similar. It’s called [`renv`](https://rstudio.github.io/renv/).

### What `renv` Does

`renv` lets you snapshot your project’s package versions and store them in a lockfile. Anyone can use that lockfile to recreate the same environment.[^1] You just run `renv::restore()` and you get the exact versions I had when I wrote the code.

I’ve now added `renv` to the project. If you clone the repo and open it in RStudio, you can restore the original setup by running this in the R console:

```r
install.packages("renv")
renv::restore()
```

This will install the right versions of `likert`, `HH`, and anything else that was needed. The [README](https://github.com/JakeC007/likert-R-examples/blob/main/README.md) has more details if you get stuck.



### Or Just Grab The Versions Manually

If you prefer not to use `renv`, I’ve also exported a list of the package versions I used. It’s basically like a Python `requirements.txt` file. You can install the packages manually using those exact versions. Again, see the [README](https://github.com/JakeC007/likert-R-examples/blob/main/README.md).



### A Quick Reflection

This was a good reminder that package environments matter. If you’re sharing code that other people might use, even casually, it’s worth capturing the package versions too. 

Packages deprecate functions or overhaul APIs. Dependency trees change and pull in new versions of libraries you never directly touched. Even minor updates to R itself or system-level libraries (like `libxml2`, `cairo`, or whatever your plotting package happens to lean on) can cause installs to fail or behavior to change.

The result is that code you wrote in good faith, that definitely worked on your machine, slowly stops working anywhere else. Including your future machine. 

That’s why freezing environments matters. It’s not just about pinning versions of the big packages you use. It’s about capturing the whole dependency stack -- including the obscure helper packages that make everything go -- and being able to recreate it with minimal guesswork.

If you're sharing code, even just for yourself, it’s worth freezing the environment. That way you’re not relying on luck and goodwill from CRAN to keep everything stable. 





[^1]: Ostensibly. There is great work by Dr. Margo Seltzer and her team on the limitations of code reproducibility.