#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

/*
1. 첫째줄에 개수 받음
2. 개수 만큼 반복문 돌려서 OX를 받는다.
	- 1글자식 받아야함,
	- OX를 바로 계산을 한다.
	- O가 유지되면 +1씩 (ex 1+2+3)
	- X가 나오면 0으로 리셋
	- 결과를 vector 저장한다.
*/
using namespace std;

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int cnt;
	cin >> cnt;
	cin.ignore();
	
	vector<int> arr;
	int temp, result;
	for(int i=0; i<cnt; i++){
		temp = 0;
		result = 0;
		string score;
		getline(cin, score);
		for(int x=0; x<score.size(); x++){
			if(score[x] == 'O'){
				temp ++;
				result += temp;
			}else{
				temp = 0;
			}
		}
		arr.push_back(result);
	}
	
	vector<int>::iterator iter;
	for(iter = arr.begin(); iter != arr.end(); iter++){
		cout << *iter << "\n";
	}
}
