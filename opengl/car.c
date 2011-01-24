// willis wendler, 2011
// car.c
// code for an accelerating car...

#include <math.h>
#include "car.h"

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

const Vector Vector::operator*(double a)
{
    Vector nv;
    nv.x = x*a;
    nv.y = x*y;
    return nv;
}

Vector::Vector()
{
    x = 0.0;
    y = 0.0;
}

void Car::move(double t)
{
    velocity = velocity + acceleration*t;
    location = location + velocity*t;
}

void Car::turn(double theta)
{
    direction += theta;
    acceleration.x = cos(direction);
    acceleration.y = sin(direction);
}

Car::Car()
{
    direction = 0.0;
}

