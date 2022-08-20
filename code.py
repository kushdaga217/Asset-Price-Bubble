import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
from datetime import datetime


#1 Tulip Bubble
df = pd.read_csv("tulip.csv")

ax = plt.gca()

print(df["answer"].mean(), df["answer"].mean() + df["answer"].std())

df.plot(x='date',y='mean',color='green',ax=ax)
df.plot(x='date',y='std',color='blue',ax=ax)
df.plot(x='date',y='answer',color='red',ax=ax)
plt.show()

#2 Japan Real Estate Bubble
df = pd.read_csv("Japan.csv")
ax = plt.gca()
print(df)

df.plot(x='Year',y='mean',color='green',ax=ax)
df.plot(x='Year',y='std',color='blue',ax=ax)
df.plot(x='Year',y='answer',color='red',ax=ax)

plt.show()

#3 US Housing Bubble
style.use("ggplot")
df = pd.read_csv("hso_synopsis_data.csv")
ax = plt.gca()

df["date"] = [datetime.strptime(date, '%d-%m-%Y').date() for date in df["date"]]
df.plot(x='date',y='mean',color='green',ax=ax)
df.plot(x='date',y='std',color='blue',ax=ax)
df.plot(x='date',y='price',color='red',ax=ax)
plt.show()
