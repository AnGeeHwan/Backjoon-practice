function solution(d, budget) {
    var answer = 0;
    var dSum = 0;
    d.sort(function(a,b){
        return a-b;
    })
    
    console.log(d)
    
    while(dSum < budget){
        if(answer == d.length){
            break;
        }
        if(dSum + d[answer] > budget){
            break;
        }else {
            dSum += d[answer];
            answer++;
        }
    }
    
    console.log(dSum, answer)
    
    return answer;
}