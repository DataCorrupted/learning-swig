# learning-swig

This repo is created to learn swig. It has code I write to play with swig to create python-c++ interface.

It all started when I have a O(n^2m^2) problem where n=32, m=30000+. The front end was written in python and I didn't bother to change it. So I used C++ to do the heavy lifting. :)

You can check swig [here](http://www.swig.org/), it is really handy.

## The problem

I was dealing with the following problem:

Given a n * m matrix _A_ with positive real numbers inside.
A threshold _h_ is also provided.
Find a maxium sub-matrix so that the average of the sub-matrix is greater than _h_.

### My Solution

Partial sum is a notion in [series](https://en.wikipedia.org/wiki/Series_(mathematics)). It helps deciding if a series is convergent.

However, an extra upside of partial sum in computer science is that it only take O(n) to calculate and can manage queries of segment sum in O(1) time.
I managed to use a partial sum on 2-D surface. So I can calcualte any sub-matrix's sum in O(1) time.

The left part? Search (almost) every possible sub-matrix in the matrix, there are O(n^2m^2) possibilities. Since query time is O(1) and partial sum takes O(mn), the algorithm takes O(n^2m^2).

(Now you see why I prefer C++ despite all the troubles.)