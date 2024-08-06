//
// Created by Froys on 02/08/2024.
//

#include "Solution.h"
#include <vector>

using namespace std;

void Solution::rref(vector<vector<Rat>>& matrix) {
    ref(matrix);
    int rows = matrix.size();
    int cols = matrix[0].size();
    int r = rows - 1;
    for (int i = cols - 1; i >= 0 && r >= 0; i--) {
        int currRow = r;
        while (currRow >= 0 && matrix[currRow][i].n == 0) {
            currRow--;
        }
        if (currRow != -1 && matrix[currRow][i].n == matrix[currRow][i].d) {
            for (int j = currRow-1; j >= 0; j--) {
                if (matrix[j][i].n != 0) {
                    Rat factor = matrix[j][i];
                    for (int k = i; k < cols; k++) {
                        matrix[j][k] -= (factor * matrix[currRow][k]);
                    }
                }
            }
            r--;
        }
    }
}

void Solution::ref(vector<vector<Rat>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int c = 0;
    for (int i = 0; i < rows && c < cols; i++) {
        if (matrix[i][c].n != 0) {
            if (matrix[i][c].n != matrix[i][c].d) {
                Rat scale(matrix[i][c].d, matrix[i][c].n);
                cout << "scale factor: " << scale.n << "/" << scale.d << endl;
                for (int g = 0; g < cols; g++) {
                     matrix[i][g] *= scale;
                }
                cout << "scale to 1" << endl;
                printMatrix(matrix);
            }
            for (int j = i+1; j < rows; j++) {
                if (matrix[j][c].n != 0) {
                    Rat factor = matrix[j][c];
                    cout << "factor: " << factor.n << "/" << factor.d << endl;
                    for (int k = c; k < cols; k++) {
                        matrix[j][k] -= (factor * matrix[i][k]);
                    }
                }
            }
            cout << "clear down" << endl;
            printMatrix(matrix);
            c++;
        } else {
            int j = i+1;
            for (j; j < rows; j++) {
                if (matrix[j][c].n != 0) {
                    swap(matrix[i], matrix[j]);
                    cout << "swap to make nonzero" << endl;
                    printMatrix(matrix);
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

void Solution::printMatrix(const vector<vector<Rat>> &matrix) {
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            cout << matrix[i][j].printVal() << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void Solution::printVector(const vector<Rat>& vec) {
    for (auto i : vec) {
        cout << i.printVal() << " ";
    }
    cout << endl;
}


vector<Rat> Solution::sdiv(const vector<Rat>& p, const pair<Rat,Rat>& d) {
    Rat factor(d.first.d, d.first.n);
    Rat mult = -1 * factor * d.second;
    vector<Rat> q(p.size(), p[0]);
    for (int i = 1; i < p.size(); i++) {
        Rat em = mult * q[i-1];
        Rat eh = p[i] + em;
        q[i] = eh;
    }
    for (int i = 0; i < q.size()-1; i++) {
        q[i] *= factor;
    }
    return q;
}

