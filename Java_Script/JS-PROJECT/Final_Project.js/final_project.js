const bells = new Audio("./sounds/bell.wav");
const startBtn = document.querySelector(".btn-start");
const minuteDiv = document.querySelector(".minutes");
const secondDiv = document.querySelector(".seconds");

let myInterval;
let totalSeconds;
let state = true;

const appTimer = () => {
  const sessionAmount = Number.parseInt(minuteDiv.textContent);

  if (state) {
    state = false;
    totalSeconds = sessionAmount * 60;

    myInterval = setInterval(updateSeconds, 1000);
  } else {
    alert("Session has already started.");
  }
};

const updateSeconds = () => {
  totalSeconds--;

  let minutesLeft = Math.floor(totalSeconds / 60);
  let secondsLeft = totalSeconds % 60;

  // seconds format
  secondDiv.textContent = secondsLeft < 10 ? "0" + secondsLeft : secondsLeft;

  // minutes update
  minuteDiv.textContent = minutesLeft;

  // finish
  if (minutesLeft === 0 && secondsLeft === 0) {
    bells.play();
    clearInterval(myInterval);
    state = true; // restart ochish uchun
  }
};

startBtn.addEventListener("click", appTimer);
