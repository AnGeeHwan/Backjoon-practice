function solution(s)
{
    var answer = -1;
    var sList = s.split('');
    var answerList = [];
    answerList.push(sList.pop());
    
    while(sList.length != 0){
        var strPop = sList.pop();
        
        if(strPop == answerList[answerList.length-1]){
            answerList.pop();
        }
        else{
            answerList.push(strPop);
        }
        
    }

    return answerList.length == 0 ? 1 : 0;
}