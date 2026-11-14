#Commercial Metal Forging and Heat-Treating Plant
min_temp = 60.0
max_temp = 950.0
ideal_temp = 400.0
#input current temperature
current_temp=float(input("Enter current temperature : "))
while True:
    if(current_temp>100 and current_temp<900):
        print("No problem")
        break
    elif(current_temp>60 and current_temp<100):
        print("Temperture is slightly low increase a little")
        break
    elif(current_temp>900 and current_temp<950):
        print("Temperture is slightly high decrease a little")
        break
    elif(current_temp<60):
        print("temperature is too low ... activating heating system 🚨🚨🚨")
        while current_temp<100:
            current_temp=current_temp+5
            print("current temperature ...",current_temp)
        break
    elif(current_temp>950):
        print("temperature is too high ... activating cooling system 🚨🚨🚨")
        while current_temp>900:
            current_temp=current_temp-5
            print("current temperature ...",current_temp)
        
        break
    else:
        print("invalid input")
        break
