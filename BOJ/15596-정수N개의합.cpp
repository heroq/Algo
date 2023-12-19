#include <iostream>
#include <string>
#include <vector>
using namespace std;
long long sum(vector<int> &a){
	std::vector<int>::iterator iter;
	long long result = 0;
	for(iter = a.begin(); iter != a.end(); iter++){
		result += *iter;
	}
	return result;
}


int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<int> aa;
	aa.push_back(1);
	aa.push_back(2);
	aa.push_back(3);
	int a = sum(aa);
	cout << a;

	return 0;
}