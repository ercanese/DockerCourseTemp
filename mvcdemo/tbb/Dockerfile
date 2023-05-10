FROM mcr.microsoft.com/dotnet/sdk:7.0 as ercanbuid
WORKDIR /src
COPY *.csproj .
RUN dotnet restore
COPY . .
RUN dotnet publish --configuration Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:7.0 as final
WORKDIR /app
COPY --from=ercanbuid /src/out .
EXPOSE 80

CMD ["dotnet","tbb.dll"]