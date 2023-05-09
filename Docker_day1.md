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


