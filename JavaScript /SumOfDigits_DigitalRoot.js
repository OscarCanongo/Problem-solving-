// Digital root is the recursive sum of all the digits in a number.
// Given n, take the sum of the digits of n. If that value has more than one digit, 
// continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

function digital_root(n) {
  if(n < 10)
    return n;
  let sum = 0;
  while(n > 0){
    sum = sum + (n%10);
    n = parseInt(n/10, 10);
  }
  return digital_root(sum);
}
