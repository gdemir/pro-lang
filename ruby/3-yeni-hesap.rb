#!/usr/bin/ruby
require 'config.rb'


# murat emre, demir için m.demir e.demir me.demir ismini üreten,
# mert demir için için m.demir ismini üreten uniq üretici fonksiyon.
def uniq_uret(ad, sd)
  ad = ad.split
  unames = []
  unames << ad[0][0].chr + sd.to_s
  if ad.length == 2
    unames << ad[1][0].chr + sd
    unames << ad[0][0].chr + ad[1][0].chr + sd
  end
  unames
end

# ali demir için a.demir kullanıldıgından;
# al.demir ali.demir şeklinde pramit isim listesi üretir.
def pramitisim_uret(ad, sd)
  a = []
  (0..(ad.length)).each { |i| a << ad[0..i] + sd }
  a
end

# uniq isim dısında pramit şekilde isim üreten fonksiyon.Yani
# ilk ismi pramit şeklini üret, eger 2 ismi varsa 2. isminin pramit şeklini üret
def allias_uret(ad, sd)
  ad = ad.split()
  anames1 = pramitisim_uret(ad[0], sd)
  if ad.length == 2 then
    anames2 = pramitisim_uret(ad[1], sd)
    return anames1 + anames2
  end
 return anames1
end

# kisiye isimleri numaralı şekilde secmesi için secim sunan fonksiyon.
def secim(names)
  puts "isimlerden numarasını girip seçiniz"
  names.each_with_index do |value, indis|
    puts indis.to_s + " " + value
  end
  return names[input("seçiminiz?")]
end

# önceden kullanılmış isimleri listeden ayıklayıp,
# listenin yeni halini dönen fonksiyon.
def cakisma_kontrol(olasiliklar)
  for no in $kisiler.keys
     olasiliklar.delete($kisiler[no]["un"])
  end
  olasiliklar
end

def tara(no)
  no[no.length - 1] = ""
  if $kisiler.has_key?(no) then
    return $kisiler[no]
  else
    sozluk = {}
    for alan in $value
      sozluk[alan] = nil
    end
    return sozluk
  end
end

def bilgi_kontrol(ad, sd, un)
   ad == nil or sd == nil or un != nil
end

def input(msj)     puts msj
  gets.to_i
end

def raw_input(msj) puts msj
  gets.to_s
end

def main
  #kisiler = {} listesine kişilerin bilgilerini yükle $kisiler = { no => {"ad" => ad, "sd" => sd, "un" => un}} (bknz : config.py)
  yukle
  bilgi = tara(raw_input("numaraniz?"))
  ad, sd, un = bilgi["ad"], bilgi["sd"], bilgi["un"]
  # kisinin ad,soyad boşmu veya uniq ismi atanmış mı daha önceden diye kontrol et
  if bilgi_kontrol(ad, sd, un) then
    puts "kisinin ismi veya soy ismi bulunmamaktadır ya da uniq ismi atanmıştır"
    return
  end
  # uniq olasılıkları uret
  olasiliklar = uniq_uret(ad, sd)
  # uniq olasıklarından önceki bir kayıtta kullanılmış mı diye kontrol et, ayıkla
  unames = cakisma_kontrol(olasiliklar)
  if unames == [] then
    olasiliklar = allias_uret(ad, sd)
    #allias olasılıklarından önceki bir kayıtta kullanılmış mı diye kontrol et, ayıkla
    anames = cakisma_kontrol(olasiliklar)
    #allias isimlerini secime sun ve bilgi[2] yani un değişkenine kişinin seçtigine ata
    bilgi["un"] = secim(anames)
  else
    #allias isimlerini secime sun ve bilgi[2] yani un değişkenine kişinin seçtigine ata
    bilgi["un"] = secim(unames)
  end
  #kisiler = {} listesindeki bilgileri yaz (bknz : config.py)
  bosalt
end
if ARGV.length != 0
 puts "kullanım : ./3-yeni-hesap.rb"
 exit 1
end
main
