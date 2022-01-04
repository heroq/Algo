#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

// 135의 값을 받으면 이 값 사이의 공차가 몇개인지
// 100~135의 값  
// 구하는 것 
int arithmetic(int a){
	int cnt;
	if(a < 100) return a;
	if(a == 1000) a = 999;
	cnt = 99;
	
	for(int i=100; i<=a; i++){
		int on = i / 100; // 백의 자리
		int tw = (i / 10) % 10; // 십의 자리 
		int th = i % 10; // 일의 자리
		
		if( (on-tw) == (tw-th) ){
			cnt ++;
		} 
	}
	return cnt;
}
 
int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
 	int a;
 	cin >> a;
	int b = arithmetic(a);
	cout << b;
}