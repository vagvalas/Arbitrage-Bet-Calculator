import sys


main_choice = 'Y'
while main_choice != 'Q':
    first_odd = float(input("Enter first odd: "))
    second_odd = float(input("Enter second odd: "))

    probabilityA = 1/first_odd
    probabilityB = 1/second_odd
    print("The first odd has a probability of {:.2f}%".format(probabilityA*100))
    print("The second odd has a probability of {:.2f}%".format(probabilityB*100))
    sum_probability = probabilityA + probabilityB
    print("That's a total of {:.2f}%".format(sum_probability*100))
    if sum_probability < 1:
        print("The sum of probabilities is less than 1.")
        print("Do you want to calculate the MIN profit or the individual bets with certain budget?")
        choice = input("Type 'profit' for the former and 'budget' for the latter or 'Q' for exit: ")
        if choice == 'profit':
            profit = float(input("Enter the profit: "))
            min_odd = min(first_odd, second_odd)
            max_odd = max(first_odd, second_odd)
            max_prob = probabilityA if min_odd == first_odd else probabilityB
            min_prob = probabilityB if max_odd == second_odd else probabilityA
            total_bet_amount = profit*sum_probability / (max_prob*min_odd - sum_probability)
            print()
            print(f"The minimum bet amount needed for a profit of {profit} is {total_bet_amount:.2f}.")
            print()
            amount=(total_bet_amount*max_prob)/sum_probability
            amount2=(total_bet_amount*min_prob)/sum_probability
            print(f"You have to bet {amount:.2f} $ on {min_odd}")
            print("resulting in {:.2f} $".format(amount*min_odd),"total payout from",min_odd)
            print()
            print(f"You have to bet {amount2:.2f} $ on {max_odd}")
            print("resulting in {:.2f} $".format(amount2*max_odd),"total payout from",max_odd)

        elif choice == 'budget':
            total_bet_amount = int(input("Give me the whole budget that you have: "))
            min_odd = min(first_odd, second_odd)
            max_odd = max(first_odd, second_odd)
            max_prob = probabilityA if min_odd == first_odd else probabilityB
            min_prob = probabilityB if max_odd == second_odd else probabilityA
            amount=(total_bet_amount*max_prob)/sum_probability
            amount2=(total_bet_amount*min_prob)/sum_probability
            print()
            print(f"You have to bet {amount:.2f} $ on {min_odd}")
            print("resulting in {:.2f} $".format(amount*min_odd),"total payout from",min_odd)
            print()
            print(f"You have to bet {amount2:.2f} $ on {max_odd}")
            print("resulting in {:.2f} $".format(amount2*max_odd),"total payout from",max_odd)
        else:
            sys.exit()
    else:
        print("The sum of probabilities is greater than or equal to 1. so can not be betted")
    main_choice = input("check other odd or 'Q' for exit:")