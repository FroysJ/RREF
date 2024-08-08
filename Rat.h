//
// Created by Froys on 02/08/2024.
//

#ifndef RAT_H
#define RAT_H

#include <numeric>
#include <cmath>
#include <iostream>

using namespace std;

class Rat {
public:
    Rat(int value) : n(value), d(1) {}
    constexpr Rat(int num, int den) : n(num), d(den) {}
    constexpr void simplify() {
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
    constexpr Rat& operator*=(const Rat& rhs) {
        int newN = n * rhs.n / gcd(n * rhs.n, d * rhs.d);
        d = d * rhs.d / gcd(n * rhs.n, d * rhs.d);
        n = newN;
        simplify();
        return *this;
    }
    constexpr Rat& operator/=(const Rat& rhs) {
        Rat newR(rhs.d, rhs.n);
        *this *= newR;
        return *this;
    }
    constexpr Rat& operator+=(const Rat& rhs) {
        int l = lcm(d, rhs.d);
        n = (n * (l / d)) + (rhs.n * (l / rhs.d));
        d = l;
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
    static constexpr int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    static constexpr int lcm(int a, int b) {
        return (a / gcd(a, b)) * b;
    }
    int n;
    int d;
    [[nodiscard]] string printVal() const;
};

constexpr Rat& operator*(const Rat& lhs, const Rat& rhs) {
    Rat lhsc = lhs;
    return lhsc *= rhs;
}

constexpr Rat& operator/(const Rat& lhs, const Rat& rhs) {
    Rat lhsc = lhs;
    return lhsc /= rhs;
}

constexpr Rat& operator+(const Rat& lhs, const Rat& rhs) {
    Rat lhsc = lhs;
    return lhsc += rhs;
}

constexpr Rat& operator-(const Rat& lhs, const Rat& rhs) {
    Rat lhsc = lhs;
    return lhsc -= rhs;
}

#endif //RAT_H
