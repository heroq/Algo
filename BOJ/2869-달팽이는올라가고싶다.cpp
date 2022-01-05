#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>

using namespace std;

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int a, b, v;
	cin >> a >> b >> v;
	
	double result = (double)(v-b)/(a-b);
	cout.precision(11);
	cout << ceil(result);
}
