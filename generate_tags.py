import os
import yaml

POSTS_DIR = "_posts"
TAGS_DIR = "tags"
LAYOUT = "tag"

if not os.path.exists(TAGS_DIR):
    os.mkdir(TAGS_DIR)

all_tags = set()

for filename in os.listdir(POSTS_DIR):
    if filename.endswith(".md"):
        with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8') as f:
            front_matter = []
            lines = f.readlines()
            if lines[0].strip() == "---":
                for line in lines[1:]:
                    if line.strip() == "---":
                        break
                    front_matter.append(line)
            data = yaml.safe_load("".join(front_matter))
            if data and "tags" in data:
                all_tags.update(data["tags"])

for tag in all_tags:
    tag_slug = tag.lower().replace(" ", "-")
    tag_file = os.path.join(TAGS_DIR, f"{tag_slug}.md")
    if not os.path.exists(tag_file):
        with open(tag_file, 'w', encoding='utf-8') as f:
            f.write(f"""---
layout: tag
tag: {tag}
permalink: /tags/{tag_slug}/
---""")

