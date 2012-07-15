#!/bin/sh

LOG="$HOME/sys.log"
tmuxdir="/etc/tmux/"

# log -> bosalt
cat /dev/null >$LOG

[ -n $(which unzip) ] || { echo >>$LOG "Lutfen unzip programini kurun"; exit 1; }
[ -n $(which tmux) ] || { echo >>$LOG "Lutfen tmux programini kurun"; exit 1; }
[ -x $tmuxdir ] && { echo >>$LOG "hata : /etc/tmux/ dizini zaten mevcut"; exit 1; }
echo "[tmux] ayarlari yukleniyor..."

wget 'http://gdemir.me/file/tmux.zip' 2>/dev/null 1>&2 || { echo >>$LOG "hata : tmux.zip'i indirilemedi"; exit 1; }
echo "ok : http://gdemir.me/file/tmux.zip indirildi.."

unzip tmux.zip 2>/dev/null 1>&2 || { echo >>$LOG "hata : unzip programi tmux.zip'i acamadi"; exit 1; }
echo "ok : tmux dizini cikarildi.."

sudo mv ~/tmux /etc/
sudo ln -s /etc/tmux/rc/default ~/.tmux.conf 2>/dev/null 
grep "tmux" ~/.bashrc && { echo >>$LOG "hata : ~/.bashrc tmux yonlendirmesine sahip"; exit 1; }
echo "tmux 2>/dev/null 1>&2" >>~/.bashrc
echo "ok : ~/.bashrc'ye yonlendirme eklendi.."

echo >>$LOG "ok : tmux ayarlari yuklendi"
echo "yukleme tamamlandi"
