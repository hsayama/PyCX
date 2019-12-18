from pylab import *
import networkx as nx
from scipy import stats as st

n = 10000
ba = nx.barabasi_albert_graph(n, 5)
Pk = [float(x) / n for x in nx.degree_histogram(ba)]
domain = range(len(Pk))
ccdf = [sum(Pk[k:]) for k in domain]

logkdata = []
logPdata = []
prevP = ccdf[0]
for k in domain:
    P = ccdf[k]
    if P != prevP:
        logkdata.append(log(k))
        logPdata.append(log(P))
        prevP = P

a, b, r, p, err = st.linregress(logkdata, logPdata)
print("Estimated CCDF: P(k >= k') =", exp(b), "* k'^", a)
print('r =', r)
print('p-value =', p)

plot(logkdata, logPdata, 'o')
kmin, kmax = xlim()
plot([kmin, kmax],[a * kmin + b, a * kmax + b]) 
xlabel("$\log \, k'$")
ylabel("$\log \, P(k \geq k')$")
show()
