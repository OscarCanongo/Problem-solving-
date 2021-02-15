// Given an array of integers, find the one that appears an odd number of times.
// There will always be only one integer that appears an odd number of times.

function findOdd(A) {
  A = A.sort();
  let count = 1;
  for(let i = 0; i < A.length-2; i++){
    if(A[i] == A[i+1]){
      count++;
    }
    else{
      if(count % 2 != 0){
        return A[i];
      }
      count = 1;
    }
  }
  return A[A.length-1];
}