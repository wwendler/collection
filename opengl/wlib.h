// willis wendler, 2011
// wlib.h
// containing certain classes I tend to use, such as vectors...

#ifndef VECTOR_H
#define VECTOR_H

namespace wlib
{
    class Vector
    {
        public:
            double x;
            double y;
            Vector & operator=(const Vector &);
            const Vector operator+(const Vector &);
            const Vector operator-(const Vector &);
            const Vector operator*(double);
            double magnitude();
            Vector();
    };

    class Color
    {
        public:
            unsigned char r;
            unsigned char g;
            unsigned char b;
            Color();
    };
}

#endif

