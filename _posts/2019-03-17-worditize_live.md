---
layout: post
title: "Worditize is Live!"
date: 2019-03-17 19:32
description: "A small writeup about my new NLP R Shiny project."
tags:
  - r
  - shiny
  - text mining
  - data mining
categories:
  - Projects
---

I'm happy to announce today that I have finally returned to my Shiny app
[worditize](https://github.com/progdrum/worditize). I have added some detailed
documentation and I have also released a version to shinyapps.io, which
can be found [here](https://progdrum.shinyapps.io/worditize/).

Detailed documentation is available in the README on the GitHub page, but please
allow me to offer a brief explanation here.

I learned about the [tidytext](https://www.tidytextmining.com/) package
at a talk given by one of the package's authors, [David Robinson](http://varianceexplained.org/),
relatively recently before I had conceived the idea for the original version of
this project. In short, it applies [tidy data](https://en.wikipedia.org/wiki/Tidy_data)
principles to text analysis. It also includes a number of tools and additional
data, such as sentiment corpora, to aid in text analysis.

Originally, I had conceived of the project as something where someone could
upload their own documents and get a rundown of some key stats and a
basic analysis. From there, I thought I'd add interactive facilities for users
to probe the data within the application. All in all, what I really
wanted to do was to get more familiar with text mining, with `tidytext` in
particular, and to dive into Shiny, all at the same time.

Being particularly interested in the text mining, and figuring that this would
be the more difficult and/or complicated part of the project, I decided to dive
into the analysis part first. At the very least, I wanted to get some small
part of that working, so that I could then work with the rest of the app. To
this end, I decided I would just pull some text from [Project Gutenberg] (https://www.gutenberg.org/)
--- which I learned about from the same presentation --- using the [gutenbergr](https://github.com/ropensci/gutenbergr)
package to test with. This would provide me with an easily accessed, large
corpus of data for testing the analysis code.

As I went along, I decided that I was actually more interested in the Project
Gutenberg test text instead. So instead of building file input widgets and
whatnot in the Shiny interface, I went ahead and made selectors for public
domain documents from Project Gutenberg. As they say, the rest is history.

This turned out to be especially useful for the part of the application that
does topic modeling. I was able to quickly and easily retrieve two different
texts to mine topics from and compare. If you decide to play with the app,
you'll likely understand what I mean. So, without further ado, I recommend
checking out the [app](https://progdrum.shinyapps.io/worditize/).
