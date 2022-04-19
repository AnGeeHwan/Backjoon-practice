function solution(n) {
  var answer = 0;
  var nDivlist = [];
  for(let i = 1; i < n+1; i++){
    if(n % i == 0){
      nDivlist.push(i)
    }
  }
  
  answer = nDivlist.reduce((sum, cur)=> sum + cur, 0)
    
  return answer;
}