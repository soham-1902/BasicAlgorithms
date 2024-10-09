function selectionShort(arr){

    let n= arr.length;

    for(let i=0; i<n-1; i++){
      let indexMin = i;
      for(let j=i+1; j<n; j++){
        if(arr[j]<arr[indexMin]){
          indexMin =j;
        }
      }
      if(indexMin!== i){
        let temp= arr[indexMin];
        arr[indexMin]= arr[i];
        arr[i] = temp;
      }
    }
  }
  
  let arr = [23, 45, 12, 22, 9, 34, 78, 55, 21, 2];

  selectionShort(arr);
  console.log(arr);
    