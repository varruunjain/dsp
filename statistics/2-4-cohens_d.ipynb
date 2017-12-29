{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def CohenEffectSize(group1, group2):\n",
    "    \"\"\"Computes Cohen's effect size for two groups.\n",
    "    \n",
    "    group1: Series or DataFrame\n",
    "    group2: Series or DataFrame\n",
    "    \n",
    "    returns: float if the arguments are Series;\n",
    "             Series if the arguments are DataFrames\n",
    "    \"\"\"\n",
    "    diff = group1.mean() - group2.mean()\n",
    "\n",
    "    var1 = group1.var()\n",
    "    var2 = group2.var()\n",
    "    n1, n2 = len(group1), len(group2)\n",
    "\n",
    "    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)\n",
    "    d = diff / np.sqrt(pooled_var)\n",
    "    return d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nsfg\n",
    "import numpy as np\n",
    "import thinkplot, thinkstats2\n",
    "resp = nsfg.ReadFemResp()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "preg = nsfg.ReadFemPreg()\n",
    "live = preg[preg.outcome == 1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "firsts = live[live.birthord == 1]\n",
    "others = live[live.birthord != 1]\n",
    "\n",
    "first_hist = thinkstats2.Hist(firsts.prglngth, label='first')\n",
    "other_hist = thinkstats2.Hist(others.prglngth, label='other')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.028879044654449883"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CohenEffectSize(firsts.prglngth,others.prglngth)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
