//
// Created by Froys on 02/08/2024.
//

#ifndef SOLUTION_H
#define SOLUTION_H

#include <vector>

#include "Rat.h"


class Solution {
public:
    static void rref(vector<vector<Rat>>& matrix);
    static void ref(vector<vector<Rat>>& matrix);
    static void printMatrix(const vector<vector<Rat>>& matrix);
    static void printVector(const vector<Rat>& vec);
    static vector<Rat> sdiv(const vector<Rat>& p, const vector<Rat>& d);
    static vector<vector<int>> ratMatrixToInt(vector<vector<Rat>>& matrix);
    static vector<int> ratVectorToInt(vector<Rat>& vec);
    static vector<vector<int>> int_rref(vector<vector<int>>& matrix);
    static vector<int> int_sdiv(vector<int>& p, vector<int>& d);
};



#endif //SOLUTION_H
