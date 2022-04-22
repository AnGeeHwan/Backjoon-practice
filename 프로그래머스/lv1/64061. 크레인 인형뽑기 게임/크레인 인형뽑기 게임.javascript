function solution(board, moves) {
    var answer = [];
    var newBoard = [];    
    var answerList = [];
    const emptyBox = 0
    
    for(let i = 0; i < board.length; i++){
        var boardArr = [];
        for(let j = 0; j < board[i].length; j++){
            boardArr.push(board[j][i])
        }
        newBoard.push(boardArr)
    }
          
    // 인형을 뽑아 바구니에 담기
    for(let i = 0; i < moves.length; i++){
        for(let j = 0; j < newBoard[moves[i]-1].length; j++){
            if(newBoard[moves[i]-1][j] != 0){
                answerList.push(newBoard[moves[i]-1][j])
                // push 이후 이전 인덱스와 같은지 체크하여 다른 배열로 이동
                if(answerList.length == 1){                    
                }
                else if(answerList[answerList.length-2] == answerList[answerList.length-1]){
                    answer.push(answerList[answerList.length-1])
                    answerList.pop()
                    answerList.pop()
                }
                
                newBoard[moves[i]-1][j] = emptyBox
                break;
            }            
        }
    }    
    console.log(answerList)
     
    console.log(answer)
    
    return answer.length*2;
}