#!/usr/bin/ruby
require "config_v2.rb"

def IN(liste, elt)
  return nil if liste == nil
  liste.each { |item| return 1 if item == elt }
  return nil
end

def main(csv)

  c2010 = Yukle.new(csv, "tc")

  depo = { nil => [] }
  #Yukle.class kullanma biçimi BEGIN
  c2010.kisiler.each do |gore, kisi|
    if IN(depo.keys, kisi["un"]) # liste'nin içinde var mı ?
      depo[kisi["un"]] << kisi
    else
      depo[kisi["un"]] = [kisi]
    end
  end
  #Yukle.class END

  i = 0
  depo.each do |mesaj, liste|
    kisiler = Hash[*liste.map { |kisi| [kisi["tc"], kisi] }.flatten]
    Bosalt.new(kisiler, ["tc", "un"], "part" + i.to_s + ".csv")
    i += 1
  end

end

csv = ARGV.shift or die "Kullanım: #{$0} <csvdosya>"
FileTest.exists? csv or die "Dosya #{csv} bulunamadı"
main(csv)

#Bosalt.new(c2010, csv)
