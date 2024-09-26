TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_choice = int(input("Which tariff? 11 or 31: "))
while tariff_choice != 11 and tariff_choice != 31:
    print("Please choice a valid tariff!")
    tariff_choice = int(input("Which tariff? 11 or 31: "))

daily_use_kwh = float(input("Enter daily use in kwh: "))
billing_days = int(input("Enter number of billing days: "))

if tariff_choice == 11:
    estimated_bill = TARIFF_11 * daily_use_kwh * billing_days
else:
    estimated_bill = TARIFF_31 * daily_use_kwh * billing_days


print(f"Estimated bill: {estimated_bill:.2f}")