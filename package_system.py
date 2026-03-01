# Request for the maximum number of objects

max_items = 0
valid_number = False

while valid_number == False:

    user_input = input("enter the maximum number of objects: ")

    is_number = True

    if user_input == "":
        is_number = False
    else:
        for char in user_input:
            if char < "0" or char > "9":
                is_number = False

    if is_number == True:
        max_items = int(user_input)

        if max_items > 0:
            valid_number = True
        else:
            print("Error: the number must be greater than 0.")
    else:
        print("Error: insert a valid number.")


# ----------------------------
# Variable initialization
# ----------------------------

current_weight = 0
packages_sent = 0
total_weight_sent = 0
total_unused_capacity = 0

max_unused = 0
package_with_max_unused = 0
package_number = 0


# ----------------------------
# Main sequence
# ----------------------------

for i in range(max_items):

    valid_weight = False

    while valid_weight == False:

        weight_input = input("Enter the weight of the object (0 to finish): ")

        is_number = True

        if weight_input == "":
            is_number = False
        else:
            for char in weight_input:
                if char < "0" or char > "9":
                    is_number = False

        if is_number == True:

            weight = int(weight_input)

            if weight == 0:
                valid_weight = True

            elif weight >= 1 and weight <= 10:
                valid_weight = True

            else:
                print("Error: The weight must be between 1 and 10 kg.")

        else:
            print("Error: insert a valid number.")


    if weight == 0:
        break


    # ----------------------------
    # 20 kg exceedance check
    # ----------------------------

    if current_weight + weight > 20:

        packages_sent = packages_sent + 1
        package_number = package_number + 1

        unused = 20 - current_weight
        total_unused_capacity = total_unused_capacity + unused

        if unused > max_unused:
            max_unused = unused
            package_with_max_unused = package_number

        total_weight_sent = total_weight_sent + current_weight

        current_weight = weight

    else:
        current_weight = current_weight + weight


# ----------------------------
# Last package shipping
# ----------------------------

if current_weight > 0:

    packages_sent = packages_sent + 1
    package_number = package_number + 1

    unused = 20 - current_weight
    total_unused_capacity = total_unused_capacity + unused

    if unused > max_unused:
        max_unused = unused
        package_with_max_unused = package_number

    total_weight_sent = total_weight_sent + current_weight


# ----------------------------
# Final results
# ----------------------------

print("\n--- FINAL RESULTS ---")
print("Number of sent packages:", packages_sent)
print("Total weight sent:", total_weight_sent, "kg")
print("Total unused capacity:", total_unused_capacity, "kg")

if packages_sent > 0:
    print("The package with the most unused capacity is the number",
          package_with_max_unused,
          "with", max_unused, "unused kg.")