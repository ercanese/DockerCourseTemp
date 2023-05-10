#First
docker --version

#registry üzerinden imaj çekmek için kullanılan komut.
docker pull <imagename>
#imajları tutuğumuz yere registry veya repository diyoruz.
#imajları listelemek için.
docker images #or
docker image ls


#imajdan container türetmek için.
docker run <o_arg> <r_imagename> <o_commands>
docker run busybox echo Hello World
docker run busybox date

#examples
#busybox imajından container türeterek ekranada hello world ve şu anki date yazalım.
#ubuntu imajından container türeterek hello world ve date ekrana yazalım.
docker run ubuntu echo hello world
docker run ubuntu date

#çalışan containerları listelemek için docker ps kullanılır.
docker ps
#tüm çalışan veya çalışmayan containerları listelemek için 
docker ps -a

#container çalıştırılken içerisine(terminal) girip komut çalıştırmak için.
docker run -it ubuntu /bin/bash
#ubuntu imajı içerisine girip mkdir demo ile bir klasör oluşturup çıkalım.
docker run -it ubuntu /bin/bash
mkdir demo
exit
docker run -it ubuntu /bin/bash
apt update 
apt install figlet
exit
#container silmek için
docker rm <containerid>
#tüm containerları silmek için
docker rm $(docker ps -qa)
#container idleri sadece döndürmek için.
docker ps -qa


#bir container ayakara durabilmesi için devamlı çaşılan bir processe ihtiyacı vardır,
docker run jpetazzo/clock
ctrl+c
#arka planda container çalıştırmak istiyorsak.
docker run -d jpetazzo/clock

#docker üzerindeki tüm objelerin özelliklerini ve değerlerini ekranda görmek için.
docker inspect <objectid>
docker inspect 4aa

#container içerisinden logları görebilmek için.
docker logs
#logları takip etmek için
docker logs 23a --follow 
#tail komutuyla gelecek log sayısını belirtebiliriz.
docker logs 43a --tail 3
#en son oluşturulan container hangisi
docker ps -l

#clock uygulamasını arka planda 3 adet çalışacak şekilde oluşturun isimleri
#clock1 2 3 olarak oluşsun.
#3 container loglarını ekranda en son 2 tane logu görecek şekilde loglarına bakalım.
#2. containerında follow komutuyla loglarını takip edelim.
docker run -d --name clock1 jpetazzo/clock
docker run -d --name clock2 jpetazzo/clock
docker run -d --name clock3 jpetazzo/clock

docker logs clock3 --tail 2
docker logs clock2 --follow 

#bir containerı sağlıklı durdurmak için.
docker stop <containerid>
docker stop 12a
#bir containeri direk kapatmak için.
docker kill 12a
docker kill <containerid>
#çalışan bir container durdurmak ve silmek için.
docker rm 12a --force

#çalışan bir container restart etmek için.
docker restart <containerid>
docker restart 1a2

#durmus olan bir container başlatmak için.
docker start <containerid>
docker start 1a2

#imajları indirirken tage göre indirmek için.

docker pull ubuntu:18.04

#tage göre çalıştırmak için
docker run ubuntu:18.04


#alpine imajı 1.4 versiyonunu indirelim ve it komutu ile içerisine girip
cat /etc/os-release komutyla versiyonu kontrol edelim. 
docker pull alpine:1.14
docker run -it alpine:1.14 /bin/sh
cat /etc/os-release

#ubuntu 23.04 imajını indirelim ve ondan it komutu ile bir container türetelim.
#yukarıdaki komutu kullanarak versiyonu görüntüleyelim.
docker  pull ubuntu:23:04
docker run -it ubuntu:23.04 /bin/bash
cat /etc/os-release

#redis 6.0alpine versiyonunu indirelim.
docker pull redis:6.0-alpine
docker run -d --name redis


#imaj silmek için.
docker rmi <imageid>
docker rmi 123
docker rmi 123 --force

#çalışan bir container içerisine girmek için.
docker exec -it <containerid> /bin/sh
docker exec -it 213a /bin/bash
docker exec 212a date

#bir adet redis container ayağa kaldıralım ve
#exec komutu ile terminaline girerek klasör oluşturalım.
mkdir demo
exit


#PowerShell projesi

docker pull ubuntu
docker run -it --name powershell ubuntu /bin/bash

apt-get update
# Install pre-requisite packages.
apt-get install -y wget apt-transport-https software-properties-common
# Download the Microsoft repository GPG keys
wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb"
# Register the Microsoft repository GPG keys
dpkg -i packages-microsoft-prod.deb
# Delete the the Microsoft repository GPG keys file
rm packages-microsoft-prod.deb
# Update the list of packages after we added packages.microsoft.com
apt-get update
# Install PowerShell
apt-get install -y powershell

apt install nano

mkdir app
cd app
nano time.ps1
<code paste>

ctrl x
y
enter

pwsh time.ps1

exit

#oluşturduğumuz containerları imaj haline çevirmek için.
docker commit  <containerid> <imagename>:<tag>
docker commit 213a powershell:v1

docker run powershell:v1 pwsh /app/time.ps1

#imaj haline çevirirken change parametresi ile cmd veya workdir değiştirmek.
docker commit --change='CMD ["pwsh","/app/time.ps1"]' 12a powershell:v2
docker commit --change='CMD ["pwsh","time.ps1"]' --change='WORKDIR /app' 12a powershell:v2



