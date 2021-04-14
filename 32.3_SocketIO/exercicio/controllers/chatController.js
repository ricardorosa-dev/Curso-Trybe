const Router = require('express');
const router = Router();

router.get('/', async (req, res) => {
  // const data = await getJokes();
  const data = { joke: 'Oba' };
  
  return res.status(200).render('chatView', { joke: data.joke });
});

module.exports = router;
