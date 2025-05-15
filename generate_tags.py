#!/usr/bin/env python3
import os
import yaml
import glob

def generate_tag_pages():
    # Create tags directory if it doesn't exist
    if not os.path.exists('tags'):
        os.makedirs('tags')
    
    # Get all posts
    posts = glob.glob('_posts/*.md')
    
    # Collect all tags
    all_tags = set()
    for post in posts:
        with open(post, 'r', encoding='utf-8') as f:
            content = f.read()
            if '---' in content:
                front_matter = content.split('---')[1]
                try:
                    metadata = yaml.safe_load(front_matter)
                    if metadata and 'tags' in metadata:
                        all_tags.update(metadata['tags'])
                except yaml.YAMLError:
                    continue
    
    # Generate tag pages
    for tag in all_tags:
        tag_filename = tag.lower().replace(' ', '-')
        tag_path = os.path.join('tags', f'{tag_filename}.md')
        
        if not os.path.exists(tag_path):
            with open(tag_path, 'w', encoding='utf-8') as f:
                f.write(f'''---
layout: tag
title: {tag}
tag: {tag}
---
''')
            print(f'Generated tag page for: {tag}')

if __name__ == '__main__':
    generate_tag_pages() 