i = str('Y')
while i == 'Y':
     price = float(input('Enter the product price: '))
     discount = int(input('Enter the product discount: '))
     discount_amount = price * (discount / 100)
     sale_price = price - discount_amount

     print(f'From ${price} to only ${sale_price:.1f}!!')
     i = input('Do you want to continue? [Y/N] \n'
               ': ')
     if i == 'N':
         print('Thank you for your time!')
     else:
         continue
