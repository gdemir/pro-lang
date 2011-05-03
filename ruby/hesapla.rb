#!/usr/bin/ruby
def err(pn)
  "kullanım : <./hesapla> <girdi_1> <girdi_2>"
end
def sum(arg1,arg2)
  arg1 + arg2
end

err(ARGV) if ARGV.length != 2

puts sum(ARGV[0].to_i, ARGV[1].to_i)

