# Stage 1: Build app
FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

# Stage 2: Serve app
FROM node:18-alpine

WORKDIR /app

# Cài serve để chạy build
RUN npm install -g serve

# Copy build từ stage 1
COPY --from=build /app/build ./build

EXPOSE 3000

CMD ["serve", "-s", "build", "-l", "3000"]