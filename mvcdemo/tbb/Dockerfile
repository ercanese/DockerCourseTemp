FROM mcr.microsoft.com/dotnet/sdk:7.0 as eebuild
WORKDIR /app

COPY . .

RUN dotnet restore
RUN dotnet publish --configuration Release -o out


FROM mcr.microsoft.com/dotnet/aspnet:7.0

WORKDIR /app

COPY --from=eebuild /app/out .

CMD [ "dotnet","tbb.dll" ]
