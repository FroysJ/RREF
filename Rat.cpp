//
// Created by Froys on 02/08/2024.
//

#include "Rat.h"
#include <vector>

using namespace std;

Rat::Rat(int value) {
    n = value;
    d = 1;
    val = (double) value;
}

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

constexpr Rat& operator*=(const Rat& rhs) {
    int newN = n * rhs.getN() / gcd(n * rhs.getN(), d * rhs.getD());
    d = d * rhs.getD() / gcd(n * rhs.getN(), d * rhs.getD());
    n = newN;
    return *this;
}

constexpr Rat& operator*(Rat lhs, const Rat& rhs) {
    return lhs *= rhs;
}

constexpr Rat& operator-=(const Rat& rhs) {
    int lcm = lcm(d, rhs.getD());
    d = lcm;
    n = (n * (lcm / d)) + (rhs.getN() * (lcm / rhs.getD()));
}

