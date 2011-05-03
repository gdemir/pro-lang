#!/usr/bin/ruby
#-*- coding:utf-8 -*-

# istediginiz kullanıcının
# tüm repoları/gistleri indiren betik.
# author : gdemir
# http://gdemir.me

# DIKKAT!
# open-uri ve net/http ruby 1.9.2'de standart olarak geliyor.
# Bkz : http://www.ruby-doc.org/stdlib/
# json ve highline kurmanız gerekiyor, kurulum :
# sudo apt-get install rubygems
# sudo apt-get install gem
# sudo gem install highline
# sudo gem install json

require 'open-uri'
require 'net/http'
require 'json'
require 'highline/import'

# http://develop.github.com'deki repoları al(payload)
def get_repos(user)
  url = URI.parse("http://github.com/api/v1/json/#{user}")
  veri = Net::HTTP.post_form(url, {})
  repos = JSON.parse(veri.body)["user"]["repositories"]
end

# http://develop.github.com'deki gistleri al(payload)
def get_gists(user)
  url = URI.parse("http://gist.github.com/api/v1/json/gists/#{user}")
  veri = Net::HTTP.post_form(url, {})
  gists = JSON.parse(veri.body)["gists"]
end

# url sağlam mı kontrol et düzenlenecek TODO
def validurl?(url)
  response = open(url)
  true
  rescue OpenURI::HTTPError => e
  $stderr.puts "#{e}"
  false
end

# hata iletisi
def die(msj)
  $stderr.puts "err : #{msj}"
  exit(19)
end

# kullanıcıya sor bakalım ne diyor ?
def yesno(ask, default)
  case default
   when /[eEyY]*/; prompt = "|E/h|"
   when /[hHnN]*/; prompt = "|e/H|"
  end
  loop do
    print "#{ask} #{prompt}"
    answer = gets
    answer = default if answer == "\n"
    case answer
      when /(^[Ee]|[yY])/; return true
      when /(^[Hh]|[Nn])/; return false
     else print "Lütfen [e]vet veya [h]ayır girin"
    end
  end
end

# oluşturma ya da tekrardan oluşturup güncellemesini sor
def update_or_install(dir, process)
  if File::exists?(dir)
    # sor dizin var ise ne yapılsın ?
    if yesno "#{dir} dizini mevcut tekrardan oluşturmak istiyor musunuz?", "e"
      system("rm -rf #{dir}")
      system(process)
    end
  else
    system(process)
  end
end

# ev dizinine gecelim.
Dir.chdir(ENV['HOME'])
puts "tüm işlemler ev dizini [~/] üzerinden yapılacak"

# github kullanıcı isimini al.
user = ask("github kullanıcı? ") { |q| q.readline = true; q.default = ENV['USER'] }
puts "kullanıcı kontrol ediliyor..."
# kullanıcı ismi doğru mu?
die("böyle bir kullanıcı yok") unless validurl?("https://github.com/" + user)

# sor : repo indirmek istiyor mu ?
if yesno "repoları indirmek istiyor musunuz?", "e"
  # sor : repoların ineceği dizin ismi ?
  repo_dir = ask("repo dizini? ") { |q| q.readline = true; q.default = "projects" }
  update_or_install(repo_dir, "mkdir #{repo_dir}")

  # dizine gir ve repo'ları indir
  Dir.chdir(ENV['HOME'] + "/" + repo_dir)
  puts "github kullanıcı adı ve parola istenebilir"
  puts "repolar indiriliyor..."
  get_repos(user).each do |repo|
    update_or_install(repo["name"],
    "git clone git@github.com:" + user + "/" + repo["name"] + ".git")
  end
end

# sor : gist indirmek istiyor mu ?
if yesno "gistleri indirmek istiyor musunuz?", "h"
  # sor : gistlerin ineceği dizin ismi ?
  gist_dir = ask("gist dizini? ") { |q| q.readline = true; q.default = "gist" }
  update_or_install(gist_dir, "mkdir #{gist_dir}")

  # dizine gir ve gist'lerı indir
  Dir.chdir(ENV['HOME'] + "/" + gist_dir)
  puts "github kullanıcı adı ve parola istenebilir"
  puts "gistler indiriliyor..."
  get_gists(user).each do |gist|
    update_or_install(gist["repo"],
    "git clone git@gist.github.com:" + gist["repo"] + ".git")
  end
end
