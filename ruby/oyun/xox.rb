#!/usr/bin/ruby

# xox oyunu. (tictactoe game)
# copyrigth gdemir
# http://gdemir.me

class G_xox

  def initialize
    @player = 'x'
    @cpu = 'o'
    @row = ["a", "b", "c"]
    @col = ["1", "2", "3"]
    @kafa = [
             "a1", "a2", "a3",
	     "b1", "b2", "b3",
	     "c1", "c2", "c3"
	    ]
    @alan = field
  end

  def field # xox sahasını en başta nil'le.
    Hash[*(@kafa).map { |alan| [alan, nil] }.flatten]
  end

  def in?(str, aranan) # "a1a2a3" içerisinde "a1" arar, true/false döner.
    (0..100).select { |sayi| sayi % 2 == 0}.each  do |i|
      return true  if aranan == str[i..i + 1]
      return false if i >= str.length
    end
  end

  def display # xox sahasını çiz.
    row, col = @row.clone, @col.clone
    @kafa.each do |yer|
      chr = @alan[yer]
      print row.shift," "       if  in?("a1b1c1", yer)
      print "   "           unless  chr
      print  " " , chr, " "     if  chr
      print "\n  ---+---+---\n" if  in?("a3b3", yer)
      print "|"              unless in?("a3b3c3", yer)
    end
    puts # void
    col.each { |i| print "   ", i }
  end

  def move(hedef) # verilen hedef'e göre hamle yap.
    for yer1 in @alan.keys
      for yer2 in @alan.keys
        h1, s1 = yer1[0].chr, yer1[1].chr
	h2, s2 = yer2[0].chr, yer2[1].chr
        harf, sayi = @row.clone, @col.clone
        if @alan[yer1] == hedef and @alan[yer2] == hedef and yer1 != yer2
          if h1 == h2
            sayi -= [s1, s2]
            return h1 + sayi[0]      unless @alan[h1 + sayi[0]]
          elsif s1 == s2
            harf -= [h1, h2]
	    return harf[0] + s1      unless @alan[harf[0] + s1]
          elsif h1 != h2 and s1 != s2 and (yer1 == "b2" or yer2 == "b2")
            sayi -= [s1, s2]
            harf -= [h1, h2]
            return harf[0] + sayi[0] unless @alan[harf[0] + sayi[0]]
          end
        end
      end
    end
    nil
  end

  def cpu # otomatik önce saldırı, olmazsa savunma o da olmazsa, rastgele boş yer dön.
    # ana hamle
    return "b2" if @alan["b2"] == nil

    # saldırı => @cpu oyun bitirmek için saldırı yapılacak yer varsa yeri dön.
    yer = move(@cpu)
    return yer if yer

    # savunma => @player'a karşı savunma yapılacak yer varsa yeri dön.
    yer = move(@player)
    return yer if yer

    # random  => rastgele ve boş bir yer dön.
    begin
        yer = @kafa[rand(9)]
    end until @alan[yer] == nil
    return yer
  end

  def full? # bütün alanların değerleri nil'den farklı ise; yani fullsa, true dön.
    (@alan.values - [nil] * 9).length == 9
  end

  def win? # kazanan ?.

    return "tie" if full?

    # sütunları kontrol et.
    [0, 1, 2].each do |i|
      p = @alan[@kafa[i]]
      return p if p == @alan[@kafa[i + 3]] && p == @alan[@kafa[i + 6]]
    end

    # satırları kontrol et.
    [0, 3, 6].each do |i|
      p = @alan[@kafa[i]]
      return p if p == @alan[@kafa[i + 1]] && p == @alan[@kafa[i + 2]]
    end

    # çapraz hatları kontrol et.
    [[0, 8], [2, 6]].each do |i|
       p = @alan[@kafa[4]]
       return p if p == @alan[@kafa[i[0]]] && p == @alan[@kafa[i[1]]]
    end

    # yenen yoksa, nil dön.
    nil
  end

  def choose_place # boş olana kadar, dön ve boş yer seç.
    while true
      yer = gets.chomp!
      return yer unless @alan[yer]
      print "Please, choose empty field "
    end
  end

  def pre_data # hamle taşları görüntüle.
    puts "-------------------------------"
    puts "Player  move stone : #{@player}"
    puts "Cpu     move stone : #{@cpu}   "
    puts "Example move 'b2'              "
    puts "-------------------------------"
  end

  def the_end # kazananı ekrana bas.
    puts # void
    puts "-------------"
    puts "  tie game   " if win? == "tie"
    puts "   you win   " if win? == @player
    puts "   cpu win   " if win? == @cpu
    puts "-------------"
  end

  def play
    ilk = [false, true][rand(2)]

    # ilk Cpu' mu oynasın ?
    @alan[cpu()] = @cpu if ilk

    pre_data
    display
    while true

      print "\nPlayer playing... "
      yer = choose_place
      @alan[yer] = @player
      display
      break if win? # kazanan varsa çık

      puts "\nCpu playing..."
      sleep 1
      @alan[cpu] = @cpu
      display
      break if win? # kazanan varsa çık
    end
    the_end
  end
end

t = G_xox.new()
t.play
