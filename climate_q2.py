import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('climate_data.csv')

years = data['year']
co2 = data['co2']
temp = data['temperature']


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")


plt.show()