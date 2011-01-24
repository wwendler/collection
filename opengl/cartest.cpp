// willis wendler, 2011
// cartest.cpp
// a function to test whether my car works...

#include <stdio.h>
#include "car.h"

int main()
{
    printf("starting accelacar\n");
    Car a;
    printf("acc %lf, %lf\n", a.acceleration.x, a.acceleration.y);
    a.move(2.0);
    printf("loc %lf, %lf\n", a.location.x, a.location.y);
    a.turn(0.0);
    printf("acc %lf, %lf\n", a.acceleration.x, a.acceleration.y);
    a.move(2.0);
    printf("loc %lf, %lf\n", a.location.x, a.location.y);
    a.turn(1.6);
    a.move(2.0);
    printf("loc %lf, %lf\n", a.location.x, a.location.y);
    printf("vel %lf, %lf\n", a.velocity.x, a.velocity.y);
    a.move(2.0);
    printf("loc %lf, %lf\n", a.location.x, a.location.y);
    printf("kaboom!\n");
}
