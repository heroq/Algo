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

	int max = -1000001, i = 0, pos = 0;
	while(true)
	{
		int get;
		cin >> get;
		if(cin.eof() == true) break;
		if(get > max){
			max = get;
			pos = i;	
		}
		i++;
	}
	cout << max << "\n" << (pos+1);
}
