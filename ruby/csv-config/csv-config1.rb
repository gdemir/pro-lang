#!/usr/bin/ruby
require 'csv'
##[global]#############################################################
$kisiler = {}       #db.csv'den okunan bilgilerin tutuldugu sozluk
$csvname = "UZEM.csv" #okunacak db'nin adı.
$kafa = []	    #csv dosyasının ilk satırı.(örn : ["ad", "soyad", "no"])
$key = "tc"	    #herhangi bir csv de key olarak seçeceginiz ifade.
$value = []         #$kafa'nın keysiz hali.(örn : ["ad", "soyad"])
#######################################################################
#
#
# csv'de alanlar "ad", "sd" ,"no", "un" olsun.
# global olarak $key = "no" seçerseniz, yükleme sırasında
#   kisiler = {
#                  no => { "ad" => "gokhan", "sd" => "demir", "un" => "gdemir"},
#                  no => { "ad" => "emin",   "sd" => "eker",  "un" => "eeker" },
#             }
#
#  ve  $kafa = ["no", "ad", "sd", "un"],  $value = ["ad", "sd", "un" ]olacak,
#
#  şekilde yükleyecektir.Örneğin csv'de gokhanın no'su "12345" olsun.
#
#  ÖRNEK[1] : ogrenci = $kisiler["12345"] denirse,
#                 print ogrenci  -->  {"ad" => "gokhan", "sd" => "demir", "un" => "gdemir"} döner.
#
#  ÖRNEK[2] : ogrenci = $kisiler["12345"]
#                 print ogrenci["ad"]  --> "gokhan" döner.
#
#  ÖRNEK[3] : for no in $kisiler.keys
#                 print $kisiler[no]["ad"]  --> "gokhan", "emin" döner.

def _values(kisi, key_indis, sozluk)
  $kafa.each_index do |indis|
    alan = $kafa[indis]
      sozluk[alan] = kisi[indis] if indis != key_indis
  end
  sozluk
end

def yukle
  oku = CSV.open($csvname, "r")
  $kafa = oku.shift   # ["no","ad","sd","un"]
  *$value = *$kafa
  key_indis = $kafa.index($key)
  $value.delete($key) # ["ad", "sd", "un"]
  oku.each { |kisi|
    $kisiler[kisi[key_indis]] = _values(kisi, key_indis, {})
  }
end

def bosalt
  CSV::Writer.generate(File.open($csvname, "w")) do |csv|
    csv << $kafa
    $kisiler.each do |no, value|
      yaz = []
      yaz << no
      $value.each { |v|  yaz << value[v]}
      csv << yaz
    end
  end
end

# ör. kullanım :

# yukle
# for kisi in $kisiler.values
#  puts kisi["no"]
# end

# veya

# yukle
# for no in $kisiler.values
#  puts kisi["no"]["ad"]
# end
