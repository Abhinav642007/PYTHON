
print("-----------Welcome to the Dhaba!------------")
dhaba_Menu=['aloo dum','paneer chilli ','chole bhature','dal makhani','chicken biryani']
dhaba_rates=[100,150,120,130,200]

print('what would you like to order?')
print('Here is the menu:')
print('1. aloo dum : ',dhaba_rates[0])
print('2. paneer chilli : ',dhaba_rates[1])
print('3. chole bhature : ',dhaba_rates[2])
print('4. dal makhani   : ',dhaba_rates[3])
print('5. chicken biryani : ',dhaba_rates[4])
order_a_quantity=int(input('for a enter the quantity of your order:'))


order_a=int(input('for a enter the number of your order:'))
if order_a==1:
    print('you have ordered aloo dum')
    print('your bill is:',order_a_quantity*dhaba_rates[0])
elif order_a==2:
    print('you have ordered paneer chilli ')
    print('your bill is:',order_a_quantity*dhaba_rates[1])
elif order_a==3:
    print('you have ordered chole bhature')
    print('your bill is:',order_a_quantity*dhaba_rates[2])
elif order_a==4:
    print('you have ordered dal makhani')
    print('your bill is:',order_a_quantity*dhaba_rates[3])
elif order_a==5:
    print('you have ordered chicken biryani')
    print('your bill is:',order_a_quantity*dhaba_rates[4])
else:
    print('invalid order')

order_b=int(input('for b enter the number of your order:'))
order_b_quantity=int(input(' for b enter the quantity of your order:'))
if order_b==1:
    print('you have ordered aloo dum')
    print('your bill is:',order_b_quantity*dhaba_rates[0])
elif order_b==2:
    print('you have ordered paneer chilli ')
    print('your bill is:',order_b_quantity*dhaba_rates[1])
elif order_b==3:
    print('you have ordered chole bhature')
    print('your bill is:',order_b_quantity*dhaba_rates[2])
elif order_b==4:
    print('you have ordered dal makhani')
    print('your bill is:',order_b_quantity*dhaba_rates[3])
elif order_b==5:
    print('you have ordered chicken biryani')
    print('your bill is:',order_b_quantity*dhaba_rates[4])
else:
    print('invalid order')



    
    

total_bill=(order_a_quantity*dhaba_rates[order_a-1])+(order_b_quantity*dhaba_rates[order_b-1])
print('your total bill is:',total_bill)
print('After applying 10% discount, your bill is:',total_bill*0.9)
print('-----------Please pay the bill at the counter!------------')
print('-----------Thank you for visiting the Dhaba!------------')
print('-----------Have a nice day!------------')    
print('-----------Please visit again!------------')


