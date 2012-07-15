#!/usr/bin/ruby
require 'csv'

def die(*msg)
  $stderr.puts(*msg)
  exit 1
end

class Unit
  def ac(type, csv, islem)
    begin
      fp = type.open(csv, islem)
    rescue Exception => e
      die "CSV dosya okuma veya yazmada hata: #{e}"
    end
  return fp
  end
end

class Yukle < Unit
  attr_accessor :kisiler, :kafa
  def initialize(csv, gore = "tc")
    @kisiler = {}
    @gore = gore
    oku = ac(CSV, csv, "r")
    @kafa = oku.shift

    # bir şablon oluşturalım, tüm kayıtlar bunun gibi olmalı
    bunungibi = Hash[*@kafa.map { |alan| [alan, nil] }.flatten]

    oku.each do |kisi|
      # şablondan çoğalt
      kayit = bunungibi.clone
      # csv satırda her alanı kafadaki sırayla al
      @kafa.each { |alan| kayit[alan] = kisi.shift }
      #  artık bir nesne oluşturup ekleyebiliriz
      @kisiler[kayit[@gore]] = kayit
    end
  end
end

class Bosalt < Unit
  def initialize(kisiler, kafa, csv)
    yaz = ac(File, csv, "w")

    CSV::Writer.generate(yaz) do |row|
      # csvnin ilk satırına kafa bilgisini ekle
	  row << kafa

      kisiler.each do |no, kisi|
        # kisilerden her kisinin bilgilerini temp'e doldur sonra satıra ekle
        temp = []
        kafa.each { |alan|  temp << kisi[alan].to_s}
        row << temp
      end
    end
  end
end

# csv = ARGV.shift or die "Kullanım: #{$0} <csvdosya>"
# FileTest.exists? csv or die "Dosya #{csv} bulunamadı"

# ör. kullanim :
# c2010 = Yukle.new "bil305.csv", "no"

# c2010.kisiler.each do |gore, kisi|
#   puts gore
# end

# Bosalt.new c2010.kisiler, c2010.kafa, "bil305-new.csv"
