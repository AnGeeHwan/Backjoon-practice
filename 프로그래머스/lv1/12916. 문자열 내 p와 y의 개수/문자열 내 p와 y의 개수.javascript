function solution(s){
    var answer = true;
    var sList = s.toLowerCase().split('')
    var pCnt = 0
    var yCnt = 0
    for(let i = 0; i < sList.length; i++){
        if(sList[i] == "p"){
            pCnt+=1;
        }
        else if(sList[i] ==  "y"){
            yCnt+=1;
        }
    }
    pCnt == yCnt ? answer = true : answer = false;
    
    return answer;
}