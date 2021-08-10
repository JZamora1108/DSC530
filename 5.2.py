{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Examples and Exercises from Think Stats, 2nd Edition\n",
                "\n",
                "http://thinkstats2.com\n",
                "\n",
                "Copyright 2016 Allen B. Downey\n",
                "\n",
                "MIT License: https://opensource.org/licenses/MIT\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "`scipy.stats` contains objects that represent analytic distributions"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 31,
            "metadata": {},
            "outputs": [],
            "source": [
                "import scipy.stats"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 32,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "scipy.stats._distn_infrastructure.rv_frozen"
                        ]
                    },
                    "execution_count": 32,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "mu = 178\n",
                "sigma = 7.7\n",
                "dist = scipy.stats.norm(loc=mu, scale=sigma)\n",
                "type(dist)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 33,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "(178.0, 7.7)"
                        ]
                    },
                    "execution_count": 33,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "dist.mean(), dist.std()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 34,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "0.1586552539314574"
                        ]
                    },
                    "execution_count": 34,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "dist.cdf(mu-sigma)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 35,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "(0.48963902786483265, 0.8317337108107857, 0.3420946829459531)"
                        ]
                    },
                    "execution_count": 35,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "# Solution\n",
                "\n",
                "low = dist.cdf(177.8)    # 5'10\"\n",
                "high = dist.cdf(185.4)   # 6'1\"\n",
                "low, high, high-low"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Exercise:** To get a feel for the Pareto distribution, let’s see how different the world would be if the distribution of human height were Pareto. With the parameters xm = 1 m and α = 1.7, we get a distribution with a reasonable minimum, 1 m, and median, 1.5 m.\n",
                "\n",
                "Plot this distribution. What is the mean human height in Pareto world? What fraction of the population is shorter than the mean? If there are 7 billion people in Pareto world, how many do we expect to be taller than 1 km? How tall do we expect the tallest person to be?\n",
                "\n",
                "`scipy.stats.pareto` represents a pareto distribution.  In Pareto world, the distribution of human heights has parameters alpha=1.7 and xmin=1 meter.  So the shortest person is 100 cm and the median is 150."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 36,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "1.5034066538560549"
                        ]
                    },
                    "execution_count": 36,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "alpha = 1.7\n",
                "xmin = 1       # meter\n",
                "dist = scipy.stats.pareto(b=alpha, scale=xmin)\n",
                "dist.median()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 37,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "2.428571428571429"
                        ]
                    },
                    "execution_count": 37,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "# Solution\n",
                "\n",
                "dist.mean()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 38,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "0.778739697565288"
                        ]
                    },
                    "execution_count": 38,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "# Solution\n",
                "\n",
                "\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 39,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "(55602.976430479954, 55602.97643069972)"
                        ]
                    },
                    "execution_count": 39,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "# Solution\n",
                "\n",
                "(1 - dist.cdf(1000)) * 7e9, dist.sf(1000) * 7e9"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 40,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "1.0525455861201714"
                        ]
                    },
                    "execution_count": 40,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "# Solution\n",
                "\n",
                "# One out of 7 billion prediction\n",
                "\n",
                "dist.sf(600000) * 7e9            "
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 41,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "618349.6106759505"
                        ]
                    },
                    "execution_count": 41,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "dist.ppf(1 - 1/7e9)"
    ]
},
{
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "**Exercise:** The Weibull distribution is a generalization of the exponential distribution that comes up in failure analysis (see http://wikipedia.org/wiki/Weibull_distribution). Its CDF is\n",
        "\n",
        "$\\mathrm{CDF}(x) = 1 − \\exp[−(x / λ)^k]$ \n",
        "\n",
        "Can you find a transformation that makes a Weibull distribution look like a straight line? What do the slope and intercept of the line indicate?\n",
        "\n",
        "Use `random.weibullvariate` to generate a sample from a Weibull distribution and use it to test your transformation.\n",
        "\n",
        "Generate a sample from a Weibull distribution and plot it using a transform that makes a Weibull distribution look like a straight line."
    ]
},
{
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "If you are stuck, you can get a hint from `thinkplot.Cdf`, which provides a transform that makes the CDF of a Weibull distribution look like a straight line.  Here's an example that shows how it's used."
    ]
},
{
    "cell_type": "code",
    "execution_count": 42,
    "metadata": {},
    "outputs": [
        {
            "data": {
                "image/png": "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\n",
                "text/plain": [
                    "<Figure size 432x288 with 1 Axes>"
                ]
            },
            "metadata": {
                "needs_background": "light"
            },
            "output_type": "display_data"
        }
    ],
    "source": [
        "sample = [random.weibullvariate(2, 1) for _ in range(1000)]\n",
        "cdf = thinkstats2.Cdf(sample)\n",
        "thinkplot.Cdf(cdf, transform='weibull')\n",
        "thinkplot.Config(xlabel='Weibull variate', ylabel='CCDF')"
    ]
},
{