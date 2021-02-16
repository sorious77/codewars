function grow(x){
  var answer = 1;
  for(var i=0;i<x.length;i++){
    answer *= x[i];
  }
  return answer;
}
