function calculate(){
    var number = document.querySelector(".get")
    console.log(number)
    var value  = Number(number.value)
    console.log(value)
    var text = document.querySelector("h2")
    text.innerHTML = "your sum is" + (value+100)
    console.log(text)

}
