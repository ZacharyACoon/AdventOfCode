import sys
from scipy.stats import gstd, tmean, tstd, shapiro
from scipy.stats.mstats import gmean
from math import log, exp

record = []

if len(sys.argv) > 1:
    text = open(sys.argv[1])
else:
    text = sys.stdin

for l in text.readlines():
    row = l.split()
    try:
        part1Time = int(row[2])
        part2Time = int(row[5])
        record.append([part1Time, part2Time])
    except Exception:
        continue

scores = []
logscores = []
for row in record:
    for i in row:
        scores.append(float(i))
        logscores.append(log(float(i)))

gmean = gmean(scores)
gstd = gstd(scores)
logmean = tmean(logscores)
logstd = tstd(logscores)
logshapiro = shapiro(logscores)
lower = exp(logmean - 2 * logstd)
upper = exp(logmean + 2 * logstd)

print("\
Score:\n\
  Geometric mean: {:.6g}\n\
  Geometric standard deviation: {:.6g}\n\
  Test of lognormality (Shapiro-Wilk): {:.6g} (p = {:.6g})\n\
  Prediction interval (95%): {:.6g} - {:.6g} (lognormal dist.)\
".format(round(gmean), gstd, logshapiro[0], logshapiro[1], round(lower), round(upper))
)
