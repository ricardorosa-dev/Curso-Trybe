const createBook = (sequelize, Datatypes) => {
  const Book = sequelize.define('Book', {
    title: Datatypes.STRING,
    author: Datatypes.STRING,
    pageQuantity: Datatypes.INTEGER,
  });
  return Book;
};

module.exports = createBook;
