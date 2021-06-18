import numpy as np

no_payments = {
    "Annual": 1,
    "Semiannual": 2,
    "Quarterly": 4,
    "Monthly": 12,
    "Weekly": 52,
    "Daily": 365,
    "Continuously": np.inf
}
ir_per_period = {}
net_value = {}

ir = 0.1

for frequency in no_payments:
    if frequency == "Continuously":
        ir_per_period[frequency] = ""
        net_value[frequency] = np.exp(0.1)
    else:
        ir_per_period[frequency] = ir / no_payments[frequency]
        net_value[frequency] = (1+ir_per_period[frequency]) ** no_payments[frequency]

print("_____________________________________________________________________________")
print("Type          Number of Payments      Interest Rate per Period     Net Value")
print("_____________________________________________________________________________")
for frequency in no_payments:
    print(f"{frequency:22}{no_payments[frequency]:<25}{ir_per_period[frequency]:<20.2}${net_value[frequency]:<20.5f}")
print("_____________________________________________________________________________")