# Stage 1
FROM golang:1.11-alpine3.8 as builder
COPY ./main.go ./
RUN go build -o /app ./main.go

# Stage 2
FROM alpine:latest
EXPOSE 3000
COPY --from=builder /app .
ENTRYPOINT ["./app"]
