function isPalindrome(word) {
  let lowerWord = word.toLowerCase();
  let reversed = lowerWord.split('').reverse().join('');
  
  if (lowerWord === reversed) {
    return true;
  } else {
    return false;
  }
}

console.log(isPalindrome("racecar"));   // true
console.log(isPalindrome("madam"));     // true
console.log(isPalindrome("moonlight")); // false
console.log(isPalindrome("aviary")); //false