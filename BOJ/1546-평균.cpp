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
	
	int cnt, max = -1000000001;
	cin >> cnt;
	cin.ignore();
	
	string score;
	getline(cin, score);
	stringstream f(score);
	string buffer;
	
	vector<double> arr;
	while(getline(f, buffer, ' ')){
		if(stoi(buffer) > max) max = stod(buffer);
		arr.push_back(stod(buffer));
	}
	
	double temp;
	for (vector<double>::iterator itr = arr.begin(); itr != arr.end(); ++itr) { 
		temp += (*itr/max)*100;
	}
	// 225가 나와야함 temp가.
	cout << temp/cnt;
}
