var path = require('path'),
    request = require('request'),
    express = require('express'),
    session = require('express-session'),
    bodyParser = require('body-parser'),
    passport = require('passport'),
    cors = require('cors'),
    pug = require('pug'),
    mysql = require('mysql');


var app = express();

//View engine setup
app.set('port', (process.env.PORT || 4026));
app.set('view engine', 'pug');


app.use(cors());
app.use(session({ secret: 'anything', resave: true, saveUninitialized: true })); 
app.use(passport.initialize());
app.use(passport.session()); 
app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({extended: true}));
app.locals.site = {
  title: 'Home'
};

app.listen(app.get('port'), function() {
  console.log('Server started: http://localhost:' + app.get('port') + '/');
});

app.post('/search', function(req, res){
  var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'mquiroga',
  password : 'm4rc0Qu1r0g4!',
  database : 'aquiroga'});

  connection.connect();
  connection.query('INSERT INTO javaNode (nombre, usuario, pass) VALUES("'+req.body.name+'", "'+req.body.user+'", "'+req.body.password+'")', function (error, results, fields) {
  if (error) throw error;
  });
  connection.end();
  var html = pug.renderFile('login2.pug', {});
  res.send(html);
});

app.post('/enterlogin', function(req, res){
  var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'mquiroga',
  password : 'm4rc0Qu1r0g4!',
  database : 'aquiroga'});
  
  connection.connect();
  connection.query('SELECT * from javaNode WHERE usuario="'+req.body.usuario+'" AND pass="'+req.body.password+'"', function (error, results, fields) {
  if (error) throw error;
    console.log('The solution is: ', results[0].usuario);
  if (results.length == 0){
      if (error) throw error;
  }else{
    var html = pug.render('h2 Hello '+results[0].nombre, {});

    res.send(html);

    } 
  });
  connection.end();
});


app.get('/', function(req, res){
  var html = pug.renderFile('login2.pug', {});
  res.send(html);
});

app.get('/registro', function(req, res){
  var html = pug.renderFile('registro.pug', {});
  res.send(html);
});



