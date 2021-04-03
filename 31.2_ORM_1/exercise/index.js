const express = require('express');
const bodyParser = require('body-parser');
const BookController = require('./controllers/BookController');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.use('/book', BookController);

app.use((err, req, res, next) => {
  res.status(500).json({ message: 'Algo deu errado.' });
})

app.listen(PORT, () => console.log(`Example app listening on port ${PORT}!`));
