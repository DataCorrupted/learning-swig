%module MaxRect
%{
#include "MaxRect.h"
%}
%include "std_pair.i"
%include "std_vector.i"
namespace std {

  /* On a side note, the names VecDouble and VecVecdouble can be changed, but the order of first the inner vector matters! */
  %template(VecDouble) vector<double>;
  %template(VecVecdouble) vector< vector<double> >;

  %template(PyLoc) std::pair<int, int>;
  %template(PyLocPair) std::pair<std::pair<int, int>, std::pair<int, int>>;
}

%include "MaxRect.h"