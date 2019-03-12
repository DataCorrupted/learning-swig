#include <vector>

using namespace std;

typedef pair<int, int> Loc;

class MaxRect{
private:
	int height;
	int width;
	vector<vector<double>> m_map;
	vector<vector<double>> m_partialSum;
	pair<Loc, Loc> m_maxRectLoc;
	int m_maxRectSize = 0;

private:
	double getRectSum(Loc& upperLeft, Loc& lowerRight);
	int getRectSize(Loc& upperLeft, Loc& lowerRight);
public:
	MaxRect(vector<vector<double>>);
	~MaxRect(){};
	void calMaxRect(double);
	pair<Loc, Loc> getMaxRectLoc();
	int getMaxRectSize();
};