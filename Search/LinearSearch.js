

function Search(arr, target){
    for(let i=0; i<arr.length; i++){
     if(arr[i]==target){
       return i;
     }
    }
    return "not found"
 
 }
 
 console.log(linearSearch([-89, 7, 6, 0, 12, 76], 77));