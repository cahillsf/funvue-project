db = new Mongo().getDB("sitecontent");
db.createUser({
  user: 'flask-role',
  pwd: 'toor',
  roles: [
    {
      role: 'dbAdmin',
      db: 'sitecontent',
    },
    {
      role: 'readWrite',
      db: 'sitecontent',
    },
  ],
});
db.createCollection('cards');
db.createCollection('users'); //fixme: create an index so handle is unique: https://stackoverflow.com/questions/3298963/how-to-set-a-primary-key-in-mongodb

// var myCards=
// 	[
// 		{
//             '_id': 0,
//             'title':'CardOne',
//             'msg':'testOne',
//             'animation':'fade-up'
//           },
//           {
//             '_id': 1,
//             'title':'CardTwo',
//             'msg':'testTwo',
//             'animation':'fade-up'
//           },
//           {
//             '_id': 2,
//             'title':'CardThree',
//             'msg':'testTwo',
//             'animation':'fade-up'
//           },
//           {
//             '_id': 3,
//             'title':'CardFour',
//             'msg':'testTwo',
//             'animation':'fade-up'
//           },

// 	];

// 	db.cards.insert(myCards);