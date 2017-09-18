FROM node:boron
WORKDIR /usr/src/app
# Install app dependencies
COPY package.json .

RUN npm install
# Bundle app source
COPY . .
EXPOSE 8000
CMD [ "npm", "start" ]