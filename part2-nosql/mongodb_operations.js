use fleximart;

// Operation 1: Load Data
// Import JSON into products collection
db.products.insertMany(load("products_catalog.json"));

// Operation 2: Basic Query
// Find Electronics products priced below 50000 and return name, price, stock
db.products.find(
  { category: "Electronics", price: { $lt: 50000 } },
  { _id: 0, name: 1, price: 1, stock: 1 }
);

// Operation 3: Review Analysis
// Find products with average rating >= 4
db.products.aggregate([
  { $unwind: "$reviews" },
  {
    $group: {
      _id: "$name",
      avgRating: { $avg: "$reviews.rating" }
    }
  },
  { $match: { avgRating: { $gte: 4 } } }
]);

// Operation 4: Update Operation
// Add a new review to product ELEC001
db.products.updateOne(
  { product_id: "ELEC001" },
  {
    $push: {
      reviews: {
        user: "U999",
        rating: 4,
        comment: "Good value",
        date: new Date()
      }
    }
  }
);

// Operation 5: Complex Aggregation
// Calculate average price by category
db.products.aggregate([
  {
    $group: {
      _id: "$category",
      avg_price: { $avg: "$price" },
      product_count: { $sum: 1 }
    }
  },
  { $sort: { avg_price: -1 } }
]);
