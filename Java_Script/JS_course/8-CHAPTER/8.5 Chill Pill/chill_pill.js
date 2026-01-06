const quoteList = [
  "Some doors only open from the inside. Breath is a way of accessing that door.",
  "What has to be taught first, is the breath.",
  "Remember the blue sky. It may at times be obscured by clouds, but it is always there.",
  "In the midst of movement and chaos, keep stillness inside of you.",
  "We can't control the sea, but we can learn how to surf the waves.",
  "Feelings come and go like clouds in a windy sky. Conscious breathing is my anchor.",
  "To understand the immeasurable, the mind must be extraordinarily quiet, still.",
  "Peace isn't found by escaping the world, but by returning to yourself.",
  "Even the longest night ends. Behind every darkness, morning is preparing its light.",
  "Your calm mind is the ultimate weapon against your challenges. So relax.",
  "Not every storm is meant to break you—some come to clear the path.",
  "A single deep breath can return you to yourself more than a thousand thoughts can.",
  "Let go of the need to force the moment; even rivers reach the ocean by flowing naturally."
];

const colors = ["#e81416", "#ffa500", "#faeb36", "#79c314", "#487de7", "#4b369d", "#70369d", "#00ffff", "#000000", 'aquamarine', '#40e0d0', '#8a2be2', '#3a3a3a', '#adf7d1', '#98ffea'];

let wrapperDiv = document.getElementById('wrapper');
let quoteText = document.getElementById('quote-text');
let quoteButton = document.getElementById('quote-button');

quoteButton.addEventListener("click", function() {
    let randomIndex = Math.floor(Math.random() * quoteList.length);
    let randomQuote = quoteList[randomIndex];
    quoteText.innerText = randomQuote;
    wrapperDiv.style.backgroundColor = colors[randomIndex];
});
