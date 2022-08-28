const fs = require("fs")
const csv = require('csvtojson')
const {Parser} = require('json2csv')

(async() => {
    const list = await csv().fromFile("cars.csv")
    console.log(list) 
})();