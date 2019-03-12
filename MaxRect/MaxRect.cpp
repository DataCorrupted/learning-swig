#include "MaxRect.h"
#include <iostream>

double MaxRect::getRectSum(Loc& upperLeft, Loc& lowerRight){
	Loc& lr = lowerRight;
	Loc& ul = upperLeft;

	return m_partialSum[lr.first+1][lr.second+1] 
			- m_partialSum[ul.first][lr.second+1]
			- m_partialSum[lr.first+1][ul.second]
			+ m_partialSum[ul.first][ul.second];
}
int MaxRect::getRectSize(Loc& upperLeft, Loc& lowerRight){
	return (lowerRight.first - upperLeft.first + 1)
			* (lowerRight.second - upperLeft.second + 1);
}

MaxRect::MaxRect(vector<vector<double>> map):
		height(map.size()), width(map.back().size()), m_map(map){
	m_partialSum.push_back(vector<double>(width+1, 0));
	for (int i=1; i<=height; i++){
		m_partialSum.push_back(vector<double>(width+1, 0));
		for (int j=1; j<=width; j++){
			m_partialSum[i][j] = 
					m_map[i-1][j-1] 
					+ m_partialSum[i-1][j] + m_partialSum[i][j-1] 
					- m_partialSum[i-1][j-1];
		}
	}
};

void MaxRect::calMaxRect(double threshold){
	for (int i=0; i<height-1; i++){
	for (int j=0; j<width-1; j++){
		for (int x=i+1; x<height; x++){
		for (int y=j+1; y<width; y++){
			Loc upperLeft(i, j);
			Loc lowerRight(x, y);
			int rectSize = getRectSize(upperLeft, lowerRight);
			if (rectSize < m_maxRectSize){
				continue;
			}
			double avg = getRectSum(upperLeft, lowerRight) / rectSize;
			if (avg > threshold) {
				m_maxRectSize = rectSize;
				m_maxRectLoc=pair<Loc, Loc>(upperLeft, lowerRight);
			}
		}}
	}}
};
pair<Loc, Loc> MaxRect::getMaxRectLoc(){
	return m_maxRectLoc;
};
int MaxRect::getMaxRectSize(){
	return m_maxRectSize;
};