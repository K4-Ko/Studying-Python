# Develop a program that asks for the distance of a trip in Km. Calculate the ticket price, charging R$0.50 per Km for trips up to 200Km and R$0.45 for longer trips.

v = int(input('What is the distance to your final travel destination: '))
if v <= 200:
    print('Since your trip is {}km long, the ticket price will be R$ {}'.format(v, v * 0.5))
else:
    print('Since your trip is {}km long, the ticket price will be R$ {}'.format(v, v * 0.45))
