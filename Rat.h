//
// Created by Froys on 02/08/2024.
//

#ifndef RAT_H
#define RAT_H

#include <vector>
using namespace std;

class Rat {
public:
    Rat(int n, int d);
    bool isInt();
    int getN();
    int getD();
    double getVal();
private:
    int n;
    int d;
    double val;
};



#endif //RAT_H
