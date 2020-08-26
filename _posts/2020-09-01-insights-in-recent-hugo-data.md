---
layout: post
title: Insights in Recent Hugo Data
subtitle: How even the most favorable Hugo nominations data (2009-2020) shows discrimination against women
gh-repo: JakeC007/hugo_stats
gh-badge: [star, fork, follow]
tags: [projects, repo]
---



For a class stats project I examined Hugo Award nominations over the past 11 years. What I found probably won't surprise you but I thought it was interesting so I figured I'd share. Skip to the [results](#results) section if you want to get to the answers right away. 

I was curious to know what the gender break down was of Hugo award nominations over the past ten or so years. **You cannot infer someone's gender** so I did the next best thing and analyzed the pronouns breakdown of the authors who were nominated for a Hugo award over the past ten years or so. I didn't use the pronoun data to extrapolate anything about gender because, again, **you cannot infer someone's gender.**



## Methodology

Right, so how did I go about doing this? Well....

- My data source was [the hugo awards website](http://www.thehugoawards.org/hugo-history/)
  - I pulled every nominated author from each relevant category into a spreadsheet 
  - To ascertain an author's pronouns, I looked through an author's twitter, Wikipedia page, or website. 
  - Nominations with multiple authors were excluded because it would violate my assumption of one set of pronouns per nomination. **As such, my data is missing a few data points**
  - I only looked at the following categories because finding an author's pronouns is labor intensive so I had to limit the scope of the project 
    - Best Novel
    - Best Novella
    - Best Novelette
  - Each category yielded ~66 observational units.
- I used Python to do some minimal data processing and R for data viz



### Disclaimers
- The data entry was done by hand, as such it is possible that there is an error in the data set
- I pruned nominations with multiple authors from my data set because it would violate my assumption of one set of pronouns per nomination
- I want to make it very clear that **I am glad that the Hugo Awards have recently been more conscious about gender equity.** 
- **The data that I collected at is wildly skewed.** The number of people nominated that use *she/her* pronouns shown in this sample is by no means representative of the 50+ year Hugo dataset as a whole. 

## Results 

| ![Stacked bar chart that shows the pronoun breakdown of each year's Best Novel nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best_Novel_BarChart.png?raw=true)  | 
![Stacked bar chart that shows the pronoun breakdown of each year's Best Novella nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best_Novella_BarChart.png?raw=true)
  |
|---|---|
| ![Stacked bar chart that shows the pronoun breakdown of each year's Best Novelette nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best_Novelette_BarChart.png?raw=true)  | ![Stacked bar chart that shows how many times an author has been nominated.](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Nominations_by_author.png?raw=true)  |







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