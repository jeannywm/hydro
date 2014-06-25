#GCVeg_Plot_PerCov
def getColumn(fname, col):
    results = csv.reader(open(fname))
    return [result[col] for result in results]

SPP = getColumn("GCveg_clean.csv",7)
PerCov = getColumn("GCveg_clean.csv",11)

plt.figure("SPP/Percent Cover")
plt.xlabel("SPP(Species)")
plt.ylabel("Percent Cover(PerCov)")
plt.plot(SPP,PerCov)
