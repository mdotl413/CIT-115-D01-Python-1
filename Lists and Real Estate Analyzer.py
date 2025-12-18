def getFloatInput(prompt):
    
    # Prompts the user for a float input.
    #  Reprompts if input is not a number.
    # Re-prompts if the input is not greater than zero.
    
    while True:
        try:
            user_input = float(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("Input a number that is greater than 0.")
        except ValueError:
            print("Input a number that is greater than 0.")

def getMedian(num_list):
    
    # Calculates the median of a list of numbers.
    
    count = len(num_list)
    
    # If the list is empty, return 0
    if count == 0:
        return 0.0
    
    # Calculate the middle index using integer division
    mid_index = count // 2

    if count % 2 == 1:
        # If the number of entries is odd, use the middle entry
        return num_list[mid_index]
    else:
        # If the number of entries is even, average the two middle entries
        # The one at mid_index and the one immediately before it
        val1 = num_list[mid_index]
        val2 = num_list[mid_index - 1]
        return (val1 + val2) / 2

def main():
    # List for all user inputted sales values
    sales_list = []
    
    # Input Loop
    while True:
        # prompt for sales price
        price = getFloatInput("Enter property sales value: ")
        sales_list.append(price)

        # Loop so user can enter Y, y, N, or n
        while True:
            continue_input = input("Enter another value Y or N: ").strip().lower()
            if continue_input in ['y', 'n']:
                break
            
            
        if continue_input == 'n':
            break

    # Sort the list from smallest value to largest
    sales_list.sort()
    
    count = len(sales_list)
    
    # Calculate the metrics
    if count > 0:
        min_val = min(sales_list)
        max_val = max(sales_list)
        total_val = sum(sales_list)
        avg_val = total_val / count
        median_val = getMedian(sales_list)
        commission = total_val * 0.03
    else:
        # Handle case with 0 entries just in case
        min_val = max_val = total_val = avg_val = median_val = commission = 0.0

    # Output
    print()
    
    # Output each entry in the sorted list
    for i in range(count):
        
        print(f"Property {i + 1} $ {sales_list[i]:,.2f}")

    # Output displayed as currency with 2 decimal positions
    print(f"Minimum:    $ {min_val:,.2f}")
    print(f"Maximum:    $ {max_val:,.2f}")
    print(f"Total:      $ {total_val:,.2f}")
    print(f"Average:    $ {avg_val:,.2f}")
    print(f"Median:     $ {median_val:,.2f}")
    print(f"Commission: $ {commission:,.2f}")

# run the program
if __name__ == "__main__":
    main()