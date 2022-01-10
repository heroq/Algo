#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int fac(int a, int b){
	if(b == 2) return 2;
	if(a < 0 ) return 1;
	if(a <= 1 ) return a * b;
	int tmp = a * b;
	// cout << tmp << "\n";
	return fac(a-1, tmp);
}

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a;
	cin >> a;
	int r = fac(a-2, a*(a-1));
	cout << r;
}