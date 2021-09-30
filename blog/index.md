---
layout: default
regenerate: true
active-tab: blog
---

# Blog

---

<!-- LEGEND -->

### Legend

---

<!-- POST LIST -->

### Posts

{% assign filtered-posts = site.posts | where: "categories", "blog" %}

{% for post in filtered-posts %}

    {% assign category = post.categories[1] %}

    {% include blog-post-entry.html post=post %}
        
{% endfor -%}
