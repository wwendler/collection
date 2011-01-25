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

void Car::move(double t)
{
    velocity = velocity + acceleration*t;
    double mag = velocity.magnitude();
    if (mag > max_speed)
        velocity = velocity*(max_speed/mag);
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
    max_speed = 10.0;
    direction = 0.0;
    turn(0.0);
}

