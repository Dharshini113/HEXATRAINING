use food_delivery_assessment_db

db.restaurants.insertMany([
  {
    restaurant_id: 1,
    name: "Spice Hub",
    city: "Hyderabad",
    cuisine: "Indian",
    rating: 4.5,
    avg_order_value: 450,
    delivery_available: true,
    tags: ["biryani", "north indian", "family"],
    contact: { phone: "9876543210", email: "spicehub@mail.com" }
  },
  {
    restaurant_id: 2,
    name: "Pizza Corner",
    city: "Bangalore",
    cuisine: "Italian",
    rating: 4.2,
    avg_order_value: 600,
    delivery_available: true,
    tags: ["pizza", "fast food", "cheese"],
    contact: { phone: "9876543211", email: "pizza@mail.com" }
  },
  {
    restaurant_id: 3,
    name: "Green Bowl",
    city: "Chennai",
    cuisine: "Healthy",
    rating: 4.7,
    avg_order_value: 350,
    delivery_available: false,
    tags: ["salad", "vegan", "healthy"],
    contact: { phone: null, email: "greenbowl@mail.com" }
  },
  {
    restaurant_id: 4,
    name: "Burger Street",
    city: "Hyderabad",
    cuisine: "Fast Food",
    rating: 3.9,
    avg_order_value: 300,
    delivery_available: true,
    tags: ["burger", "fries", "fast food"],
    contact: { phone: "9876543213", email: null }
  },
  {
    restaurant_id: 5,
    name: "Royal Tandoor",
    city: "Delhi",
    cuisine: "Indian",
    rating: 4.8,
    avg_order_value: 800,
    delivery_available: true,
    tags: ["tandoor", "north indian", "premium"],
    contact: { phone: "9876543214", email: "royal@mail.com" }
  },
  {
    restaurant_id: 6,
    name: "Tea Tales",
    city: "Pune",
    cuisine: "Cafe",
    rating: 4.1,
    avg_order_value: 200,
    delivery_available: false,
    tags: ["tea", "snacks", "cafe"],
    contact: { phone: "9876543215", email: "tea@mail.com" }
  },
  {
    restaurant_id: 7,
    name: "Ocean Grill",
    city: "Mumbai",
    cuisine: "Seafood",
    rating: 4.6,
    avg_order_value: 900,
    delivery_available: true,
    tags: ["fish", "grill", "premium"],
    contact: { phone: "9876543216", email: "ocean@mail.com" }
  },
  {
    restaurant_id: 8,
    name: "Dosa Point",
    city: "Chennai",
    cuisine: "South Indian",
    rating: 4.3,
    avg_order_value: 250,
    delivery_available: true,
    tags: ["dosa", "idli", "breakfast"],
    contact: { phone: null, email: null }
  }
])

// Exercise 1
db.restaurants.find()

// Exercise 2
db.restaurants.find({}, { name: 1, city: 1, cuisine: 1, _id: 0 })

// Exercise 3
db.restaurants.find({ city: "Hyderabad" })

// Exercise 4
db.restaurants.find({ cuisine: "Indian" })

// Exercise 5
db.restaurants.find({ delivery_available: true })

// Exercise 6
db.restaurants.find({ rating: { $gt: 4.5 } })

// Exercise 7
db.restaurants.find({ avg_order_value: { $lt: 400 } })

// Exercise 8
db.restaurants.find({ rating: { $gte: 4.0, $lte: 4.7 } })

// Exercise 9
db.restaurants.find({ avg_order_value: { $gte: 600 } })

// Exercise 10
db.restaurants.find({ city: "Hyderabad", delivery_available: true })

// Exercise 11
db.restaurants.find({
  $or: [
    { city: "Chennai" }, 
    { cuisine: "Indian" }]
})

// Exercise 12
db.restaurants.find({ delivery_available: false })

// Exercise 13
db.restaurants.find({
  city: { $in: ["Hyderabad", "Delhi", "Mumbai"] }
})

// Exercise 14
db.restaurants.find({
  cuisine: { $in: ["Indian", "Italian", "Cafe"] }
})

// Exercise 15
db.restaurants.find({
  city: { $nin: ["Hyderabad", "Bangalore"] }
})

// Exercise 16
db.restaurants.find({name: /^P/})

// Exercise 17
db.restaurants.find({name: /Point/})

// Exercise 18
db.restaurants.find({cuisine: /Food/})

// Exercise 19
db.restaurants.find({ "contact.phone": null })

// Exercise 20
db.restaurants.find({ "contact.email": null })

// Exercise 21
db.restaurants.find({
  $or: [
    { "contact.phone": null },
    { "contact.email": null }
  ]
})

// Exercise 22
db.restaurants.find({tags: "premium"})

// Exercise 23
db.restaurants.find({ tags: "fast food"})

// Exercise 24
db.restaurants.find({
  tags: { $all: ["north indian", "premium"] }
})

// Exercise 25
db.restaurants.find().sort({rating: -1})

// Exercise 26
db.restaurants.find().sort({ rating: -1 }).limit(3)

// Exercise 27
db.restaurants.find().sort({avg_order_value: 1})

// Exercise 28
db.restaurants.find().sort({avg_order_value: -1}).limit(2)

// Exercise 29
db.restaurants.updateOne(
  { name: "Burger Street" },
  { $set: { rating: 4.0 } }
)

// Exercise 30
db.restaurants.updateOne(
  { name: "Tea Tales" },
  { $set: { delivery_available: true } }
)

// Exercise 31
db.restaurants.updateMany(
  {},
  { $set: { active: true } }
)

// Exercise 32
db.restaurants.updateOne(
  { name: "Spice Hub" },
  { $push: { tags: "popular" } }
)

// Exercise 33
db.restaurants.updateMany(
  {},
  { $unset: { active: "" } }
)

// Exercise 34
db.restaurants.deleteOne({ restaurant_id: 6 })

// Exercise 35
db.restaurants.deleteMany({ rating: { $lt: 4.0 } })

// Exercise 36 - 39
db.restaurants.countDocuments()

db.restaurants.countDocuments({ delivery_available: true })

db.restaurants.distinct("city")

db.restaurants.distinct("cuisine")

// Exercise 40
db.restaurants.aggregate([
  { $group: { 
    _id: "$city", 
    total: { $sum: 1 } } }
])

// Exercise 41
db.restaurants.aggregate([
  { $group: { 
    _id: "$cuisine", 
    total: { $sum: 1 } } }
])

// Exercise 42
db.restaurants.aggregate([
  { $group: { 
    _id: "$cuisine", 
    average_rating: { $avg: "$rating" } } }
])

// Exercise 43
db.restaurants.aggregate([
  { $group: {
    _id: "$city", 
    average_order_value: { $avg: "$avg_order_value" } } }
])

// Exercise 44

db.restaurants.aggregate([
  { $group: {
     _id: "$cuisine", 
     average_order_value: { $avg: "$avg_order_value" } } 
    },
  { $sort: { average_order_value: -1 } },
  { $limit: 1 }
])


// Exercise 45
db.restaurants.aggregate([
  { $group: { _id: "$cuisine", total: { $sum: 1 } } },
  { $match: { total: { $gt: 1 } } }
])

