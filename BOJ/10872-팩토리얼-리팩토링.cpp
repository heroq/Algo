#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int fac(int a){
	if(a <= 1) return 1;
	// 5 * 4 > 4 * 
	else return a * fac(a-1);
}

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a;
	cin >> a;
	int r = fac(a); // 5
	cout << r;
}