def massachusetts_state():  # assume 6% sales tax
    wic_eligible_food = float(input("How much did your food cost?"))
    total_cost = wic_eligible_food + (wic_eligible_food * .06)
    print("Your total wic_eligible_food cost is:$%.2f" % total_cost)

    clothing = float(input("How much did your cloths cost?"))
    total_cost = clothing + (clothing * .06)
    print("Your total clothing cost is:$%.2f" % total_cost)

    everything_else = float(input("How much did it cost?"))
    total_cost = everything_else + (everything_else * .06)
    print("Your total cost is:$%.2f" % total_cost)


def new_hampshire_state():  # assume 0% sales tax
    wic_eligible_food = float(input("How much did your food cost?"))
    total_cost = wic_eligible_food + (wic_eligible_food * .0)
    print("Your total wic_eligible_food cost is:$%.1f" % total_cost)

    clothing = float(input("How much did your cloths cost?"))
    total_cost = clothing + (clothing * .0)
    print("Your total clothing cost is:$%.1f" % total_cost)

    everything_else = float(input("How much did it cost?"))
    total_cost = everything_else + (everything_else * .0)
    print("Your total cost is:$%.1f" % total_cost)


def maine_state():  # assume 5% sales tax
    wic_eligible_food = float(input("How much did your food cost?"))
    total_cost = wic_eligible_food + (wic_eligible_food * .05)
    print("Your total wic_eligible_food cost is:$%.2f" % total_cost)

    clothing = float(input("How much did your cloths cost?"))
    total_cost = clothing + (clothing * .05)
    print("Your total clothing cost is:$%.2f" % total_cost)

    everything_else = float(input("How much did it cost?"))
    total_cost = everything_else + (everything_else * .05)
    print("Your total cost is:$%.2f" % total_cost)
