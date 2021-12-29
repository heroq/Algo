#include <iostream>
#include <string>
#include <vector>	
#include <algorithm>
#include <cstdlib>

using namespace std;
vector<int> arr;
void selfNumber(int temp){
	int check = 0;
	
	for(int x=temp; x>0; x--){
		string casting = to_string(x);
		int get = x;
		int plus = 0;
		
		for(int i=0; i<casting.size(); i++){
			plus += casting[i] - '0';
		}
		
		int result = get + plus;
		if(result == temp){
			check = 1;
			break;
		}
	}
	
	if(check == 0) arr.push_back(temp);
	temp++;
	if(temp < 10000) selfNumber(temp);
}

int main(int argc, char** argv) {
	selfNumber(1);
	
	vector<int>::iterator iter;
	for(iter=arr.begin(); iter != arr.end(); iter++){
		cout << *iter << "\n";
	}
	
	return 0;
}