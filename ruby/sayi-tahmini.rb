#!/usr/bin/ruby
def uret() rand(100) end
hedef = uret()
begin
  tahmin = gets.to_i
  if    tahmin < hedef then puts "sayıyı büyültün"
  elsif tahmin > hedef then puts "sayıyı küçültün"
  end
end until hedef == tahmin
puts "tebrikler bildiniz!"
