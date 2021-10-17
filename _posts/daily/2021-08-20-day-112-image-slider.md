---
layout: post-daily
title: "Day 112: Image Slider \U0001F4BB"
author: Ash
categories: daily
tags: [default, hobby]
worktime: 27
date: 2021-08-20 23:41 +0200
---
I think I figured out what sideproject I want to do (see [Day 108]({% post_url daily/2021-08-17-day-108-holiday-slump %})): making and hosting my own website. I will post more updates on that on Sunday.

However, for now I wanted to implement another functionality here on my daily journal that I will later need for my website anyway. I needed an image slider/slideshow. In theory, it doesn't sound that hard to implement. After all, you just need to bunch some images together and put some arrows on it to switch between them, right? Well, it's a little more complicated than that.

I took the code from a [slideshow tutorial](https://www.w3schools.com/howto/howto_js_slideshow.asp), which allows for one fixed slideshow on any given webpage, and modified it in order to be able to put multiple slideshows onto one page. Then I wanted to test it and realized it doesn't work &mdash; there weren't any images being shown. After 3 hours of implementing, testing, figuring out what the heck I'm even doing, realizing I don't know how HTML, CSS or Javascript work, I finally made the slideshow work.

What better way to show off my slideshow implementation than to show some pictures of the city hall in Munich that I took over time:

{% include image-slider.html name="marienplatz" parent="/assets/res/" images="day-112-marienplatz-1.jpg; day-112-marienplatz-2.jpg; day-112-marienplatz-3.jpg; day-112-marienplatz-4.jpg" %}

Ash

{% include image-slider-base.html %}
