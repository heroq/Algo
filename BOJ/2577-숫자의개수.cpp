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

	int arr[3], temp;
	// A x B x C
	for(int i=0; i<3; i++){
		cin >> temp;
		arr[i] = temp;
	} 
	
	temp = arr[0] * arr[1] * arr[2];

	string strTemp = to_string(temp);
	int cnt = 0;
	int result[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	
	while(cnt < strTemp.size()){
		int getInt = strTemp.at(cnt) - '0';
		result[getInt] ++;
		cnt ++;
	}
	for(int i=0; i<10; i++){
		cout << result[i] << "\n";
	}
}
