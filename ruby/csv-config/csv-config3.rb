#!/usr/bin/ruby
require 'csv'

module Unit
  def ac(type, csv, islem)
    begin
      fp = type.open(csv, islem)
    rescue Exception => e
      die "CSV dosya okuma veya yazmada hata: #{e}"
    end
  return fp
  end
  def die(*msg)
    $stderr.puts(*msg)
    exit 1
  end
end

class Csv
  attr_accessor :kisiler, :kafa, :name

  include Unit
  def initialize(name, gore = "tc")
    @kisiler = {}
    @gore = gore
    @name = name
  end
  def yukle()
    oku = ac(CSV, @name, "r")
    @kafa = oku.shift

    bunungibi = Hash[*@kafa.map { |alan| [alan, nil] }.flatten]

    oku.each do |kisi|
      kayit = bunungibi.clone
      @kafa.each { |alan| kayit[alan] = kisi.shift }
      @kisiler[kayit[@gore]] = kayit
    end
  end
  def bosalt(kafa = @kafa, name = @name)
    yaz = ac(File, name, "w")

    CSV::Writer.generate(yaz) do |row|
      row << kafa
      @kisiler.each do |no, kisi|
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
# csv = Csv.new "db.csv", "no"
# csv.yukle  # dosyayı oku
# puts csv.kafa # dosya baslıgı

# csv.kisiler.each do |gore, kisi|
#   puts gore
# end

# csv.bosalt csv.kafa, "db-new.csv"
