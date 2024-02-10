import sys

print("\nRetro Pay Calculator\n")
print("**Please be advised this calculator is based on 8 hour workdays**\n\n")

ee_name = input("Enter the employee's name: ")
paycycle = input("Is the pay cycle biweekly or monthly?: ")

#########################################################
# determine the pay cycle

# if the pay cycle is monthly:
if paycycle == "monthly":
    rate = input("Enter the monthly wage: $")
# if the pay cycle is biweekly:
elif paycycle == "biweekly":
    rate = input("Enter the hourly rate: $")
else:
    print("\nThis is not an acceptable response.")
    sys.exit()

print("Are wages for the entire paycycle owed?: ")
part_or_full = input("Enter 'yes' or 'no': ")

#########################################################
# if the full paycycle is owed:
if part_or_full == "yes":
    # biweekly:
    if paycycle == "biweekly":
        wages_owed = float(rate) * 80
    # monthly:
    if paycycle == "monthly":
        wages_owed = float(rate)

##########################################################
# if only specific days are owed:
elif part_or_full == "no":
    # biweekly:
    if paycycle == "biweekly":
        hours_owed = input("Enter the number of hours owed: ")
        wages_owed = float(hours_owed) * float(rate)
    # monthly:
    if paycycle == "monthly":
        days_owed = input("Enter the number of days owed: ")
        hours_owed = int(days_owed) * 8
        calculated_hourly_rate = (float(rate)*12)/2080
        wages_owed = float(calculated_hourly_rate) * float(hours_owed)

###########################################################
# invalid response
else:
    print("\nThis is not an acceptable response.")
    sys.exit()

###########################################################
# final output
print(f"The retro wages owed to {ee_name} are: ${"%.2f" % wages_owed} Thank you.")