// Willis Wendler
// tank.cpp
// Code for a Perfect Battle like game...

#include <vector>

#include "tank.h"
#include "wlib.h"

using namespace std;
using namespace wlib;

Object::Object(World * w)
{
    world = w;
    direction = 0.0;
    radius = 0.0;
}

void Object::move(double t)
{
    velocity = acceleration*t;
    location = velocity*t;
}

bool Object::touching(const Object & obj)
{
    return abs(location - obj.location) <= radius + obj.radius;
}

Quadnode::Quadnode(double xmin, double ymin, double xmax, double ymax)
{
    this.xmin = xmin;
    this.ymin = ymin;
    this.xmax = xmax;
    this.ymax = ymax;
    this.xmid = (xmin + xmax)/2.0;
    this.ymid = (ymin + ymax)/2.0;
    isLeaf = true;
    object = NULL;
    for (int n = 0; n < 4; n++)
        quad[n] = 0;
}

Quadnode * Quadnode::makeQuad(int qn)
{
    switch(qn)
    {
        case 0:
            return new Quadnode(xmin, ymin, xmid, ymid);
        case 1:
            return new Quadnode(xmin, ymid, xmid, ymax);
        case 2:
            return new Quadnode(xmid, ymin, xmax, ymid);
        case 3:
            return new Quadnode(xmid, ymid, xmax, ymax);
        default:
            return NULL;
    }
}

int Quadnode::getQuad(Object * obj)
{
    if (obj.location.real < xmid)
        if (obj.location.imag < ymid)
            return 0;
        else
            return 1;
    else
        if (obj.location.imag < ymid)
            return 2;
        else
            return 3;
}

void Quadnode::addObject(Object * obj)
{
    if (isLeaf)
    {
        if (oject == NULL)
            object = obj;
        else
        {
            if (obj.location == object.location)
                return false;
            int q1 = getQuad(obj);
            int q2 = getQuad(object);
            quad[q1] = makeQuad(q1);
            if (q2 != q1)
                quad[q2] = makeQuad(q2);
            quad[q1]->addObject(obj);
            quad[q2]->addObject(object);
            object = NULL;
        }
        return true;
    }
    else
    {
        int q1 = getQuad(obj);
        if (quad[q1] == NULL)
            quad[q1] = makeQuad(q1);
        return quad[q1]->addObject(obj);
    }
}

bool Quadnode::removeObject(Object *obj)
{
    if (isLeaf)
    {
        if (object == obj)
        {
            object = NULL;
            return true;
        }
        else return false;
    }
    else
    {
        int qn = getQuad(obj);
        if (quad[qn] == NULL)
            return false;
        else
            return quad[qn]->removeObject(obj);
    }
}

