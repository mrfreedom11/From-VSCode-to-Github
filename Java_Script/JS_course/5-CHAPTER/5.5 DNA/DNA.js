const dnaPieces = ["A", "C", "G", "T"];
const myDNA = [];

for (let i = 0; i < 24; i++) {
  // Get three random indices
  const rand1 = Math.floor(Math.random() * dnaPieces.length);
  const rand2 = Math.floor(Math.random() * dnaPieces.length);
  const rand3 = Math.floor(Math.random() * dnaPieces.length);

  // Build a 3-letter string
  const dnaStr = dnaPieces[rand1] + dnaPieces[rand2] + dnaPieces[rand3];

  // Add to myDNA array
  myDNA.append(dnaStr);
}

console.log(myDNA);