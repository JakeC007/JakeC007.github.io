---
layout: post
title: Make `diff` More Effective With Kompare
tags: [linux, ubuntu, linux tips, tech tips, linux tools]
---

# Make `diff` More Effective With Kompare

The diff tool is a powerful utility when trying to compare two files. In my own uses of the diff tool I have sometimes wished for something a bity more human friendly. Luckily that's where Kompare comes in. It's a GUI that compares two files--same as diff!

In using Kompare I've found that the compare button is sometimes greyed out. 

![](/assets/img/kompare_grey.png)

Luckily I've found an easy fix to this problem. 

### Graphical Way

To make the compare button work you need to use the GUI file explorer to drag the files into the "source" and "destination" instead of using the "select file" or "select folder" button.

### Text-based way

Note in the picture below there is now a "file:/" before the file path. All you need to do is add `file:/` before you type out the path to your file. *Note:* ensure that you file path starts with a front slash so that there are two slashes before the first folder. E.g.: `file://mystuff/myfile.txt` 



![](/assets/img/kompare_full.png)