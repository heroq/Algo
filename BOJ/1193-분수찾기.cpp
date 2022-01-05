#include <iostream>
#include <string>
#include <vector>	
#include <algorithm>
#include <cstdlib>

using namespace std;
/*
2,3,4,5... 개수가 상승

> 더해주는 값 2,3..
> 1+(더한값-원래값)

기본값 1
+2 = 3 ~ 1+(2-1) 2는 2/1 0
+3 = 6 ~ 1+(6-3) 4는 3/1 1
+4 = 10 ~ 1+(10-4) 7는 1/4 0

처음에는 1

1. 5가 입력이 될 경우
2. 5의 값의 위치를 찾아야함.
3. +2, +3을 해줌
	- for써서 +2
4. 그리고 계산 1+(6-3) 4~6을 찾음
	- temp에 값을 넣고 계산때리고 범위 찾음
5. 1일 경우 위에서 부터 6부터 분모 3,2,1
	- 짝수일경우 2, 4, 6 
6. 분자는 1,2,3
7. 6은 3/1 5는 2/2
*/

int main(int argc, char** argv) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long long n;
	cin >> n;
	
	if(n == 1){
		cout << "1/1";
		return 0;
	}

	int max = 1, check = 0;
	int i = 1, def = 0, min = 0;	
	int temp = 0;
	
	int cnt = 0;
	int a=1, b=1;
	
	while(true){
		def = i;
		i ++;
		temp = i;
		max += i;
		min = (max - i)+1;
		cnt = (max - min)+1;

		if(cnt % 2 == 0) check = 0;
		else check = 1;
		
		// 0 log -> high
		// 1 high -> low
		
		if(check == 0){
			a = 1, b = cnt;
			for(int k=min; k<max; k++){
				if(k == n) break;
				b --;
				a ++;
			}
		}else{
			a = cnt, b = 1;
			for(int k=min; k<max; k++){
				if(k == n) break;
				b ++;
				a --;
			}
		}
			
		if(n <= max) break;
	}
	cout << a << "/" << b;
	return 0;
}