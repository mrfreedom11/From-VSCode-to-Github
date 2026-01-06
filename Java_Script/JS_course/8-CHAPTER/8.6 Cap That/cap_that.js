const memeArray = [
  "https://i.imgur.com/bSi4xLb.png",
  "https://i.imgur.com/6y0G7N0.png",
  "https://i.imgur.com/LXnRao1.png",
  "https://i.imgur.com/Qqoxh1N.png"
];

const captionsArray = [
  "When you realize it's Monday tomorrow...",
  "That moment you forget what you were doing",
  "Me trying to act normal in public",
  "When the Wi-Fi finally works",
  "When you find money in your old jeans",
  "When your pet does something cute",
  "When you finish a series and don't know what to do with your life",
  "When the food delivery arrives",
  "When you ace a test you didn't study for",
  "When your favorite song comes on"
];

let meme = document.getElementById('random-meme');
let caption = document.getElementById('random-caption');
let button = document.getElementById('generator-button');
button.addEventListener('click', function() {
  let randomMemeIndex = Math.floor(Math.random() * memeArray.length);
  let randomCaptionIndex = Math.floor(Math.random() * captionsArray.length);
  meme.src = memeArray[randomMemeIndex];
  caption.innerText = captionsArray[randomCaptionIndex];});