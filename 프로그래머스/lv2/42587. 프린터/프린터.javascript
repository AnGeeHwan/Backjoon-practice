function solution(priorities, location) {
    var answer = 0;
    var printCnt = 0;
        
    // 루프시마다 max 값체크 하여 제거
    // 아닐경우 shift 후 push로 마지막으로 보냄
    while(priorities.length > 0){            
        var compareValue = priorities.shift();
        
        if(priorities.some((value) =>{
            return value > compareValue;
        })){
            priorities.push(compareValue);            
        } else {
            printCnt+=1;    
            if(location == 0)
                return printCnt;
        }        
        
        if(location == 0) {
            location = priorities.length - 1;
        } else {
            location-=1;
        }
    }
    
    return answer;
}