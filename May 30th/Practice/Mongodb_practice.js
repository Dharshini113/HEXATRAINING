use retail_db

db.createCollection("Customers")

db.customers.insertOne({})

db.customers.insertOne({
  customer_id:1,
  name:"Rahul Sharma",
  city:"Hyderabad",
  phone:"9876543210",
  membership:"Gold"
})

db.customers.insertMany([
  {
    customer_id:2,
    name:"Priya Reddy",
    city:"Bangalore",
    phone:"9876501234",
    membership:"Silver"
  },
  {
    customer_id:3,
    name:"Amit Kumar",
    city:"Mumbai",
    phone:null,
    membership:"Gold"
  },
  {
    customer_id:4,
    name:"Sneha Patel",
    city:"Chennai",
    phone:"9098765432",
    membership:"Bronze"
  }
])

db.customers.find()

db.customers.find({city:"Hyderabad"})

// greater than
db.customers.find({customer_id:{$gt:2}})

// less than equal to 
db.customers.find({customer_id:{$lte:3}})

// less than 
db.customers.find({customer_id:{$lt:3}})

db.customers.find({
  city:{$in:["Hyderabad","Bangalore"]}
})

// (AND)
db.customers.find({
  city:"Hyderabad",
  membership:"Gold"
})

// (OR)
db.customers.find({
  $or:[
    {city:"Hyderabad"},
    {membership:"Silver"}
  ]
})

db.customers.find(
  {},
  {name:1,city:1,_id:0}
)

db.customers.find().sort({customer_id:1})

db.customers.find().sort({customer_id:-1})

db.customers.find().limit(3)
