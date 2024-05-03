---
layout: post
title: The Joy Of Building Small Tools
---

Creating small tools that perform simple tasks to enhance the lives of others can be surprisingly rewarding. 

Let me tell you a short enocunter that led to the creation of my [`dta` to `csv` repository](https://github.com/JakeC007/dta-to-csv-converter).

[...]

Recently, a colleague of mine found herself staring at a `.dta` file, tasked with examining it for a law journal article she was working on. Unfortunately, she had no clue how to crack open this mysterious file format. I happened to stop by and offered to help. Admittedly, I was equally clueless about `.dta` files, but a quick search on DuckDuckGo informed me that it's the data storage format used by Stata.

Now, I'm a R aficionado and have never worked with Stata. However, a faint memory surfaced from the depths of my mind -- I recalled working with Stata data files through the `Haven` package in R a few years back.

So, I whipped up a quick R script to assist my colleague in manipulating the data. As it turned out, she only needed to read data. However, in my enthusiasm, I went back to tinker with the R markdown file. Not only did it convert `.dta` files to `.csv`, but now it automatically converted every `.dta` file in the script's directory by just running the script. This way, all anyone has to do is add the files requiring conversion into the folder and run the script. 



The creation process didn't consume much time, but it undeniably made a  significant difference for her. That's the beauty of small tools -- they  may be simple, but their impact can be profound.







If you found this page by internet search somehow and need your `.dta` files converted you can find the repository [here](https://github.com/JakeC007/dta-to-csv-converter).