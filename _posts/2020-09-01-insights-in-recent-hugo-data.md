---
layout: post
title: Insights in Recent Hugo Data
subtitle: How even the most favorable Hugo nominations data (2009-2020) shows discrimination against authors that don't use he/him pronouns
gh-repo: JakeC007/hugo_stats
gh-badge: [star, fork, follow]
tags: [projects, repo]
---



***This is a Draft. See its unedited, ungrammatical, glory 

For a class statistics project, I choose to work with data from the Hugo Awards. Looking at the nominations data, I was curious to know the gender breakdown over the past ten or so years. This proved to be impossible because **you cannot infer someone's gender**; so, I did the next best thing and analyzed the breakdown of a nominated author's pronouns. I ended up with eleven years of data because the 2020 nominations were released during my collection of the 2009-2019 data. I figured more data is better and added the 2020 nominations to my data set. I didn't use the pronoun data I collected to extrapolate anything about gender because, again, **you cannot infer someone's gender.**

What I found probably won't surprise you, but I thought it was interesting so I figured I'd share. Skip to the [results](#results) section if you want to get to the answers right away. 



## Methodology

Right, so how did I go about doing this? Well...

- My data source was [the Hugo Awards website](http://www.thehugoawards.org/hugo-history/)
  - I pulled every nominated author from each relevant category into a spreadsheet 
  - To ascertain an author's pronouns, I looked through an author's twitter, Wikipedia page, or website
  - Nominations with multiple authors were excluded because it would violate my assumption of one set of pronouns per nomination. **As such, my data is missing a few data points**
  - I only looked at the following categories because finding an author's pronouns is labor intensive so I had to limit the scope of the project 
    - Best Novel
    - Best Novella
    - Best Novelette
  - Each category yielded ~66 observational units.
- I used Python to do some minimal data processing and R for data visualization
- The GitHub repo with my dataset, code, and images is linked at the top of the post. It can also be found [here](https://github.com/JakeC007/hugo_stats)!



### Disclaimers
- The data entry was done by hand; as such, it is possible that there is an error in the data set
- I pruned nominations with multiple authors from my data set because it would violate my assumption of one set of pronouns per nomination
- I want to make it very clear that **I am glad that the Hugo Awards have recently been more conscious about gender equity**
- **The data that I collected is wildly skewed.** The number of people nominated that use *she/her* pronouns shown in this sample is by no means representative of the 60+ year Hugo dataset as a whole 



## Results 

| ![Stacked bar chart that shows the pronoun breakdown of each year's Best Novel nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best_Novel_BarChart.png?raw=true) | ![Stacked bar chart that shows the pronoun breakdown of each year's Best Novella nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best_Novella_BarChart.png?raw=true)|
|---|---|
| ![Stacked bar chart that shows the pronoun breakdown of each year's Best Novelette nominations](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Best_Novelette_BarChart.png?raw=true)  | ![Stacked bar chart that shows how many times an author has been nominated.](https://github.com/JakeC007/hugo_stats/blob/master/imgs/Nominations_by_author.png?raw=true)|



### Some Stats

- Best Novel Nominations
    - There are 24 unique authors that use *she/her* pronouns
    - There are 23 unique authors that use *he/him* pronouns
    - There are 0 unique authors that use *they/them* pronouns
- Best Novella Nominations
    - There are 21 unique authors that use *she/her* pronouns
    - There are 23 unique authors that use *he/him* pronouns
    - There are 2 unique authors that use *they/them* pronouns
- Best Novelette Nominations
    - There are 28 unique authors that use *she/her* pronouns
    - There are 26 unique authors that use *he/him* pronouns
    - There is 1 unique author that use *they/them* pronouns
- The three authors with the most nominations are
    1. Seanan McGuire (7)
    2. Mira Grant (6)
    3. Aliette de Bodard (5)



### Analysis 

* On the surface, there looks to be a large improvement in representation for authors that use *she/her* pronouns 
  * Both Best Novel and Best Novelette have a strong positive correlation for authors who use *she/her* pronouns
    * Best Novel takes this correlation to its natural conclusion in 2020 where all of the authors use *she/her* pronouns 
  * Best Novella has a weak positive correlation for authors who use *she/her* pronouns
  * In both the Best Novella and Best Novelette categories, there is a strange blip in the 2015 data. This is a result of a malicious scheme by a group of [internet misogynists](https://en.wikipedia.org/wiki/Sad_Puppies) to stuff the ballot box because they felt that too many people that didn't have *he/him* pronouns were getting nominations. 

* The breakdown of nominations per author is very informative. Authors who use *she/her* pronouns had multiple nominations at a rate that far outstripped authors of *he/him* and *they/them* pronouns
  * This tells us that they keep drawing from the same pool of authors that use she/her pronouns 
  * **In other words, authors that use *she/her* pronouns need to be exceptional to receive a nomination, while those with *he/him* pronouns don't need to raise to the same standard** 
  * I don't have the exact number anymore, but just 18 authors that use *she/her* pronouns are responsible for ~66 nominated works. That's about a third of the nominations over the last 11 years coming from just 18 people! So while overall representation has improved for authors who use *she/her* pronouns, the spread of authors is dismally low.
- Representation for people who don't use *she/her* or *he/him* pronouns is abysmal at just 3 out of 118 nominated authors over the past 11 years