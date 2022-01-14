#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;
long fibo(int n){
	if(n == 0) return 0;
	if(n == 1) return 1;
	return fibo(n-2) + fibo(n-1);
}

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n;
	cin >> n;
	long c = fibo(n);
	cout << c;
}