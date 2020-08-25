---
layout: post
title: Insights in Recent Hugo Data
subtitle: How the Hugo award XXXX
gh-repo: JakeC007/hugo_stats
gh-badge: [star, fork, follow]
tags: [projects, repo]
---



For a class stats project I examined Hugo Award nominations over the past 11 years.

## Disclaimers
- The data entry was done by hand, as such it is possible that there is an error in the data set
- I pruned nominations with multiple authors from my data set because it would violate my assumption of one set of pronouns per nomination
- I want to make it very clear that **I am glad that the Hugo Awards have recently been more conscious about gender equity.** 

## About This Project 
- My data source was [the hugo awards website](http://www.thehugoawards.org/hugo-history/)
    - To ascertain an author's pronouns, I looked through an author's twitter, Wikipedia page, or website. 
    - **Nominations with multiple authors were excluded because it would violate my assumption of one set of pronouns per nomination.**
    - I only looked at the following categories because finding an author's pronouns is labor intensive so I had to limit the scope of the project 
        - Best Novel
        - Best Novella
        - Best Novelette
    - Each category yielded ~66 observational units.
- I used Python to do some minimal data processing and R for data viz

## Results 

![Stacked bar chart that shows how many times an author has been nominated.](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Nominations%20by%20author.png)

![Stacked bar chart that shows the pronoun breakdown of each year's Best Novel nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best%20Novel%20BarChart.png)

![Stacked bar chart that shows the pronoun breakdown of each year's Best Novella nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best%20Novella%20BarChart.png)



![Stacked bar chart that shows the pronoun breakdown of each year's Best Novelette nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best%20Novelette%20BarChart.png)

![]()

<img src="https://github.com/JakeC007/hugo_stats/blob/master/imgs/Nominations%20by%20author.png" alt="Italian Trulli">

test

### Some Overall Stats Relating To The Nominations Per Author Image
- Best Novel Nominations
    - There are 24 unique authors that use she/her pronouns
    - There are 23 unique authors that use he/him pronouns
    - There are 0 unique authors that use they/them pronouns
- Best Novella Nominations
    - There are 21 unique authors that use she/her pronouns
    - There are 23 unique authors that use he/him pronouns
    - There are 2 unique authors that use they/them pronouns
- Best Novelette Nominations
    - There are 28 unique authors that use she/her pronouns
    - There are 26 unique authors that use he/him pronouns
    - There is 1 unique author that use they/them pronouns
- The three authors with the most nominations are
    1. Seanan McGuire (7)
    2. Mira Grant (6)
    3. Aliette de Bodard (5)