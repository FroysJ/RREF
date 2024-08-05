//
// Created by Froys on 02/08/2024.
//

#include "Solution.h"
#include <vector>

using namespace std;

void rref(vector<vector<Rat>>& matrix) {
    ref(matrix);
    int rows = matrix.size();
    int cols = matrix[0].size();
    int r = rows - 1;
    for (int i = cols - 1; i >= 0 && r >= 0; i--) {
        int currRow = r;
        while (currRow >= 0 && matrix[currRow][c].getN() == 0) {
            currRow--;
        }
        if (currRow != -1 && matrix[currRow][c].getN() == matrix[currRow][c].getD()) {
            for (int j = i-1; j >= 0; j--) {
                if (matrix[j][c].getN() != 0) {
                    Rat factor = matrix[j][c];
                    for (int k = c; k < cols; k++) {
                        matrix[j][k] -= (factor * matrix[i][k]);
                    }
                }
            }
            r--;
        }
    }
}

void ref(vector<vector<Rat>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int c = 0;
    for (int i = 0; i < rows && c < cols; i++) {
        if (matrix[i][c].getN() != 0) {
            if (matrix[i][c].getN() != matrix[i][c].getD()) {
                Rat scale(matrix[i][c].getD(), matrix[i][c].getN());
                for (Rat r : matrix[i]) {
                    r *= scale;
                }
            }
            for (int j = i+1; j < rows; j++) {
                if (matrix[j][c].getN() != 0) {
                    Rat factor = matrix[j][c];
                    for (int k = c; k < cols; k++) {
                        matrix[j][k] -= (factor * matrix[i][k]);
                    }
                }
            }
            c++;
        } else {
            int j = i+1;
            for (j; j < rows; j++) {
                if (matrix[j][c].getN() != 0) {
                    swap(matrix[i], matrix[j]);
                    break;
                }
            }
            i--;
            if (j == rows) {
                c++;
            }
        }
    }
}

vector<Rat> ldiv(vector<Rat>& p1, vector<Rat>& p2) {
    vector<Rat> q;
    return q;
}
