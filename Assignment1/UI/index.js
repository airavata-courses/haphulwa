var express = require("express");
var app = express();
var request = require("request");

const cors = require('cors');
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/', function(req, res) {
 res.sendFile(__dirname + '/home.html');
});
app.post('/java', function(req, res, next) {
	console.log("5");
	var port = process.env.PORT || 8085;
	
 request.get({
  url: "http://localhost:" + port
 }, function(error, response, body) {
  if (!error && response.statusCode == 200) {
	  console.log("3");
	  console.log(response.body);
   res.send(response.body);
  }
 });
});
app.post('/python', function(req, res) {
 request.get({
  url: "http://localhost:5000/"
 }, function(error, response, body) {
  if (!error && response.statusCode == 200) {
   res.send(response.body);
  }
 });
});
app.post('/node', function(req, res) {
 request.get({
  url: "http://localhost:8000/"
 }, function(error, response, body) {
  if (!error && response.statusCode == 200) {
   res.send(response.body);
  }
 });
});
var port = process.env.PORT || 8080;
app.listen(port, '0.0.0.0', function(err) {
  console.log("Started listening on %s", err);
});