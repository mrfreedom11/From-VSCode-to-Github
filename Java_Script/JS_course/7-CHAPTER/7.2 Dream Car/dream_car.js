
const car = {};

car.model = "Honda";
car.year = 2024;
car.color = "white";
car.used = true; 

let condition = car.used ? "used" : "new";

console.log(`I'm looking for a ${car.color} ${car.year} ${car.model} that is ${condition}.`);
