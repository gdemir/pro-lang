#!/bin/sh

LOG="$HOME/sys.log"
vimfile="$HOME/.vimrc"

# log -> bosalt
cat /dev/null >$LOG

[ -n $(which unzip) ] || { echo >>$LOG "Lutfen unzip programini kurun"; exit 1; }
[ -n $(which vim) ] || { echo >>$LOG "Lutfen vim programini kurun"; exit 1; }
[ -f $vimfile ]; && { echo >>$LOG "hata : .vimrc dosyasi zaten mevcut"; exit 1; }
echo "[vim] ayarlari yukleniyor..."

if ! wget -O SingleCompile.zip 'http://www.vim.org/scripts/download_script.php?src_id=14010' 2>/dev/null;then
	echo >>$LOG "hata : bir nedenle SingleComplie.zip'ini indirilemedi"; exit 1;
fi
if ! unzip -d ~/.vim SingleCompile.zip 2>/dev/null;then
	echo >>$LOG "hata : unzip programi SingleComplie.zip'i acamadi"; exit 1;
fi
echo "ok : derle/calistir ayari yuklendi.."

echo \
"#!/bin/sh
set background=dark
syntax enable
map <f9> :SCCompile<cr>
nmap <c-f9> :SCCompileRun<cr>
map <f5> :w\| !ruby % <cr>
map <f4> :w\| !python % <cr>
" >>$vimfile
echo "ok : ~/.vimrc ayarlari yuklendi.."

echo "ok : vim ayarlari yüklendi."
