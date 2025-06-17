---
layout: page
title: Blog Archive
---

<div class="archive-container">
  <div class="tags-sidebar">
    <h2>Tags</h2>
    {% assign sorted_tags = site.tags | sort %}
    {% for tag in sorted_tags %}
      <div class="tag-group">
        <div class="tag-name">{{ tag[0] }} ({{ tag[1].size }})</div>
      </div>
    {% endfor %}
  </div>
</div>