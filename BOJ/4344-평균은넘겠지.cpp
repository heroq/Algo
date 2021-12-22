#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>

using namespace std;

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int cnt;
	cin >> cnt;
	cin.ignore();
	
	vector<double> arr;
	for(int i=0; i<cnt; i++){
		string score;
		getline(cin, score);
		string buffer;
		stringstream ss(score);
		
		int index = 0;
		double temp = 0, store = 0;
		vector<double> tempArr;
		while(getline(ss, buffer, ' ')){
			if(index == 0){
				temp = stod(buffer);
			}else{
				store += stod(buffer);
				tempArr.push_back(stod(buffer));
			} 
			index++;
		}
		
		double avg = store/temp;
		double winCnt = 0.0;
		for(vector<double>::iterator i = tempArr.begin(); i != tempArr.end(); ++i){
			if(*i > avg){
				winCnt++;
			}
		}
		
		int powResult = pow(10, 3);
		winCnt = round((winCnt/temp)*100 * powResult) / powResult;
		cout<<fixed;
		cout.precision(3);
		cout << winCnt << "%\n";
		continue;
	}
		
/*
	1. 몇개 받을지 인수 받음
	2. 인수 받은만큼 반복문 돌림
	3. 인수 받은거의 첫번째를 제외하고 평균을 구하면됨
	4. 평균을 출력 후 평균 넘는 비율을 반올림해야함
	
	>> 평균이 초과되야함
*/
}
