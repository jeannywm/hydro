import pandas

data = pandas.read_csv("../clean_data/GCveg_clean.csv", parse_dates=True)
data2 = pandas.read_csv("../clean_data/TSveg_clean.csv", parse_dates=True)


# %matplotlib inline
import matplotlib.pyplot as plt

data['Date'] = pandas.to_datetime(data['Date'])
data2['Date'] = pandas.to_datetime(data2['Date'])


sapa = data[data.SPP == 'SAPA']
sapa_lm = sapa[sapa.Habitat == 'LM']

sapa_lm.groupby('Date').PerCo.mean().plot(label='one')

plt.figure()
mask = data2.SPP == 'SAVI'
mask = mask + (data2.SPP == 'SAPA')
sapa2 = data2[mask]
sapa2.groupby('Date').PerCo.mean().plot(label='two')

plt.legend(loc=0)