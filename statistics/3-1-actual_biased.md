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
    "from __future__ import print_function, division\n",
    "\n",
    "%matplotlib inline\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "import nsfg\n",
    "import first\n",
    "import thinkstats2\n",
    "import thinkplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def BiasPmf(pmf, label):\n",
    "    new_pmf = pmf.Copy(label=label)\n",
    "\n",
    "    for x, p in pmf.Items():\n",
    "        new_pmf.Mult(x, x)\n",
    "        \n",
    "    new_pmf.Normalize()\n",
    "    return new_pmf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEKCAYAAAD9xUlFAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAFyJJREFUeJzt3X+QVeWd5/H3124QdIwjYG0yoNuEEQFdxNnWmKJNdJkY\nUZRYJKXRZGMSy8IaJ0y2TMb8mDjWVrJrlZPJGs0Qyh/JVEbUUok64uj4g1KzGmiyxoyIBo2jrU5A\nNCpjUBq++8e9nrko0NJ9Tx/u7ferqotzz3nuPd8DRX/u8zznR2QmkiQB7FV1AZKkPYehIEkqGAqS\npIKhIEkqGAqSpIKhIEkqGAqSpIKhIEkqGAqSpEJn1QXsrgkTJmRXV1fVZUhSS1m9evVLmXngQO1a\nLhS6urro7e2tugxJaikR8a/vpZ3DR5KkgqEgSSoYCpKkQsvNKUhSoy1bttDX18fmzZurLmWPMGbM\nGCZNmsSoUaMG9X5DQVJL6+vrY7/99qOrq4uIqLqcSmUmGzdupK+vj8mTJw/qMxw+ktTSNm/ezPjx\n40d8IABEBOPHjx9Sr8lQkNTyDIT/MNS/ixEzfHTLw89w/QNP8eaWrVWX0hR7j+rg9GOnMP+YrqpL\nkdRGRkxPoZ0CAeDNLVu5/oGnqi5DUt1Pf/pTIoK1a9fust2PfvQjXnjhhUHvZ8WKFcybN2/Q7x/I\niAmFdgqEt7XjMUmtaunSpfT09LB06dJdthtqKJRtxAwfNbrp6ydUXcKQLPjOXVWXIKnBpk2bePDB\nB7nvvvs45ZRTuPjiiwG45JJL+MlPfsJee+3F3Llz6e7upre3l7POOouxY8fy0EMPMX36dHp7e5kw\nYQK9vb1ccMEFrFixgpUrV7Jo0SI2b97M2LFjueaaazj00ENLP5YRGQqS2lOZX5h29WXylltu4cQT\nT2Tq1KmMHz+e1atXs379em655RZ+/vOfs88++/Dyyy8zbtw4Lr/8ci699FK6u7t3ub9p06bxwAMP\n0NnZyd13383Xv/51brrppmYf1rsYCpI0REuXLmXRokUAnHHGGSxdupTM5POf/zz77LMPAOPGjdut\nz3z11Vf53Oc+x69//Wsigi1btjS97h0xFCRpCF5++WXuvfdefvWrXxERbN26lYjgU5/61Ht6f2dn\nJ9u2bQPY7vqCv/qrv+L4449n2bJlPPPMMxx33HFllP/ueoZlL5I0DKqYL7zxxhv57Gc/yw9/+MNi\n3Uc/+lH2339/rrnmGs4666ztho/2228/Xn/99aJtV1cXq1evZu7cudsND7366qtMnDgRqE1OD5cR\nc/aRJJVh6dKlnHbaadutW7BgAS+++CKnnnoq3d3dzJo1i0svvRSAs88+m4ULFzJr1ix+//vfc9FF\nF7Fo0SK6u7vp6OgoPuOrX/0qX/va1zjyyCPp7+8ftuOJzBy2nTVDd3d3DuYhO40TUO109lGrH4s0\nVI8//jjTp0+vuow9yo7+TiJidWbuenYbewqSpAaGgiSpYChIkgqGgiSpYChIkgqGgiSpYChI0hA9\n88wzHH744e9af84557BmzZrS9tvV1cVLL73U1M/0imZJKsmVV15ZdQm7zZ6CJDVBf38/Z511FtOn\nT+eTn/wkb7zxBscddxxvX2x73nnn0d3dzWGHHcZFF11UvO/CCy9kxowZzJw5kwsuuACADRs2sGDB\nAo466iiOOuoofvaznwGwceNGTjjhBA477DDOOeccyrj42J6CpLbxjdt2/dSzofj2KdN2uf2JJ57g\nqquuYvbs2XzhC1/gBz/4wfbv//a3GTduHFu3bmXOnDk8+uijTJw4kWXLlrF27Voigt/97ncALFq0\niC9/+cv09PTw7LPP8vGPf5zHH3+ciy++mJ6eHr71rW9x++23c9VVVzX9OA0FSWqCgw46iNmzZwPw\nmc98hssuu2y77TfccANLliyhv7+fF198kTVr1jBjxgzGjBnDF7/4RebNm1c8ZvPuu+/ebi7itdde\nY9OmTdx///3cfPPNAJx88skccMABTT8OQ0GSmiAidvr6N7/5DZdeeimrVq3igAMO4Oyzz2bz5s10\ndnaycuVK7rnnHm688UYuv/xy7r33XrZt28bDDz/MmDFjhvswDAVJ7WOgIZ4yPfvsszz00EN8+MMf\n5tprr6Wnp4fbbrsNqH3T33fffdl///357W9/yx133MFxxx3Hpk2beOONNzjppJOYPXs2H/zgBwE4\n4YQT+P73v89XvvIVAB555BFmzZrFRz7yEa699lq++c1vcscdd/DKK680/TicaJakJjj00EO54oor\nmD59Oq+88grnnXdese2II47gyCOPZNq0aZx55pnFMNPrr7/OvHnzmDlzJj09PXz3u98F4LLLLqO3\nt5eZM2cyY8YMFi9eDMBFF13E/fffz2GHHcbNN9/MwQcf3PTjsKcgSUPU1dXF2rXvnuResWJFsbyz\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x22cbb69af98>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "resp = nsfg.ReadFemResp()\n",
    "#age_under_18=resp[resp.age_r<18]\n",
    "pmf=thinkstats2.Pmf(resp.numkdhh,label=\"Actual\")\n",
    "Bias=BiasPmf(pmf,\"biased\")\n",
    "thinkplot.PrePlot(2)\n",
    "thinkplot.Pmfs([pmf,Bias])\n",
    "thinkplot.Config(xlabel=\"Children\",ylabel=\"PMF\")"
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
