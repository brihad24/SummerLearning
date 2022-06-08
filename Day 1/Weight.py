weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit == 'K' or unit == 'k':
    conv_weight = 2.20 * weight
    print("Weight in lbs: " + str(conv_weight))

if unit == 'L' or unit == 'l':
    conv_weight = 0.45 * weight
    print("Weight in kg: " + str(conv_weight))