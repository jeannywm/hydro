#time_plot_draft for SAPA in GCVeg_clean from column 7 get SAPA and plot time [0] v PerCo [10]

def getColumn(GCveg_quad.csv, SAPA):
    results = csv.reader(open(GCveg_quad.csv), delimiter="\t")
    return [result[column] for result in results]
and then you can use it like this

time = getColumn("GCveg_quad.csv",0)
PerCo = getColumn("GCveg_quad.csv",10)

plt.figure("Time/PerCo")
plt.xlabel("Time(days)")
plt.ylabel("Percent Cover(PerCo)")
plt.plot(time,PerCo)
