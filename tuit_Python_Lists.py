#creating a list of temperatures
temperatures = [21.2, 22.5, 26.8, 29.8]
#number of samples present in the list
num_samples = len(temperatures)
print(num_samples)



#creating list of stock prices
stock_prices= [145.67, 142.89, 150.23, 138.45, 152.11]

#getting the maximum and minimum of stock prices
stock_samples= len(stock_prices)
max_stock = max(stock_prices)
min_stock = min(stock_prices)
print("The number of stock samples are : ",stock_samples,"\nThe Minimum Stock is :",min_stock,"\nThe maximum Stock is :", max_stock)

#Sum of all the stocks from the list 
sum_of_stock_samples = sum(stock_prices)
print(sum_of_stock_samples)


# Check if any transaction is fraudulent
fraud_flags = [21,22,23,24,25]
has_fraud = any(fraud_flags)
print(f"Fraud detected: {has_fraud}")


#sorting list without harming the original one 
sorted_stock_prices = sorted(stock_prices)
print(sorted_stock_prices)
