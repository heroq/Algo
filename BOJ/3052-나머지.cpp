#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<int> arr;
	int temp;
	// 결과값 중복 제거 한 개수
	for(int i=0; i<10; i++){
		cin >> temp;
		arr.push_back(temp % 42);
	}
	
	sort(arr.begin(), arr.end());
	arr.erase(unique(arr.begin(), arr.end()), arr.end());
	int cnt = 0;
	cout << arr.size();
}
