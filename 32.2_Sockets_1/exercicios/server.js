const net = require('net');

const server = net.createServer();

let clients = {};
let clientCount = 0;

server.on('connection', connection => {
  let clientname;
  let message = [];
  
  connection.write(`Please enter a room name\r\n`);
  connection.setEncoding('utf-8');
  
  connection.on('data', (data) => {
    message.push(data);
    
    if (data === '\r\n') {
      let clientInput = message.join('').replace('\r\n');
      
      if (!clientname) {
        if (clients[clientInput]) {
          connection.write('Name taken. Try another one');
          message = [];
          return;
        }
      } else {
        clientname = clientInput;
        clientCount++;
        clients[clientInput] = connection;
        
        connection.write(`Welcome. There are ${clientCount} users online`);
        message = [];
      }
    } else {
      // 
    }
  });
});

function broadcast(msg) {
  for (let user in clients) {
    if (clients[user] !== connection) {
      clients[user].write(msg);
    }
  }
}

server.on('close', () => {
  console.log('Server disconnected');
});
server.on('error', error => {
  console.log(`Error: ${error}`);
});

server.listen(4000);
