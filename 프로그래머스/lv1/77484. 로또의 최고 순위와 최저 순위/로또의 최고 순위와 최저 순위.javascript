function solution(lottos, win_nums) {
    var answer = [];
    var collect = 0;
    lottos.sort(function(a,b){
        if(a > b){
            return 1;
        }
        else if(a < b){
            return -1;            
        }
        else{
            return 0;
        }
    })
    
    var zeroCnt = lottos.length - lottos.filter(el => el != 0).length;        
    console.log(zeroCnt)    
    zeroCnt = zeroCnt == 6 ? zeroCnt = 5 : zeroCnt;
    
    lottos = lottos.filter(el=>el != 0)
    
    for(let i = 0; i < lottos.length; i++){
        win_nums.includes(lottos[i]) ? collect+=1 : collect;
    }
    
    console.log(collect)
    var rankNum = collect == 0 ? collect : collect-1
    var rank = [ 6, 5, 4, 3, 2, 1 ]
    
    answer.push(rank[rankNum+zeroCnt])
    answer.push(rank[rankNum])
    
    return answer;
}