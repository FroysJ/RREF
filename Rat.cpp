//
// Created by Froys on 02/08/2024.
//

#include "Rat.h"
#include <vector>

using namespace std;

Rat::Rat(int num, int denom) {
    n = num;
    d = denom;
    if (d == 0) {
        val = numeric_limits<double>::max();
        if (n < 0) val *= -1;
    } else {
        val = (double) n / (double) d;
    }
}

bool isInt() {
    return (double) (n / d) == val;
}

int getN() {
    return n;
}

int getD() {
    return d;
}

double getVal() {
    return val;
}

