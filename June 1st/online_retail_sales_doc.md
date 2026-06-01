Retail Capstone Database Project

Database Design :

    Customers – customer information.
    Products – product details and prices.
    Orders – order information.
    Order_Items – products included in each order.
    Payments – payment details.
    Deliveries – delivery information.


Table Relationships :

    One customer can place many orders.
    One order can contain multiple products.
    One product can appear in many orders.
    Each order has a payment record.
    Each order has a delivery record.
    
Primary Keys :

    customers → customer_id
    products → product_id
    orders → order_id
    order_items → item_id
    payments → payment_id
    deliveries → delivery_id

Relationships :

----(Foreign Keys)-----

    orders.customer_id → customers.customer_id
    order_items.order_id → orders.order_id
    order_items.product_id → products.product_id
    payments.order_id → orders.order_id
    deliveries.order_id → orders.order_id


Key Insights from Reports :

    Customers from the same city can be identified and analyzed.
    Electronics products generate significant sales.
    Some customers place multiple orders, showing repeat purchases.
    Revenue can be calculated using successful payments.
    Failed payments and cancelled orders can be tracked.
    Pending deliveries help monitor order fulfillment.
    Revenue reports help identify top customers and product categories.
    Data quality checks help find missing payment or delivery records.

The database helps in managing retail operations and generating useful business reports.

    
