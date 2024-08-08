//
// Created by Froys on 02/08/2024.
//

#include "Rat.h"
#include <string>

using namespace std;

string Rat::printVal() const {
    if (n == 0) return "0";
    if (d == n) return "1";
    string ret = std::to_string(n);
    if (d != 1) {
        ret.append(1, '/');
        ret.append(std::to_string(d));
    }
    return ret;
}

