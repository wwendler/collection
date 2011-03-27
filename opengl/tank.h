// Willis Wendler
// tank.h
// Code for a perfect battle like game...

#ifndef TANK_H
#define TANK_H

#include <vector>

// contains the Vector class, possibly other things in the future
#include "wlib.h"

using namespace wlib;

class Object
{
    public:
        double direction;
        Complex<double> location;
        Complex<double> velocity;
        Complex<double> acceleration;
        double radius;
        Color color;
        World * world;
        Object(World *);
        void move(double t);
        bool touching(const Object &);
};

class Quadnode
{
    public:
        double xmin;
        double xmid;
        double xmax;
        double ymin;
        double ymid;
        double ymax;
        bool isLeaf;
        // bad results if two objects in same place
        Object *object;
        // 0 is xmin, ymin. 1 is xmin, ymax.
        // 2 is xmax, ymin. 3 is xmax, ymax.
        Quadnode * quad[4];
        Quadnode(double, double, double, double);
        void addObject(Object *);
        // true if successful
        bool removeObject(Object *);
        // finds all collisions with object. how does it return them?
        void findCollisions(Object *);
        // finds out which quadtrant an object is in
        int getQuad(Object *);
        // returns a call to new Quadnode, using the proper parameters
        Quadnode * makeQuad(int);
};

#endif

