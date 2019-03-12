#include "MaxRect.h"
#include <iostream>
#include <set>
#include <cmath>

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
double MaxRect::getPSNR(Loc& upperLeft, Loc& lowerRight){
	int rectSize = getRectSize(upperLeft, lowerRight);
	double mse = getRectSum(upperLeft, lowerRight) / rectSize / 3;
	return 20*log10(255) - 10*log10(mse);
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
			double psnr = getPSNR(upperLeft, lowerRight);
			if (psnr > threshold) {
				m_maxRectSize = rectSize;
				m_maxRectLoc=LocPair(upperLeft, lowerRight);
			}
		}}
	}}
};
#define TEST_NEW_LOC_PAIR_AND_INSERT_ON_TRUE(ul, lr, set) 	\
	if (ul.first >= 0 && ul.first < height && 				\
			ul.second >= 0 && ul.second < width && 			\
			lr.first >= 0 && lr.first < height && 			\
			lr.second >=0 && lr.second < width){			\
		double psnr = getPSNR(ul, lr);						\
		if (psnr >= threshold){								\
			set.insert({ul, lr});							\
			int size = getRectSize(upperLeft, lowerRight); 	\
			if (size > m_maxRectSize) {						\
				m_maxRectSize = size;						\
				m_maxRectLoc=LocPair(ul, lr);				\
			}												\
		}													\
	}
void MaxRect::calMaxRectBFS(double threshold){
	for (int i=0; i<height; i++){
	for (int j=0; j<width; j++){
		if (m_map[i][j] >= threshold){
			Loc currLoc(i, j);
			set<LocPair> Q({LocPair(currLoc, currLoc)});
			while (!Q.empty()){
				LocPair newLocPair = *Q.begin();
				Q.erase(Q.begin());
				Loc newLoc;
				Loc upperLeft = newLocPair.first;
				Loc lowerRight = newLocPair.second;

				// Push up a row
				newLoc = upperLeft; newLoc.first --;
				TEST_NEW_LOC_PAIR_AND_INSERT_ON_TRUE(newLoc, lowerRight, Q)
				// Push left a column
				newLoc = upperLeft; newLoc.second --;
				TEST_NEW_LOC_PAIR_AND_INSERT_ON_TRUE(newLoc, lowerRight, Q)
				// Push down a row
				newLoc = lowerRight; newLoc.first ++;
				TEST_NEW_LOC_PAIR_AND_INSERT_ON_TRUE(upperLeft, newLoc, Q)
				// Push right a column
				newLoc = lowerRight; newLoc.second ++;
				TEST_NEW_LOC_PAIR_AND_INSERT_ON_TRUE(upperLeft, newLoc, Q)
			}
		}
	}}
}
LocPair MaxRect::getMaxRectLoc(){
	return m_maxRectLoc;
};
int MaxRect::getMaxRectSize(){
	return m_maxRectSize;
};