const express = require('express');
const app = express();
const http = require('http').createServer(app);
const cors = require('cors');
const io = require('socket.io')(http, {
  cors: {
    origin: 'http://localhost:3000', // url aceita pelo cors
    methods: ['GET', 'POST'], // métodos aceitos pela url
  }
});

app.use(cors())

let users = [];

io.on('connection', (socket) => {
  console.log('Usuário conectado');
  users.push(socket.id);
  
  socket.emit('ola', { msg: `Bem vindo ao chat ${socket.id}`, users });
  
  socket.on('disconnect', () => {
    const indexOfUser = users.indexOf(socket.id);
    users.splice(indexOfUser, 1);
    
    console.log('Usuário desconectado');
  });
  
  socket.on('testeVemPraMim', () => {
    // chega pra todo mundo
    // io.emit('msgServer', { msg: 'mensagem pra todos' });
    
    // só pro cliente que mandou
    // socket.emit('msgServer', { msg: 'só pro cliente que mandou' });
    
    // pra todo mundo MENOS pro cliente que mandou
    socket.broadcast.emit('msgServer', { msg: 'pra todo mundo MENOS pro cliente que mandou' });
  })
  
  // socket.on('mensagem', (msg) => {
  //   console.log(`Mensagem de ${socket.id} para o admin: ${msg}`);
  // })
  
  socket.on('mensagem', (msg) => {
    io.emit('mensagemNormal', { mensagem: msg, user: socket.id });
  })
});

const chatController = require('./controllers/chatController');

app.set('view engine', 'ejs');
app.set('views', './views');
app.use(express.static(__dirname + '/views/'));

app.use('/', chatController);

const PORT = 3000;
http.listen(PORT, console.log(`Listening on ${PORT}`));
