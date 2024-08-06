#include <iostream>
#include "Solution.h"
#include "Rat.h"

using namespace std;

int main() {
    const Rat r(0,1);
    vector<vector<Rat>> matrix(2, vector<Rat>(4, r));
    int arr[] = {0, -7, -4, 2, 2, 4, 6, 12, 3, 1, -1, -2}; // 3, 4
    int arr1[] = {1, 2, 3, 6, 0, 1, 2, 4, 0, 0, 1, 3}; // 3, 4
    int arr2[] = {2, 10, -1, 3, 15, 2}; // 2, 3
    int arr3[] = {2, 1, 12, 1, 1, 2, 9, -1}; // 2, 4
    int arr4[] = {-2, -3, -2, 3, -2, -2, 3, -2, -1, -1, -1, -2}; // 4, 3
    int a = 0;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            matrix[i][j] = arr3[a];
            cout << matrix[i][j].printVal() << " ";
            a++;
        }
        cout << endl;
    }
    cout << endl;
    Solution::rref(matrix);
    Solution::printMatrix(matrix);
    return 0;
}
