In that python code i was created a REST API using a python flask and json. 
to run different operations like Add,delete,edit,get product 
i was created diffrent function in that to access or run that functions use the below commands.   

Command For Create new product or add new product :
 "curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/products"


Command for change the data of product :  
"curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/products/2" #after the products give the id of that product which we want to change discription or data.

Command For  remove or delete product :
"curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/products/2" #after the products give the id of that product which we want to delete.