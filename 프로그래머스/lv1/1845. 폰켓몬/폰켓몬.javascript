function solution(nums) {
    var answer = 0;
    
    // 배열 중복 제거
    // 중복 제거한 배열의 길이와 nums의 길이 비교
    // 골라야하는 폰켓몬 수 = nums길이/2
    // 중복 제거한 배열의 길이가 골라야하는 폰켓몬의 수보다 작을 경우  = 중복 제거한 배열의 길이
    // 클 경우 = 골라야하는 폰켓몬의 수 
    
    var filterNums = [];
    
    for(let i = 0; i < nums.length; i++){
        if(!filterNums.includes(nums[i])){
            filterNums.push(nums[i])
        }
    }
    console.log(filterNums.length)
    
    var choiceCnt = nums.length/2;
    
    filterNums.length < choiceCnt ? answer = filterNums.length : answer = choiceCnt;
    
    return answer;
}