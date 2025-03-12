# Create a tuple filled with the top 20 teams in the Brazilian Football Championship table, in ranking order.  
# Then, display:

b1 =('Flamengo','Palmeiras','São Paulo','Corinthians','Santos','Grêmio','Internacional','Atlético Mineiro','Cruzeiro','Fluminense',)
b2 = ('Botafogo','Vasco da Gama','Bahia','Athletico Paranaense','Fortaleza','Ceará','América Mineiro','Goiás','Chapecoense','Sport Recife')
t = b1 +b2

# a) The top 5 teams.
print('The top 5 is:',b1[0:5])

print('=-='*20)

# b) The last 4 teams.
print('The last four teams are:',b2[:-5:-1])

print('=-='*20)
# c) Teams in alphabetical order.
b = sorted(b1 + b2)
print(b)

print('=-='*20)
# d) The position of the Chapecoense team.
print('Chapecoense is in', t.index('Chapecoense'),'place')

