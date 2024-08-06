//
// Created by Froys on 02/08/2024.
//

#include "Rat.h"
#include <vector>
#include <cmath>

using namespace std;

string Rat::printVal() const {
    if (n == 0) return "0";
    if (d == n) return "1";
    string ret = to_string(n);
    if (d != 1) {
        ret.append(1, '/');
        ret.append(to_string(d));
    }
    return ret;
}

void Rat::simplify() {
    if (n == 0) {
        d = 1;
        return;
    }
    if (n == d) {
        n = 1;
        d = 1;
        return;
    }
    bool neg = false;
    if (((d < 0) && (n > 0)) || ((d > 0) && (n < 0))) {
        neg = true;
    }
    d = abs(d);
    n = abs(n);
    int g = gcd(n, d);
    if (g != 1) {
        d /= g;
        n /= g;
    }
    if (neg) {
        n *= -1;
    }
}

