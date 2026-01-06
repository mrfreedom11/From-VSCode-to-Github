const characters = [
  "The Wally Watchers",
  "Wilma",
  "Fritz",
  "Wizard Whitebeard",
  "Odlaw",
  "Waldo",
  "Woof"
];

if (characters.includes('Waldo')) {
  let x = characters.indexOf('Waldo');
  console.log(`Found Waldo at index ${x}!`);
} else {
  console.log('Not Found');
}
