#include <iostream>
#include <math.h>
using namespace std;

int main (){
	const int x = 4;
	const int y = 4;	
	int promedio [x][y];
	
	cout << "Ingrese los valores :) " << endl;
	for (int i = 0; i < x ; i++){
		for (int j = 0; j < y ; j++){
				cout << "[" << i << "]" <<"[" << j << "]" << " : " ;
				cin >> promedio [i][j];
		}
		cout << endl;
	}
	
	x1 /= 4.0;
	x2 /= 4.0;
	x3 /= 4.0;
	x4 /= 4.0;
	
	cout << "x1 = " << x1 << endl;
	cout << "x2 = " << x2 << endl;
	cout << "x3 = " << x3 << endl;
	cout << "x4 = " << x4 << endl;
	
	
	
	for (int i = 0; i < x ; i++){
		cout << endl;
		for (int j = 0; j < y ; j++){
			cout << "    " << promedio [x][y];
			
		}	
 }
	return 0;
}

