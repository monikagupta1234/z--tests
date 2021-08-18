import statistices as s
import pandas as p
import plotly.graph_objects as pgo
import plotly.Fiqure_factory as pff

df = p.read_csv("data.csv")
data = df["Math_score"].toList()

mean = s.mean(data)
print("Population Mean " + str(mean))

def randomSetOfSample():
    sampleSet=[]
    for i in range(0,30):
        ran = r.randint(0,len(data)-1)
        sampleSet.append(data[ran])

    SampleMean = s.mean(sampleSet)
    return(SampleMean)

meanOfSample = []
for i in range(0,100):
    mean1 =  randomSetOfSample()
    meanOfSample.append(mean1)

fig = pff.create_distplot([meanOfSample],["data"],show_hist=False)
fig.add_trace(pgo.scatter(x = [mean,mean], y = [0,0.15],mode = "lines"))
fig.show()

standradDeviation1 = s.stdev(data)
print("Standrad Deviation1" + str(standradDeviation1))

standradDeviation2 = s.stdev(data)
print("Standrad Deviation2" + str(standradDeviation2))

standradDeviation3 = s.stdev(data)
print("Standrad Deviation3" + str(standradDeviation3))

sampleMean = p.read_csv("intervention.csv")

data1 = sampleMean ["Math_score"].tolist()

mean1 = s.mean(data1)
print("intervention Mean" + str(mean1))

zscore = (mean-mean) / standradDeviation

print("Z Test results" + str(zscore))
