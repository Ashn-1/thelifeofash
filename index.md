---
layout: default
---

# the Life of Ash

Hey there,

welcome to my blog!

Here you can find all my posts, be it longer blog posts, daily entries, short stories or art.

Thank you for reading  
Ash {% include socials.html %}

---

## Post Categories

- <a class="grey-link" href="/blog/"><span style="font-weight: bold;">Blog Post;</span></a> longer, more in-depth posts about a specific topic
- <a class="grey-link" href="/daily/"><span style="font-weight: bold;">Daily Entries;</span></a> short, braindumpy entries about something out of my life
- <a class="grey-link" href="/art/"><span style="font-weight: bold;">Art;</span></a> poetry, music, drawings, and all other things artsy
- <a class="grey-link" href="/story/"><span style="font-weight: bold;">Stories;</span></a> fictional stories

---

## Blog Posts + Stories

{% assign story_posts = site.posts | where: "categories", "story" %}
{% assign blog_posts = site.posts | where: "categories", "blog" %}
{% assign relevant_posts = story_posts | concat: blog_posts | sort: "date" | reverse %}

{% for post in relevant_posts %}

    {% assign category = post.categories[1] %}

    {% include blog-post-entry.html post=post %}
        
{% endfor -%}
