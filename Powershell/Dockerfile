#-- hangi imajı kullancağız base imajı
#-- hangi komutlarını caşıstıracağız
#-- hangi dosyaları kopyalayacağız
#-- container calısırken hangı komutla calısacak

FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y wget apt-transport-https software-properties-common
RUN wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb"
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb
RUN apt-get update
RUN apt-get install -y powershell

LABEL os.version=ubuntu20.04

WORKDIR /app

COPY Time.ps1 .

CMD ["pwsh","Time.ps1"]