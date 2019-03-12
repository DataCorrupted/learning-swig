#include <iostream>
#include "MaxRect.h"

using namespace std;

template<class P1, class P2>
ostream& operator << (ostream& o, const pair<P1, P2>& p){
	o << "(" << p.first << ", " << p.second << ")";
	return o;
}

int main(int argc, char** argv){
	vector<vector<double>> m({
		{31, 32, 29, 25, 24, },
		{25, 30, 29, 25, 24, },
		{20, 22, 29, 31, 40, },
		{31, 23, 29, 20, 40, },
		{31, 32, 16, 15, 50, },
	});
	MaxRect map(m);
	map.calMaxRect(30);
	cout << map.getMaxRectLoc() << " " << map.getMaxRectSize() << endl;
}