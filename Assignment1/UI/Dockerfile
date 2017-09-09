FROM node:boron
WORKDIR /usr/src/app
# Install app dependencies
COPY package.json .

RUN npm install
# Bundle app source
COPY . .
EXPOSE 8050
CMD [ "npm", "start" ]