const app = require('express')();
const http = require('http').createServer(app);
const cors = require('cors');
const io = require('socket.io')(http, {
  cors: {
    origin: 'http://localhost:3000', // url aceita pelo cors
    methods: ['GET', 'POST'], // Métodos aceitos pela url
  }
});

app.use(cors()) // Permite recursos restritos na página web serem pedidos a domínio externo

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('Conectado');
  socket.emit('ola', 'Bem vindo fulano, fica mais um cadin, vai ter bolo :)' );
  socket.on('disconnect', () => {
    console.log('Desconectado');
  });
  socket.on('mensagem', (msg) => {
    io.emit('mensagemServer', { mensagem: msg });
  });
  /* Basta usarmos a propriedade 'broadcast' */
  socket.broadcast.emit('mensagemServer', { mensagem: ' Iiiiiirraaaa! Fulano acabou de se conectar :D'});
});

http.listen(3000, () => {
  console.log('Servidor ouvindo na porta 3000');
});
