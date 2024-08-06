//
// Created by Froys on 02/08/2024.
//

#ifndef SOLUTION_H
#define SOLUTION_H

#include "Rat.h"
#include <vector>
using namespace std;


class Solution {
public:
    static void rref(vector<vector<Rat>>& matrix);
    static void ref(vector<vector<Rat>>& matrix);
    static void printMatrix(const vector<vector<Rat>>& matrix);
    static void printVector(const vector<Rat>& vec);
    static vector<Rat> sdiv(const vector<Rat>& p, const pair<Rat,Rat>& d);
};



#endif //SOLUTION_H
