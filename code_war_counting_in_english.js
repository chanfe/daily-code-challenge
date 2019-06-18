function numberToEnglish(n) {
    var english = "";
    const thousand = ['thousand','million', 'billion','trillion','quadrillion'];
    // Return the name of the number as a string.
    var eng_arr = []
    var place = 0
    
  
    if(isNaN(n)) throw 'Not a number' 
  //   if(n == 0) return 'zero'
    
    if(n < 0){
      english += 'negative ';
      n = Math.abs(n)
    }
    
    if(n % 1 > 0){
      eng_arr.push(point(parseFloat((n%1).toFixed(5))))
    }
    
    n = Math.floor(n/1)
    
    eng_arr.unshift(belowThousand(n%1000))
    n = Math.floor(n/1000)
    
    while(n > 0){
      var temp = belowThousand(n%1000)
      if (temp != 'zero'){
        eng_arr.unshift(temp +' '+ thousand[place])
      }
      n = Math.floor(n/1000)
      place += 1
    }
    console.log(eng_arr)
  
    if (eng_arr.length > 1 && eng_arr[eng_arr.length - 1] == 'zero'){
      eng_arr = eng_arr.slice(0, -1)
    }
    else if(eng_arr[eng_arr.length - 1].length < 13){
      eng_arr = eng_arr.slice(0, -2).concat(eng_arr.slice(-2).join(' and '))
    }
  
    english += eng_arr.join(' ')
    
    
    return english;
  }
  
  function point(n){
    const ones = ['zero','one','two','three','four', 'five','six','seven','eight','nine'];
    var eng_space = []
    eng_space.push("point")
    var fixed = 4
    while(n != 0){
      n = parseFloat((n*10).toFixed(fixed))
      eng_space.push(ones[Math.floor(n)])
      n = parseFloat((n%1).toFixed(fixed))
      fixed--
    }
    return eng_space.join(' ')
    
  }
  
  function belowThousand(n){
    const ones = ['zero','one','two','three','four', 'five','six','seven','eight','nine'];
    const teens = ['ten','eleven','twelve','thirteen', 'fourteen','fifteen','sixteen', 'seventeen','eighteen','nineteen'];
    const tens = ['','','twenty','thirty','forty','fifty', 'sixty','seventy','eighty','ninety'];
    var eng_dash = []
    var eng_and = []
    var answer = ""
    if(n < 10){
      return ones[n]
    }
    
    if (n < 1000 && n >= 100){
      eng_and.push(ones[Math.floor(n/100)] + ' hundred')
      n%=100
    }
    
    if(n < 100 && n >= 20){
      eng_dash.push(tens[Math.floor(n/10)])
      n %= 10
    }
    else if(n < 20 && n >=10){
      eng_dash.push(teens[n%10])
      n=0
    }
    if(n < 10 && n > 0){
      eng_dash.push(ones[n])
    }
    
    eng_and.push(eng_dash.join('-'))
    
    return eng_and.filter(n => n).join(' and ')
  }