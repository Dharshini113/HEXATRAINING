use expense_monitoring

db.createCollection("receipts")

db.receipts.insertMany([
    {
        receipt_id: "RCPT00001",
        user_id: 1,
        expense_id: 401,
        store_name: "Dominos",
        category: "Food",
        purchase_date: "2026-01-05",
        total_amount: 250,
        notes: "Lunch order",
        items: [
            { item_name: "Pizza", quantity: 1, price: 200 },
            { item_name: "Coke", quantity: 1, price: 50 }
        ]
    },
    {
        receipt_id: "RCPT00002",
        user_id: 3,
        expense_id: 412,
        store_name: "TNEB",
        category: "Utilities",
        purchase_date: "2026-02-12",
        total_amount: 250,
        notes: "Electricity bill payment",
        items: [
            { item_name: "Electricity Bill", quantity: 1, price: 250 }
        ]
    },
    {
        receipt_id: "RCPT00003",
        user_id: 2,
        expense_id: 413,
        store_name: "Big Bazaar",
        category: "Groceries",
        purchase_date: "2026-02-15",
        total_amount: 850,
        notes: "Monthly grocery shopping",
        items: [
            { item_name: "Rice", quantity: 2, price: 500 },
            { item_name: "Milk", quantity: 5, price: 250 },
            { item_name: "Bread", quantity: 2, price: 100 }
        ]
    },
    {
        receipt_id: "RCPT00004",
        user_id: 1,
        expense_id: 414,
        store_name: "Apollo Pharmacy",
        category: "Healthcare",
        purchase_date: "2026-02-20",
        total_amount: 650,
        notes: "Medicines purchase",
        items: [
            { item_name: "Paracetamol", quantity: 2, price: 200 },
            { item_name: "Vitamin Tablets", quantity: 1, price: 450 }
        ]
    }
]);

db.receipts.find()

db.receipts.find({ user_id: 3});

db.receipts.updateOne(
{receipt_id: "RCPT00003"},
{$set:{total_amount: 900}}
)

db.receipts.deleteOne({receipt_id: "RCPT00004"})