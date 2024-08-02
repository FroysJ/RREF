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
    void rref(vector<vector<Rat>>& matrix);
    void ref(vector<vector<Rat>>& matrix);
    vector<Rat> ldiv(vector<Rat>& p1, vector<Rat>& p2);
};



#endif //SOLUTION_H
