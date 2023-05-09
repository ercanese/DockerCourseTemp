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
docer rm $(docker ps -qa)