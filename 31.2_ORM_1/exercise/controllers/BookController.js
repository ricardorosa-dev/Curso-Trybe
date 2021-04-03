const rescue = require('express-rescue');
const { Router } = require('express');
const { Book } = require('../models');

const router = Router();

router.get('/', rescue(async (req, res) => {
  const books = await Book.findAll();
  
  res.status(200).json(books);
}));

router.get('/:id', rescue(async (req, res) => {
  const { id } = req.params;
  const book = await Book.findByPk(id);
  
  res.status(200).json(book);
}));

router.post('/findByName', rescue(async (req, res) => {
  const { title } = req.body;
  const book = await Book.findOne({ where: { title } });
  
  res.status(200).json(book);
}));

router.post('/', rescue(async (req, res) => {
  const { title, author, pageQuantity } = req.body;
  const book = await Book.create({ title, author, pageQuantity });
  
  res.status(201).json(book);
}));

router.put('/:id', rescue(async (req, res) => {
  const { id } = req.params;
  const { title, author, pageQuantity } = req.body;
  
  await Book.update(
    {
      title, 
      author, 
      pageQuantity,
      updatedAt: new Date().toString()
    },
    { where: { id } }
  );
  
  res.status(200).json({});
}))

router.delete('/:id', rescue(async (req, res) => {
  const { id } = req.params;
  await Book.destroy(
    { where: { id } }
  );
  
  res.status(204).end();
}))

module.exports = router;
