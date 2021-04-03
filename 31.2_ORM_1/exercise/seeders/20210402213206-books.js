'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert('Books', [{
      title: 'the Lord of the Rings',
      author: 'JRR Tolkien',
      pageQuantity: 200,
      createdAt: Sequelize.literal('CURRENT_TIMESTAMP'),
      updatedAt: Sequelize.literal('CURRENT_TIMESTAMP')
    }], {});
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete('Books', null, {});
  }
};
