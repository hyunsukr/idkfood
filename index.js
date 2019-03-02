var express = require('express');
var app = express();
const path = require('path');
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function(req, res){
    res.sendFile(path.join(__dirname+'/home.html'));
});

app.get('/food', function(req, res){
    res.sendFile(path.join(__dirname+'/food.html'));
});

app.get('/food/:type', function(req, res){
   res.send('The id you specified is ' + req.params.type);
});

app.get('/food/:type/:flavor', function(req, res){
    res.send('The id you specified is' + req.params.type + ' ' + req.params.flavor);
});

app.get('/food/:type/:flavor/:time', function(req, res){
    res.send('The id you specified is ' + req.params.type + ' ' + req.params.flavor+ ' ' + req.params.time);
});

app.get("/insertfood", function(req, res) {
    res.send("this page shit");
});

app.listen(3000);