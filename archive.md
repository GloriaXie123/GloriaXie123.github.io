---
layout: page
title: Blog Archive
---

<div class="tags-menu">
  <h2>Tags</h2>
  <div class="tag-cloud">
    {% assign sorted_tags = site.tags | sort %}
    {% for tag in sorted_tags %}
      <a href="/tag/{{ tag[0] | downcase | replace: ' ', '-' }}/" class="tag-link">
        {{ tag[0] }} ({{ tag[1].size }})
      </a>
    {% endfor %}
  </div>
</div>

<hr>

{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.date | date: "%B %Y" }} - {{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}