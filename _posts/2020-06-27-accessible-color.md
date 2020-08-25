---
layout: post
title: Accessible Color
subtitle: How to make web content viewable for everyone
tags: [accessibility]
---



Accessibility uplifts and empowers. When you're creating content for the web, you want to make sure that your website is accessible for everyone. Too often, I find websites that may be readable by screen reader, but are virtually impossible to read by someone with low vision. This not only limits who you can reach with your website, but it also makes it difficult to read for users who don't have vision issues. 

I won't list websites that are aggressively bad with accessibility and color because they don't deserve your clicks. I will, however, list two common examples I see on the web:

- Light grey text on a white background
- Red text on a black background 

Beyond these obvious and easy to catch examples, it does get a little harder for a developer to know what level of contrast constitutes as accessible. Thankfully there are a set of applicable standards published by W2C entitled *Web Content Accessibility Guidelines* (WCAG). As of writing, the most up to date version of WCAG is [WCAG 2.1](https://www.w3.org/WAI/standards-guidelines/wcag/glance/). In this standard, there are some helpful guidelines. For example: 



> Success Criterion 1.4.6 Contrast (Enhanced)
>
> (Level AAA)
>
> The visual presentation of [text](https://www.w3.org/TR/WCAG21/#dfn-text) and [images of text](https://www.w3.org/TR/WCAG21/#dfn-images-of-text) has a [contrast ratio](https://www.w3.org/TR/WCAG21/#dfn-contrast-ratio) of at least 7:1, except for the following:
>
> - Large Text
>
>   [Large-scale](https://www.w3.org/TR/WCAG21/#dfn-large-scale) text and images of large-scale text have a contrast ratio of at least 4.5:1;
>
> - Incidental
>
>   Text or images of text that are part of an inactive [user interface component](https://www.w3.org/TR/WCAG21/#dfn-user-interface-components), that are [pure decoration](https://www.w3.org/TR/WCAG21/#dfn-pure-decoration), that are not visible to anyone, or that are part of a picture that contains significant other visual content, have no contrast requirement.



With this in mind, you can use the 7:1 ratio as a threshold to see if your website meets the contrast standards. Moreover, there are free tools online that can a developer out. Websites such as [colorsafe.co](http://colorsafe.co/ ) will generate a set of WCAG contrast appropriate colors given a canvas color, font type, font size, and font weight. If you have a preexisting set of colors, websites such as [contrastchecker](https://contrastchecker.com/) will calculate the ratio for you and let you know if you meet the minimum threshold for the the AA or AAA WCAG contrast standards.