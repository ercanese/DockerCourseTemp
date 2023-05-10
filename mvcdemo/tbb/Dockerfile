FROM mcr.microsoft.com/dotnet/sdk:7.0 as buildercan
WORKDIR /app

COPY *.csproj .
RUN dotnet restore

COPY . . 
RUN  dotnet publish --configuration Release -o out


FROM mcr.microsoft.com/dotnet/aspnet:7.0 
WORKDIR /app

COPY --from=buildercan /app/out .

EXPOSE 80

CMD ["dotnet","tbb.dll"]
