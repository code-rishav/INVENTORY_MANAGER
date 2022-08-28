class Modal{
    constructor(open,close){
        this.open = open;
        this.close = close;
        this.show = document.querySelector(".text")
    }
    open_m(){
        this.show.style.display = "initial";
    }
    close_m(){
        this.show.style.display = "none";
    }
} 

var open = document.querySelector(".js-open-modal")
console.log(open)
if(open){
    console.log("OPENED")
}

var close = document.querySelector(".close")
const modal = new Modal(open,close)

if(open){
    open.addEventListener('click',function(event){
        modal.open_m();
    })
}
if(close){
    close.addEventListener('click',function(event){
        modal.close_m()
    })
}

const h1 = document.querySelector('h1')
const letters = h1.innerText.split('')
console.log(letters)
let html = ""
letters.forEach(letter =>{
    html = html + `<span class='letter js-letter'>${letter}</span>`

})
h1.innerHTML = html
let jsselector = document.querySelectorAll(".js-letter")
jsselector.forEach(node =>{
    node.addEventListener('mouseover',function(event){
        this.classList.add("active")
    })
    node.addEventListener('mouseout',function(event){
        this.classList.remove("active")
    })
    
})



