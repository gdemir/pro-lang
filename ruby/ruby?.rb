#!/usr/bin/ruby
#say! <.to_a>!
puts (1..3).to_a

#tekrarla!-------------------
puts "gdemir" * 3
#-------False-------#
#puts 3 * "gdemir"
#-------------------#
#uzunluk dön! <.length>!
puts "gdemir".length

#dizi tanımla!
s = ["gdemir", "ecylmz", "csfyldz"]

#do yapısı!
s.each do |x|
  print x + " "
end
puts ""

#fraklı do yapısı! <.each>!
(1..4).to_a.each { |x| if x % 2 == 0 then print "2 ye bölünen", x, " dir\n" end}

#while yapısı ve <.to_s> yapısı!
i = 150
while i < 200 do
  puts "i: " + i.to_s
  i += 20
end
#for yapısı!
for i in 1..4
  puts "2 x " + i.to_s + " = " + (i * 2).to_s
end
#karakter alma denemesi!
al = gets
print  al * 2
