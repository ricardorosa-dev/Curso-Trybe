db.superheroes.find({
  $and: [
    {"aspects.height": {$in: [180, 200]}},
    {"publisher": "Marvel Comics"}
  ]
}).pretty()
