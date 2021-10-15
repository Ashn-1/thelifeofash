---
layout: default
title: Daily
regenerate: true
active-tab: story
---

# Stories

{% assign filtered-posts = site.posts | where: "categories", "story" %}

{% for post in filtered-posts %}

    {% assign category = post.categories[1] %}

    {% include blog-post-entry.html post=post %}
        
{% endfor -%}
