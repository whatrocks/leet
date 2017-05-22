/*

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

*/

function reverseInt(integer) {
  const max = Math.pow(2, 31) - 1;
  const sign = integer < 0 ? -1 : 1;
  var result = sign * Number.parseInt(integer.toString().split('').reverse().join(''));
  if (result > max || result < -max ) {
    return 0;
  } else {
    return result;
  }
}

console.log(reverseInt(123));
console.log(reverseInt(-123));
console.log(reverseInt(1534236469));
