import brfss

df = brfss.ReadBrfss(nrows=None)
df = df.dropna(subset=['htm3', 'wtkg2'])
heights, weights = df.htm3, df.wtkg2
log_weights = np.log10(weights)

# Solution

inter, slope = thinkstats2.LeastSquares(heights, log_weights)
inter, slope

# Solution

thinkplot.Scatter(heights, log_weights, alpha=0.01, s=5)
fxs, fys = thinkstats2.FitLine(heights, inter, slope)
thinkplot.Plot(fxs, fys, color='red')
thinkplot.Config(xlabel='Height (cm)', ylabel='log10 weight (kg)', legend=False)

# Solution

thinkplot.Scatter(heights, weights, alpha=0.01, s=5)
fxs, fys = thinkstats2.FitLine(heights, inter, slope)
thinkplot.Plot(fxs, 10**fys, color='red')
thinkplot.Config(xlabel='Height (cm)', ylabel='Weight (kg)', legend=False)

# Solution

# The lines are flat over most of the range,
# indicating that the relationship is linear.

# The lines are mostly parallel, indicating
# that the variance of the residuals is the
# same over the range.

res = thinkstats2.Residuals(heights, log_weights, inter, slope)
df['residual'] = res

bins = np.arange(130, 210, 5)
indices = np.digitize(df.htm3, bins)
groups = df.groupby(indices)

means = [group.htm3.mean() for i, group in groups][1:-1]
cdfs = [thinkstats2.Cdf(group.residual) for i, group in groups][1:-1]

thinkplot.PrePlot(3)
for percent in [75, 50, 25]:
    ys = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(means, ys, label=label)

thinkplot.Config(xlabel='height (cm)', ylabel='residual weight (kg)', legend=False)

# Solution

rho = thinkstats2.Corr(heights, log_weights)
rho

# Solution

r2 = thinkstats2.CoefDetermination(log_weights, res)
r2

# Solution

rho**2 - r2

# Solution

std_ys = thinkstats2.Std(log_weights)
std_ys

# Solution

std_res = thinkstats2.Std(res)
std_res

# Solution

1 - std_res / std_ys

# Solution

t = []
for _ in range(100):
    sample = thinkstats2.ResampleRows(df)
    estimates = thinkstats2.LeastSquares(sample.htm3, np.log10(sample.wtkg2))
    t.append(estimates)

inters, slopes = zip(*t)

# Solution

cdf = thinkstats2.Cdf(slopes)
thinkplot.Cdf(cdf)

# Solution

pvalue = cdf[0]
pvalue

# Solution

ci = cdf.Percentile(5), cdf.Percentile(95)
ci

# Solution

mean = thinkstats2.Mean(slopes)
mean

# Solution

stderr = thinkstats2.Std(slopes)
stderr

# Solution

estimates_unweighted = [thinkstats2.ResampleRows(df).htm3.mean() for _ in range(100)]
Summarize(estimates_unweighted)

# Solution

# The estimated mean height is almost 2 cm taller
# if we take into account the sampling weights,
# and this difference is much bigger than the sampling error.

estimates_weighted = [ResampleRowsWeighted(df, 'finalwt').htm3.mean() for _ in range(100)]
Summarize(estimates_weighted)