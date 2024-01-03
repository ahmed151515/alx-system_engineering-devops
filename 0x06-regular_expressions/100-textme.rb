#!/usr/bin/env ruby
SENDER = ARGV[0].match(/from:(\W?\w+)/)[1]
RECEIVER = ARGV[0].match(/to:(\W?\w+)/)[1]
FLAGS = ARGV[0].match(/flags:([^ \]]+)/)[1]

puts "#{SENDER},#{RECEIVER},#{FLAGS}"
