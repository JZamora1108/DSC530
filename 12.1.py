"**Exercise:**   The linear model I used in this chapter has the obvious drawback that it is linear, and there is no reason to expect prices to change linearly over time. We can add flexibility to the model by adding a quadratic term, as we did in Section 11.3.\n",
"\n",
"Use a quadratic model to fit the time series of daily prices, and use the model to generate predictions. You will have to write a version of `RunLinearModel` that runs that quadratic model, but after that you should be able to reuse code from the chapter to generate predictions."
]
},
{
    "cell_type": "code",
    "execution_count": null,
    "metadata": {
"tags": []
},
"outputs": [],
"source": [
"# Solution\n",
"\n",
"def RunQuadraticModel(daily):\n",
"    \"\"\"Runs a linear model of prices versus years.\n",
"\n",
"    daily: DataFrame of daily prices\n",
"\n",
"    returns: model, results\n",
"    \"\"\"\n",
"    daily['years2'] = daily.years**2\n",
"    model = smf.ols('ppg ~ years + years2', data=daily)\n",
"    results = model.fit()\n",
"    return model, results"
]
},
{
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
"# Solution\n",
"\n",
"name = 'high'\n",
"daily = dailies[name]\n",
"\n",
"model, results = RunQuadraticModel(daily)\n",
"results.summary()    "
]
},
{
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
"# Solution\n",
"\n",
"PlotFittedValues(model, results, label=name)\n",
"thinkplot.Config(title='Fitted values',\n",
"                 xlabel='Years',\n",
"                 xlim=[-0.1, 3.8],\n",
"                 ylabel='price per gram ($)')"
]
},
{
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
"# Solution\n",
"\n",
"years = np.linspace(0, 5, 101)\n",
"thinkplot.Scatter(daily.years, daily.ppg, alpha=0.1, label=name)\n",
"PlotPredictions(daily, years, func=RunQuadraticModel)\n",
"thinkplot.Config(title='predictions',\n",
"                 xlabel='Years',\n",
"                 xlim=[years[0]-0.1, years[-1]+0.1],\n",
"                 ylabel='Price per gram ($)')"
]
},
{
    "cell_type": "markdown",
    "metadata": {},
    "source": [
"**Exercise:** Write a definition for a class named `SerialCorrelationTest` that extends `HypothesisTest` from Section 9.2. It should take a series and a lag as data, compute the serial correlation of the series with the given lag, and then compute the p-value of the observed correlation.\n",
"\n",
"Use this class to test whether the serial correlation in raw price data is statistically significant. Also test the residuals of the linear model and (if you did the previous exercise), the quadratic model."
]
},
{
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
"# Solution\n",
"\n",
"class SerialCorrelationTest(thinkstats2.HypothesisTest):\n",
"    \"\"\"Tests serial correlations by permutation.\"\"\"\n",
"\n",
"    def TestStatistic(self, data):\n",
"        \"\"\"Computes the test statistic.\n",
"\n",
"        data: tuple of xs and ys\n",
"        \"\"\"\n",
"        series, lag = data\n",
"        test_stat = abs(SerialCorr(series, lag))\n",
"        return test_stat\n",
"\n",
"    def RunModel(self):\n",
"        \"\"\"Run the model of the null hypothesis.\n",
"\n",
"        returns: simulated data\n",
"        \"\"\"\n",
"        series, lag = self.data\n",
"        permutation = series.reindex(np.random.permutation(series.index))\n",
"        return permutation, lag"
]
},
{
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
"# Solution\n",
"\n",
"# test the correlation between consecutive prices\n",
"\n",
"name = 'high'\n",
"daily = dailies[name]\n",
"\n",
"series = daily.ppg\n",
"test = SerialCorrelationTest((series, 1))\n",
"pvalue = test.PValue()\n",
"print(test.actual, pvalue)"
]
},
{
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
"# Solution\n",
"\n",
"# test for serial correlation in residuals of the linear model\n",
"\n",
"_, results = RunLinearModel(daily)\n",
"series = results.resid\n",
"test = SerialCorrelationTest((series, 1))\n",
"pvalue = test.PValue()\n",
"print(test.actual, pvalue)    "
]
},
{
    "cell_type": "code",
    "execution_count": null,
    "metadata": {},
    "outputs": [],
    "source": [
"# Solution\n",
"\n",
"# test for serial correlation in residuals of the quadratic model\n",
"\n",
"_, results = RunQuadraticModel(daily)\n",
"series = results.resid\n",
"test = SerialCorrelationTest((series, 1))\n",
"pvalue = test.PValue()\n",
"print(test.actual, pvalue)"
]
},
{