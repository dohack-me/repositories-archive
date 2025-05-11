FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env

WORKDIR /app

COPY *.csproj ./
RUN dotnet restore

COPY . ./

RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:6.0

WORKDIR /app

COPY --from=build-env /app/out .
COPY --from=build-env /app/flag.txt .

RUN apt-get update && apt-get install -y socat

EXPOSE 8000

CMD ["socat", "TCP-LISTEN:8000,nodelay,reuseaddr,fork", "EXEC:dotnet LionExchange1.dll"]