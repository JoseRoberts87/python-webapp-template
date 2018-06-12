var express = require('express');
var app = express();
var path = require('path');

app.set('port', 3000);

app.use(function(req, res, next) {
    console.log(req.method, req.url);
    next();
});

app.use(express.static(path.join(__dirname, 'public')));
app.use('/node_modules', express.static(path.join(__dirname, 'node_modules')));
// app.use('/app', express.static(path.join(__dirname, 'public/node_modules')));


// app.use('http://localhost:8761/api', routes);

var server = app.listen(app.get('port'), function() {
    var port = server.address().port;
    console.log('port set at ' + port);
});