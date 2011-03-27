// Willis Wendler, 2011
// wlib.cpp
// contains structures/functions I tend to use in different programs

#include <math.h>

#include "wlib.h"

namespace wlib
{
    Vector & Vector::operator=(const Vector &a)
    {
        x = a.x;
        y = a.y;
        return *this;
    }

    const Vector Vector::operator+(const Vector &a)
    {
        Vector nv;
        nv.x = x + a.x;
        nv.y = y + a.y;
        return nv;
    }

    const Vector Vector::operator-(const Vector &a)
    {
        Vector nv;
        nv.x = x - a.x;
        nv.y = x - a.y;
        return nv;
    }

    const Vector Vector::operator*(double a)
    {
        Vector nv;
        nv.x = x*a;
        nv.y = y*a;
        return nv;
    }

    double Vector::magnitude()
    {
        return sqrt(x*x + y*y);
    }

    Vector::Vector()
    {
        x = 0.0;
        y = 0.0;
    }

    Color::Color()
    {
        r = 0;
        g = 0;
        b = 0;
    }
}

