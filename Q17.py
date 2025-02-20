
balance = 0


while True:
    transaction = input("Enter transaction (D/W amount) or press Enter to finish: ")
    
    if not transaction:  
        break
    
    
    parts = transaction.split()
    if len(parts) == 2:
        action, amount = parts[0], int(parts[1])
        
      
        if action == "D":
            balance += amount
        elif action == "W":
            balance -= amount
        else:
            print("Invalid transaction type! Use 'D' for deposit and 'W' for withdrawal.")
    else:
        print("Invalid input format! Please enter in 'D amount' or 'W amount' format.")

print(f"Net amount in bank account: {balance}")
