'''An Italian Takeaway is asking you to write a computer program
 to facilitate the ordering process
 and automatically calculate the total cost of an order.'''
#When a customer orders food,
# they give the lists of codes they would like to order.
# For instance a customer could order the following: S4,P3,P7,X2,D4,C1,W2
#our program should allow the customer to order as many options from the menu as they need.
# For each option, it should lookup the price in the text file provided.
# It should then calculate and output the total cost of the order.

print('**************************************')
print('| ---Italian Takeaway Restaurant--- |')
print('|       Place an order online       |')
print('|  (Print X to when done ordering)  |')
print('|                                   |')
print('**************************************')

order = input("Place your order: ")

file = open("Food.text","r")
while (order != 'Done'):
    for line in file:
        data = line.split(";")
        food_Code = data[0]
        food_Description = data[1]
        food_Price = float(data[2])
        if (order == food_Code):
            print(food_Code + '--' + food_Description + ' $' + str(food_Price))
            
    order = input("Enter another code to continue or type 'Done' to exit: ")
      

file.close()
print('Thanks for placing order with us!!')





     
        


