FROM golang:1.20-alpine AS build

WORKDIR /app

COPY go.mod ./
RUN go mod download

COPY . .

RUN go build -o app

FROM alpine:latest

WORKDIR /root/

COPY --from=build /app/app .

EXPOSE 8080

CMD ["./app"]