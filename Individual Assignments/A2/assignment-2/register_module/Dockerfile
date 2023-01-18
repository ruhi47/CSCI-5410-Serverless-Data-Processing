FROM node:alpine

WORKDIR /usr/src/app

COPY register_user.js package.json assignment2-csci5409-*.json ./

RUN npm install

EXPOSE 8080

CMD ["node", "register_user.js"]