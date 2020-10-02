arr = [2,1,3,5]
dup = []

for (i = 0; i < arr.length; i++){
    if(arr[i] in dup){
        console.log(arr[i])
        return
    }
    else {
        dup.push(arr[i])
    }
}
console.log(-1)
        
