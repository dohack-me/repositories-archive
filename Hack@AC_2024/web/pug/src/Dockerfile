FROM node:20-alpine3.18
EXPOSE 3000
WORKDIR /app

COPY . /app

RUN npm install

USER node
CMD ["node", "index.js"]
