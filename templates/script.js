function add_item() {
  var food_name = document.getElementById("food_name").value
  var description = document.getElementById("description").value
  var price_cents = document.getElementById("price_cents").value
  var zipcode = document.getElementById("zipcode").value
  var quantity = document.getElementById("quantity").value
  var seller_name = document.getElementById("seller_name").value
  var email = document.getElementById("email").value
  var keywords = document.getElementById("keywords").value.split("\n")
  var ingredients = document.getElementById("ingredients").value.split("\n")
  var address = document.getElementById("address").value
  

  //TODO: Put in real requst to server
  var http = new XMLHttpRequest()
  http.open("GET", "http://127.0.0.1:5000/"+food_name+"/"+description+"/"+price_cents+"/"+zipcode+"/"+quantity+"/"+seller_name+"/"+email+"/"+keywords+"/"+ingredients+"/"+address, false)
  http.send(null)
}

function add_order() {
var buyers_email = document.getElementById("buyers_email").value
var comments = document.getElementById("comments").value
var quantity = document.getElementById("quantity").value
var http = new XMLHttpRequest()

http.open("GET", "http://127.0.0.1:5000/"+buyers_email+"/"+comments+"/"+quantity, false)
http.send(null)
}

function searchByKeyword(keyword) {
var http = new XMLHttpRequest()
http.open("GET", "10.0.0.3" + "/keyword/"+ keyword)
http.send(null)
return http.responseText
}

function searchByTitle(title) {
var http = new XMLHttpRequest()
http.open("GET","10.0.0.3" + "/title/"+ title)
http.send(null)
return http.responseText
}

function search(key) {
const keyword_matches = searchByKeyword(key)
const title_matches = searchByTitle(key)
keyword_matches.forEach (match => {
  display(match)
});
title_matches.forEach (match => {
  display(match)
});
}

function display(result) {
let list = eval(result)
document.write(list[1])
document.write(list[2])
document.write(list[3])
document.write(list[4])
document.write(list[5])
document.write(list[6])
document.write(list[7])
document.write(list[8])
document.write(list[9])
}