function solution(a, b) {
    var answer = 0;
    
    if(a == b){
        answer = a;
    }
    else{
        var big = a > b ? a : b;
        var small = a < b ? a : b;

        for(let i = small; i < big+1; i++){          
            answer+=i;
        }
    }
    return answer;
}