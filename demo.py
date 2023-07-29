import matplotlib.pyplot as plt
from datetime import date

print("Today Covid-19 alive number: ")
ALIVE = int(input())
print("Today Covid-19 death number: ")
DEATH = int(input())
print("Today Covid-19 cured number: ")
CURED = int(input())
print("Today Covid-19 quarantine number: ")
QUARANTINE = int(input())
sum = CURED + DEATH + QUARANTINE + ALIVE
curepercentage = (CURED / (sum)) * 100
alivepercentage = (ALIVE / (sum)) * 100
deathpercentage = (DEATH / (sum)) * 100
quarantinepercentage = (QUARANTINE / (sum)) * 100
higheststat = max([CURED, DEATH, CURED, QUARANTINE])

labels = ['Alive', 'Death', 'Cured', 'Quarantine']
numbers = [ALIVE, DEATH, CURED, QUARANTINE]

plt.pie(numbers, labels=labels)
plt.legend()
plt.savefig("pie_chart.png")
plt.show()

filename = str(date.today())

with open(filename, 'w') as file:
    file.write("Today alive number: {}\n".format(ALIVE))
    file.write("Today death number: {}\n".format(DEATH))
    file.write("Today quarantine: {}\n".format(QUARANTINE))
    file.write("Today cured number: {}\n".format(CURED))
    file.write("Alive percentage: {}\n".format(alivepercentage))
    file.write("Cured percentage: {}\n".format(curepercentage))
    file.write("Death percentage: {}\n".format(deathpercentage))
    file.write("Quarantine percentage: {}\n".format(quarantinepercentage))
    file.write("The biggest count: {}\n".format(higheststat))


print("The information is recorded as txt file")