---
layout: page
title: Blog Archive
---

<div class="archive-container">
  <div class="tags-sidebar">
    <h3 class="tags-heading">Tags</h3>
    {% assign sorted_tags = site.tags | sort %}
    {% for tag in sorted_tags %}
      <div class="tag-group">
        <div class="tag-name">{{ tag[0] }} ({{ tag[1].size }})</div>
        <ul class="tag-posts">
          {% for post in tag[1] %}
            <li><a href="{{ post.url }}">{{ post.date | date: "%B %Y" }} - {{ post.title }}</a></li>
          {% endfor %}
        </ul>
      </div>
    {% endfor %}
  </div>
</div>