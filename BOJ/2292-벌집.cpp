#include <iostream>
#include <string>
#include <vector>	
#include <algorithm>
#include <cstdlib>

using namespace std;
/*
1
6(2~7) 2층
12(8~19) 3층
18(20~37) 4층
24(38~61) 5층

> 45번 입력을 했다.
그니까 정리를 하면은
int a = 1 // 값들 6 * 1
int b = 1 // 이게 층 곱하기

a += 6 * b; = a는 7
7 += 6 * 2; = a는 19

여기서 이제 n이 a보다 낮을경우 b를 output
*/

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long long n;
	cin >> n;
	
	int floor = 1;
	long long temp = 1;
	while(true){
		if(n <= temp){
			cout << floor;
			break;
		}
		
		temp += 6 * floor;
		floor++;
	}
		
	return 0;
}