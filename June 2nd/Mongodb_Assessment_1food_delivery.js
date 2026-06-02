// use food_delivery_capstone_db

//  Creating collections

db.createCollection('customers')

db.createCollection('restaurants')

db.createCollection('orders')

db.createCollection('delivery_partners')

// Insertion of data 

db.customers.insertMany([
{
customer_id: 1,
    name: "Rahul Sharma",
    city: "Hyderabad",
    membership: "Gold",
    phone: "9876543210"
    },
    {
    customer_id: 2,
    name: "Priya Reddy",
    city: "Bangalore",
    membership: "Silver",
    phone: "9876543211"
    },
    {
    customer_id: 3,
    name: "Amit Kumar",
    city: "Mumbai",
    membership: "Gold",
    phone: null
    },
    {
    customer_id: 4,
    name: "Sneha Patel",
    city: "Chennai",
    membership: "Bronze",
    phone: "9876543213"
    },
    {
    customer_id: 5,
    name: "Arjun Verma",
    city: "Delhi",
    membership: "Silver",
    phone: "9876543214"
    }
    ])


db.restaurants.insertMany([
    {
    restaurant_id: 101,
    name: "Spice Hub",
    city: "Hyderabad",
    cuisine: "Indian",
    rating: 4.5
    },
    {
    restaurant_id: 102,
    name: "Pizza Corner",
    city: "Bangalore",
    cuisine: "Italian",
    rating: 4.2
    },
    {
    restaurant_id: 103,
    name: "Green Bowl",
    city: "Chennai",
    cuisine: "Healthy",
    rating: 4.7
    },
    {
    restaurant_id: 104,
    name: "Burger Street",
    city: "Mumbai",
    cuisine: "Fast Food",
    rating: 3.9
    },
    {
    restaurant_id: 105,
    name: "Royal Tandoor",
    city: "Delhi",
    cuisine: "Indian",
    rating: 4.8
    }
    ])


db.delivery_partners.insertMany([
    {
    partner_id: 201,
    partner_name: "FastMove Logistics",
    city: "Hyderabad",
    rating: 4.4
    },
    {
    partner_id: 202,
    partner_name: "QuickShip",
    city: "Bangalore",
    rating: 4.1
    },
    {
    partner_id: 203,
    partner_name: "SpeedKart",
    city: "Mumbai",
    rating: 4.6
    },
    {
    partner_id: 204,
    partner_name: "DoorDash India",
    city: "Delhi",
    rating: 4.0
    }
    ])


db.orders.insertMany([
    {
    order_id: 1001,
    customer_id: 1,
    restaurant_id: 101,
    partner_id: 201,
    items: [
    { item_name: "Biryani", quantity: 2, price: 250 },
    { item_name: "Kebab", quantity: 1, price: 180 }
    ],
    order_amount: 680,
    payment: {
    mode: "UPI",
    status: "Success"
    },
    order_status: "Delivered",
    delivery_time_minutes: 35,
    order_rating: 5
    },
    {
    order_id: 1002,
    customer_id: 2,
    restaurant_id: 102,
    partner_id: 202,
    items: [
    { item_name: "Pizza", quantity: 1, price: 500 },
    { item_name: "Garlic Bread", quantity: 1, price: 150 }
    ],
    order_amount: 650,
    payment: {
    mode: "Card",
    status: "Success"
    },
    order_status: "Delivered",
    delivery_time_minutes: 42,
    order_rating: 4
    },
    {
    order_id: 1003,
    customer_id: 3,
    restaurant_id: 104,
    partner_id: 203,
    items: [
    { item_name: "Burger", quantity: 2, price: 180 },
    { item_name: "Fries", quantity: 1, price: 120 }
    ],
    order_amount: 480,
    payment: {
    mode: "Cash",
    status: "Pending"
    },
    order_status: "Pending",
    delivery_time_minutes: null,
    order_rating: null
    },
    {
    order_id: 1004,
    customer_id: 4,
    restaurant_id: 103,
    partner_id: null,
    items: [
    { item_name: "Salad Bowl", quantity: 1, price: 350 }
    ],
    order_amount: 350,
    payment: {
    mode: "UPI",
    status: "Failed"
    },
    order_status: "Cancelled",
    delivery_time_minutes: null,
    order_rating: null
    },
    {
    order_id: 1005,
    customer_id: 5,
    restaurant_id: 105,
    partner_id: 204,
    items: [
    { item_name: "Tandoori Chicken", quantity: 1, price: 600 },
    { item_name: "Naan", quantity: 2, price: 60 }
    ],
    order_amount: 720,
    payment: {
    mode: "UPI",
    status: "Success"
    },
    order_status: "Delivered",
    delivery_time_minutes: 50,
    order_rating: 5
    },
    {
    order_id: 1006,
    customer_id: 1,
    restaurant_id: 101,
    partner_id: 201,
    items: [
    { item_name: "Paneer Curry", quantity: 1, price: 300 },
    { item_name: "Roti", quantity: 4, price: 25 }
    ],
    order_amount: 400,
    payment: {
    mode: "Card",
    status: "Success"
    },
    order_status: "Delivered",
    delivery_time_minutes: 30,
    order_rating: 4
    }
    ])

// PART 1: Basic MongoDB Queries
// 1
db.customers.find()

// 2
db.restaurants.find()

// 3
db.customers.find({}, { _id:0, name:1, city:1, membership:1 })

// 4
db.customers.find({ city:"Hyderabad" })

// 5
db.customers.find({ membership:"Gold" })

// 6
db.restaurants.find({ rating:{ $gt:4.5 } })

// 7
db.orders.find({ order_amount:{ $gt:500 } })

// 8
db.orders.find({ order_status:"Delivered" })

// 9
db.orders.find({ order_status:"Cancelled" })

// 10
db.customers.find({ phone:null })

// PART 2: Operators
// 11
db.orders.find({ order_amount:{ $gte:400, $lte:700 } })

// 12
db.customers.find({ city:{ $in:["Hyderabad","Delhi","Mumbai"] } })

// 13
db.restaurants.find({ cuisine:{$in:["Indian","Fast Food"]} })

// 14
db.orders.find({ "payment.status":{$ne:"Success"} })

// 15
db.orders.find({ delivery_time_minutes:null })

// 16
db.orders.find({ order_rating:{$gte:4} })

// 17
db.restaurants.find({ city:{ $nin:["Bangalore","Chennai"] } })


// PART 3: Array Queries
// 18
db.orders.find({ "items.item_name":"Biryani"})

// 19
db.orders.find({ "items.item_name":"Pizza"})

// 20
db.orders.find({ "items.quantity":{$gt:1} })

// 21
db.orders.find({ "items.price":{$gt:300} })

// 22
db.orders.find( {}, {_id:0, order_id:1, items:1} )

// PART 4: Sorting and Limit
// 23
db.restaurants.find().sort({ rating:-1 })

// 24
db.restaurants.find().sort({ rating:-1 }).limit(3)

// 25
db.orders.find().sort({ order_amount:-1 })

// 26
db.orders.find().sort({ order_amount:-1 }).limit(2)

// 27
db.delivery_partners.find().sort({ rating:-1 })

// PART 5: Update Operations
// 28
db.customers.updateOne( {customer_id:1}, {$set:{membership:"Platinum"} })

// 29
db.restaurants.updateOne( {restaurant_id:104}, {$set:{rating:4.1} })

// 30
db.orders.updateOne( {order_id:1003}, {$set:{order_status:"Delivered"} })

// 31
db.orders.updateOne( {order_id:1003}, {$set:{delivery_time_minutes:45} })

// 32
db.customers.updateMany( {}, {$set:{active:true} })

// 33
db.customers.updateMany({}, {$unset:{ active:""} })

// 34
db.orders.updateOne(
  {order_id:1006},
  {
    $push:{
      items:{
        item_name:"Curd Rice",
        quantity:1,
        price:120
      }
    }
  }
)

// PART 6: Delete Operations
// 35
db.orders.deleteMany({order_status:"Cancelled"})

// 36
db.restaurants.deleteMany({rating:{ $lt:4.0 }})

// PART 7: Count and Distinct
// 37
db.customers.countDocuments()

// 38
db.orders.countDocuments()

// 39
db.orders.countDocuments({ order_status:"Delivered" })

// 40
db.orders.countDocuments({ "payment.status":"Failed" })

// 41
db.customers.distinct("city")

// 42
db.restaurants.distinct("cuisine")

// 43
db.orders.distinct("payment.mode")  

// PART 8: Aggregation
// 44 Revenue by Payment Mode
db.orders.aggregate([
  {
    $group:{
      _id:"$payment.mode",
      tot_revenue:{ $sum:"$order_amount" }
    }
  }
])

// 45 Revenue by Order Status
db.orders.aggregate([
  {
    $group:{
      _id:"$order_status",
      tot_revenue:{ $sum:"$order_amount" }
    }
  }
])

// 46 Average Delivery Time
db.orders.aggregate([
  { $match:{ order_status:"Delivered" } },
  {
    $group:{
      _id:null,
      avg_delivery_time:{
        $avg:"$delivery_time_minutes"
      }
    }
  }
])

// 47 Orders by Customer
db.orders.aggregate([
  {
    $group:{
      _id:"$customer_id",
      tot_orders:{ $sum:1 },
      tot_amount:{ $sum:"$order_amount" }
    }
  }
])

// 48 Orders by Restaurant
db.orders.aggregate([
  {
    $group:{
      _id:"$restaurant_id",
      tot_orders:{ $sum:1 },
      tot_revenue:{ $sum:"$order_amount" }
    }
  }
])

// 49 Average Rating by Restaurant
db.orders.aggregate([
  {
    $group:{
      _id:"$restaurant_id",
      avg_rating:{ $avg:"$order_rating" }
    }
  }
])

// 50 High Revenue Customers
db.orders.aggregate([
  {
    $group:{
      _id:"$customer_id",
      tot_spending:{ $sum:"$order_amount" }
    }
  },
  {
    $match:{
      tot_spending:{ $gt:700 }
    }
  }
])

// PART 9: Lookup / Join Style Queries
// 51 Orders with Customer Details
db.orders.aggregate([
  {
    $lookup:{
      from:"customers",
      localField:"customer_id",
      foreignField:"customer_id",
      as:"cust_info"
    }
  },
  { $unwind:"$cust_info" },
  {
    $project:{
      _id:0,
      order_id:1,
      customer_name:"$cust_info.name",
      city:"$cust_info.city",
      order_amount:1,
      order_status:1
    }
  }
])

// 52 Orders with Restaurant Details
db.orders.aggregate([
  {
    $lookup:{
      from:"restaurants",
      localField:"restaurant_id",
      foreignField:"restaurant_id",
      as:"restaurant"
    }
  },
  { $unwind:"$restaurant" },
  {
    $project:{
      _id:0,
      order_id:1,
      restaurant_name:"$restaurant.name",
      cuisine:"$restaurant.cuisine",
      order_amount:1
    }
  }
])

// 53 Orders with Delivery Partner Details
db.orders.aggregate([
  {
    $lookup:{
      from:"delivery_partners",
      localField:"partner_id",
      foreignField:"partner_id",
      as:"partner"
    }
  },
  { $unwind:"$partner" },
  {
    $project:{
      _id:0,
      order_id:1,
      partner_name:"$partner.partner_name",
      delivery_time_minutes:1,
      order_status:1
    }
  }
])

// 54 Full Order Report
db.orders.aggregate([
  {
    $lookup:{
      from:"customers",
      localField:"customer_id",
      foreignField:"customer_id",
      as:"cust_info"
    }
  },
  {
    $lookup:{
      from:"restaurants",
      localField:"restaurant_id",
      foreignField:"restaurant_id",
      as:"restaurant"
    }
  },
  {
    $lookup:{
      from:"delivery_partners",
      localField:"partner_id",
      foreignField:"partner_id",
      as:"partner"
    }
  },
  { $unwind:"$cust_info" },
  { $unwind:"$restaurant" },
  {
    $unwind:{
      path:"$partner",
      preserveNullAndEmptyArrays:true
    }
  },
  {
    $project:{
      _id:0,
      order_id:1,
      customer_name:"$cust_info.name",
      restaurant_name:"$restaurant.name",
      cuisine:"$restaurant.cuisine",
      partner_name:"$partner.partner_name",
      order_amount:1,
      payment_mode:"$payment.mode",
      payment_status:"$payment.status",
      order_status:1,
      delivery_time_minutes:1,
      order_rating:1
    }
  }
])