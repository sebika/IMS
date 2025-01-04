FROM node:18-alpine

WORKDIR /opt/frontend

COPY src/ src/
COPY public/ public/
COPY package.json package-lock.json index.html vite.config.js .

RUN npm i

EXPOSE 5173

CMD [ "npm", "run", "dev" ]
