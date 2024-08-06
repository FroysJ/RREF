//
// Created by Froys on 02/08/2024.
//

#ifndef RAT_H
#define RAT_H

#include <vector>
#include <numeric>
#include <cmath>
#include <iostream>

using namespace std;

class Rat {
public:
    Rat(int value) : n(value), d(1) {}
    constexpr Rat(int num, int den) : n(num), d(den) {}
    void simplify();
    constexpr Rat& operator*=(const Rat& rhs) {
        int newN = n * rhs.n / gcd(n * rhs.n, d * rhs.d);
        d = d * rhs.d / gcd(n * rhs.n, d * rhs.d);
        n = newN;
        simplify();
        return *this;
    }
    constexpr Rat& operator-=(const Rat& rhs) {
        int l = lcm(d, rhs.d);
        n = (n * (l / d)) - (rhs.n * (l / rhs.d));
        d = l;
        simplify();
        return *this;
    }
    int n;
    int d;
    [[nodiscard]] string printVal() const;
};

constexpr Rat& operator*(const Rat& lhs, const Rat& rhs) {
    Rat lhsc = lhs;
    return lhsc *= rhs;
}

#endif //RAT_H
