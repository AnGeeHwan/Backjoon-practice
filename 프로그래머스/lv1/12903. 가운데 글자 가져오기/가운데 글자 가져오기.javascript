function solution(s) {
    var answer = '';
    var pos = Math.floor(s.length/2)
    s.length % 2 == 0 ? answer = s[pos-1] + s[pos] : answer = s[pos]
    
    return answer;
}