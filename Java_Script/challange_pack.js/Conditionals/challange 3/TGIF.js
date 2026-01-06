let day = 1;

if (day >= 1 && day < 5) {
  console.log("Not Friday, yet!");
} else if (day === 5) {
  console.log("TGIF 🕺");
} else if (day === 6 || day === 7) {
  console.log("Yay, weekends! 🙌");
} else {
  console.log("Wait, what day is it?");
}
