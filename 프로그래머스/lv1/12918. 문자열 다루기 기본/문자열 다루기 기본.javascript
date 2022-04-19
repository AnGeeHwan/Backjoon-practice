function solution(s) {
    var answer = true;
        
    var checkList = []
    
    
    for(let i = 0; i < s.length; i++){
        if(!isNaN(Number(s[i]))){
            checkList.push("true")
        }
        else{
            checkList.push("false")
        }
    }
    
    checkList.filter(element => "false" === element).length > 0 ? answer = false : answer = true
    
    if(answer == true){
        s.length == 4 || s.lengh == 6 ? answer = true : answer= false;
    }
    
    return answer;
}