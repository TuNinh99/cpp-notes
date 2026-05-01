# Base image
FROM node:20-alpine

# Tạo thư mục app
WORKDIR /app

# Copy package trước để cache
COPY package.json package-lock.json* ./

RUN npm install

# Copy toàn bộ source
COPY . .

# Expose port
EXPOSE 3000

# Run dev server
CMD ["npm", "run", "start", "--", "--host", "0.0.0.0"]
