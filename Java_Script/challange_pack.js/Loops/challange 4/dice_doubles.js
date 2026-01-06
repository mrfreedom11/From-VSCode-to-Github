let die1 = Math.floor(Math.random() * 6) + 1;
let die2 = Math.floor(Math.random() * 6) + 1;
let numberOfRolls = 0;

while (die1 !== die2) {
  numberOfRolls++;
  console.log(`Roll ${numberOfRolls}: die1 = ${die1}, die2 = ${die2}`);
  
 
  die1 = Math.floor(Math.random() * 6) + 1;
  die2 = Math.floor(Math.random() * 6) + 1;
}


numberOfRolls++; 
console.log(`Roll ${numberOfRolls}: die1 = ${die1}, die2 = ${die2}`);
console.log(`Double ${die1} rolled after ${numberOfRolls} rolls!`);
