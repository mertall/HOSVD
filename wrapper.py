#Take picture when IR Sensor threshold is reached
While pi is on:
    distance = irsensor()
    threshold = 40 #units TBD
    if distance <= threshold:
        picture=capture()
        boolean_value=Facial_rec()
        #if boolean_value == True:
            #unlockdoor()
            #reademotions()
        #else:
            #warningmessage()
    else:
        continue 




