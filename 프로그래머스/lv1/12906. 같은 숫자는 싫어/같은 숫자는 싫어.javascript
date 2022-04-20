function solution(arr)
{
    var answer = [];

    var sameCheck = -1;
    for(let i = 0; i < arr.length; i++){        
        if(sameCheck == -1 ){
            sameCheck = arr[i]; 
            answer.push(arr[i]); 
        }
        
        if(sameCheck != arr[i]){ 
            answer.push(arr[i]);
            sameCheck = arr[i];
        }
        
    }
    
    console.log(answer)
    
    
    return answer;
}