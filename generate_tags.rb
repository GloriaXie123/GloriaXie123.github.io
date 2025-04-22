require 'fileutils'

tag_dir = "tag"
FileUtils.mkdir_p(tag_dir)

posts = Dir["_posts/*.{md,markdown}"]

tags = posts.flat_map do |file|
  content = File.read(file)
  if content =~ /tags:\s*\[(.*?)\]/m
    $1.split(',').map { |t| t.strip.gsub(/["']/, '') }
  else
    []
  end
end.uniq

tags.each do |tag|
  slug = tag.downcase.strip.gsub(' ', '-')
  filepath = "#{tag_dir}/#{slug}.md"

  File.open(filepath, 'w') do |f|
    f.puts "---"
    f.puts "layout: tag"
    f.puts "title: \"#{tag}\""
    f.puts "tag: #{tag}"
    f.puts "permalink: /tag/#{slug}/"
    f.puts "---"
  end
end
