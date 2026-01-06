
const luckyNumber = 8;

let guess = Math.floor(Math.random() * 10) + 1;

while (guess !== luckyNumber) {
    guess = Math.floor(Math.random() * 10);
    console.log('Your unlucky guess is: ', guess);

}
console.log('Congratulations! Your lucky number is: ', guess);