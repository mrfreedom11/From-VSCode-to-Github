let player = 0; 

let computer = Math.floor(Math.random() * 3);

let choices = ["Rock", "Paper", "Scissors"];
console.log("Player picked:     " + choices[player]);
console.log("Computer picked:   " + choices[computer]);

if (player === computer) {
  console.log("It's a tie!");
} else if (
  (player === 0 && computer === 2) ||
  (player === 1 && computer === 0) ||
  (player === 2 && computer === 1)
) {
  console.log("The player won!");
} else {
  console.log("The computer won!");
}