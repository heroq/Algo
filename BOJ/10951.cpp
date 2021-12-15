#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>

using namespace std;
int a, b;
int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<int> v;	
	while(!cin.eof()){
		a = 0, b = 0;
		cin >> a >> b;
		
		v.push_back(a+b); 
	}

	int cnt = 0;
	while(cnt < v.size()-1){
		cout << v[cnt] << "\n";
		cnt++;
	}
	return 0;
}
