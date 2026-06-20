use smart_home_energy;

db.createCollection("sensor_logs");

db.sensor_logs.insertMany([
  {
    device_id: 1,
    device_name: "Living Room AC",
    room_id: 1,
    timestamp: new Date("2026-06-15T08:00:00Z"),
    reading: {
      energy_kwh: 1.20,
      voltage: 230.5,
      current_amp: 5.2,
      temperature_c: 24.5
    },
    status: "ON"
  },
  {
    device_id: 3,
    device_name: "Kitchen Fridge",
    room_id: 2,
    timestamp: new Date("2026-06-15T00:00:00Z"),
    reading: {
      energy_kwh: 0.80,
      voltage: 228.9,
      current_amp: 3.5
    },
    status: "ON"
  },
  {
    device_id: 5,
    device_name: "Bedroom 1 AC",
    room_id: 3,
    timestamp: new Date("2026-06-15T22:00:00Z"),
    reading: {
      energy_kwh: 1.75,
      voltage: 231.0,
      current_amp: 7.6,
      temperature_c: 22.0
    },
    status: "ON"
  },
  {
    device_id: 9,
    device_name: "Geyser - Utility",
    room_id: 5,
    timestamp: new Date("2026-06-15T06:00:00Z"),
    reading: {
      energy_kwh: 2.00,
      voltage: 229.2,
      current_amp: 8.9
    },
    status: "ON"
  },
  {
    device_id: 1,
    device_name: "Living Room AC",
    room_id: 1,
    timestamp: new Date("2026-06-16T08:00:00Z"),
    reading: {
      energy_kwh: 1.10,
      voltage: 230.1,
      current_amp: 4.9,
      temperature_c: 25.0
    },
    status: "ON"
  }
]);

db.sensor_logs.find()

db.sensor_logs.find({ device_id: 1});

db.sensor_logs.find({"reading.energy_kwh": {$gt: 1.5} });

db.sensor_logs.find({ status: "ON"})

db.sensor_logs.updateMany(
  {device_id: 9},
  {$set: { reviewed: true }}
);

db.sensor_logs.deleteOne({device_id: 3})

db.sensor_logs.createIndex({ device_id: 1 });

db.sensor_logs.createIndex({ timestamp: 1 });

db.sensor_logs.getIndexes();

db.sensor_logs.countDocuments ();