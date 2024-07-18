print("Welcome to the tip calculator!")

total_bill = float(input('What was the total bill? $'))
tip_percentage = float(input('How much tip would you like to give? 10, 12 or 15? ')) / 100 
total_splitting = int(input('How many people to split the bill? '))

amount_to_split = (total_bill + (total_bill * tip_percentage)) / total_splitting
final_amount_formatted = "{:.2f}".format(amount_to_split)
print(f'Each person should pay: ${final_amount_formatted}')
