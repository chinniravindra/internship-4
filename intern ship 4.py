import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(num_flips):
    heads_count = 0
    tails_count = 0
    
    for _ in range(num_flips):
        result = coin_toss()
        print(result)
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    
    print("\nResults:")
    print(f"Heads: {heads_count} ({(heads_count/num_flips)*100:.2f}%)")
    print(f"Tails: {tails_count} ({(tails_count/num_flips)*100:.2f}%)")

def main():
    while True:
        try:
            flips = int(input("Enter the number of times you want to flip the coin: "))
            if flips <= 0:
                print("Please enter a positive integer.")
                continue
            multiple_tosses(flips)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        restart = input("Do you want to flip again? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
