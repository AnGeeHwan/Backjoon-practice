function isPrime(num) {
    const sqrtNum = parseInt(Math.sqrt(num))
    for (let i = 2; i <= sqrtNum; i++) {
      if (num % i === 0) return false;
    }
    return true;
}

function solution(n) {
    var answer = 0;
    
    for (var i = 2; i <= n; i++) {
      if (isPrime(i)) answer += 1;
    }
    
    return answer;
}