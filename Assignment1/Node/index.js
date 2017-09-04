'use strict';

const express = require('express');
const cors = require('cors');
// Constants
const PORT = 8000;
const HOST = '0.0.0.0';

// App
const app = express();

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/', (req, res) => {
  res.send('Hello world from Node.js \n');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);