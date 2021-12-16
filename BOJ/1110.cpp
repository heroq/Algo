#include <iostream>
#include <string>
using namespace std;

void zeroCheck(int *q, int *w){
	if(*q > 0 && *w == -48){
		int temp = *q;
		*q = 0;
		*w = temp;
	}
}

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string a;
	cin >> a;
	
	int x, y, sum, count=0;
	
	
	x = a[0] - '0';
	y = a[1] - '0';
	zeroCheck(&x, &y);
	string default_a = to_string(x)+to_string(y);
	// ---
	sum = x + y;
	
	string temp;
	temp = to_string(sum);
	x = y;
	if(temp[1] > 0) y = temp[1] - '0';
	else y = temp[0] - '0';
	
	count++;
	// ---
	string check;
	while(true){
		if(x < 0) break;
		count++;
		zeroCheck(&x, &y);
		sum = x + y;
		
		temp = to_string(sum);
		x = y;
		if(temp[1] > 0) y = temp[1] - '0';
		else y = temp[0] - '0';
		
		check = to_string(x)+to_string(y);
		if(default_a.compare(check) == 0) break;
	}
	cout << count;
	return 0;
}