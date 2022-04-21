function solution(s) {
    var answer = '';
    var sList = s.split('')
    
    for(let i = 0; i < sList.length; i++){
        sList[i] = sList[i].charCodeAt(0)
    }
    
    sList.sort(function(a,b){
        if(a>b){
            return -1;
        }
        else if(a<b){
            return 1;            
        }
        else
            return 0;
    })
       
    for(let i = 0; i < sList.length; i++){
        sList[i] = String.fromCharCode(sList[i])
    }    
    
    
    return sList.join('');
}