FROM node:alpine

WORKDIR /usr/src/app

COPY user_status_module.js package.json assignment2-csci5409-*.json ./

RUN npm install

EXPOSE 8080

CMD ["node", "user_status_module.js"]