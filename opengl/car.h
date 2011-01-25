// willis wendler, 2011
// car.h
// code for an accelerating car...

#ifndef CAR_H
#define CAR_H

class Vector
{
    public:
        double x;
        double y;
        Vector & operator=(const Vector &);
        const Vector operator+(const Vector &);
        const Vector operator*(double);
        double magnitude();
        Vector();
};

class Car
{
    public:
        Vector location;
        Vector velocity;
        Vector acceleration;
        double direction;
        double max_speed;
        void move(double);
        void turn(double);
        Car();
};

#endif

