var pur = document.querySelector(".purchase")
var purchase = document.querySelector(".buy")
console.log(purchase)
purchase.addEventListener("click",function(event){
    console.log("Event")
    //alert("WORK")
    s.style.display = "none"
    st.style.display = "none"
    pur.style.display = "initial";
})

var s = document.querySelector(".sale")
var sale = document.querySelector(".sold")
console.log(sale)
sale.addEventListener("click",function(event){
    console.log("sale")
    pur.style.display = "none"
    st.style.display = "none"
    s.style.display = "initial"
    
})

var st = document.querySelector(".stock")
var stock = document.querySelector(".st")
stock.addEventListener("click",function(event){
    pur.style.display = "none"
    s.style.display = "none"
    st.style.display = "initial"
})

function searchbyDate() {
    alert("function")
    var startDateArr = [];
    var endDateArr = [];
    var myTab = document.getElementById('tableData');
    let InputStartDate = document.getElementById('date_input').value;
    console.log(InputStartDate)
    let InputEndDate = document.getElementById('date_input2').value;
    console.log(InputEndDate)

    for(i = 1; i < myTab.rows.length; i++) {
        var objCells = myTab.rows.item(i).cells;
        var t1 = new Date(objCells.item(3).innerHTML)
        startDateArr.push(t1);
        var t2 = new Date(objCells.item(4).innerHTML)
        endDateArr.push(t2);
    }
    var startDate = new Date(InputStartDate);
    var endDate = new Date(InputEndDate);
    startDate.setHours(0, 0, 0, 0);
    endDate.setHours(0, 0, 0, 0);
    let myTable = document.getElementById('tableData');
    let tr = myTable.getElementsByTagName('tr');
    if(+startDate > +endDate) {
        alert("Select Valid Date. Now please Refresh this page to continue to run code.");
    } else {
        for(var j = 0; j < endDateArr.length; j++) {
            var temp1 = new Date(startDateArr[j]);
            var temp2 = new Date(endDateArr[j]);
            if(startDate && !InputEndDate) {
                if(+startDate <= +temp1 || +startDate === +temp1) {
                    tr[j + 1].style.display = "";
                } else {
                    tr[j + 1].style.display = "none";
                }
            } else if(!InputStartDate && endDate) {
                if(+endDate >= +temp2 || +endDate === +temp2) {
                    tr[j + 1].style.display = "";
                } else {
                    tr[j + 1].style.display = "none";
                }
            } else if(startDate && endDate) {
                if((+startDate <= +temp1 || +startDate === +temp1) && (+endDate >= +temp2 || +endDate === +temp2)) {
                    tr[j + 1].style.display = "";
                } else {
                    tr[j + 1].style.display = "none";
                }
            }
        }
    }
}