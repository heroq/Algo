#include <iostream>
#include <string>
#include <vector>	
#include <algorithm>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a, b, c;
	cin >> 	a >> b >> c;
	if(a <= 0 || (c-b) <= 0){
		cout << "-1";
		return 0;
	}
	int result = (a / (c-b))+1;
	if(result < 0) result = -1;
	cout << result;
	return 0;
}