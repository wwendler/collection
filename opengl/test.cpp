// based on code found here: http://gpwiki.org/index.php/SDL:Tutorials:Using_SDL_with_OpenGL
// Willis Wendler

#include "SDL.h"
#include "SDL_opengl.h"
#include <stdlib.h>
#include <math.h>

GLuint genTexture(SDL_Surface *surface)
{
    GLuint texture;
    GLenum texture_format;
    GLint nOfColors;

    // Check that the image's width is a power of 2
    if ( (surface->w & (surface->w - 1)) != 0 ) {
        printf("warning: image.bmp's width is not a power of 2\n");
    }
    // Also check if the height is a power of 2
    if ( (surface->h & (surface->h - 1)) != 0 ) {
        printf("warning: image.bmp's height is not a power of 2\n");
    }
    // get the number of channels in the SDL surface
    nOfColors = surface->format->BytesPerPixel;
    if (nOfColors == 4)     // contains an alpha channel
    {
        if (surface->format->Rmask == 0x000000ff)
            texture_format = GL_RGBA;
        else
            texture_format = GL_BGRA;
    }
    else if (nOfColors == 3)     // no alpha channel
    {
        if (surface->format->Rmask == 0x000000ff)
            texture_format = GL_RGB;
        else
            texture_format = GL_BGR;
    }
    else
    {
        printf("warning: the image is not truecolor..  this will probably break\n");
        return 0;
    }

    // create texture
    printf("gl create texture\n");
    glGenTextures(1, &texture);
    // bind texture??
    printf("gl bind texture\n");
    glBindTexture(GL_TEXTURE_2D, texture);
    // set scaling properties
    printf("gl param texture\n");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR); 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    // give texture data from sdl surface
    printf("gl tex image\n");
    glTexImage2D(GL_TEXTURE_2D, 0, nOfColors, surface->w, surface->h, 0,
            texture_format, GL_UNSIGNED_BYTE, surface->pixels);
    return texture;
}

void drawPoly(int n_side, float x, float y, float r, GLuint texture)
{
    int n;
    float xx, yy, theta;
    glBindTexture(GL_TEXTURE_2D, texture);
    glBegin(GL_POLYGON);
    for (n = 0; n < n_side; n++)
    {
        theta = n*2.0*M_PI/n_side;
        xx = x + r*cos(theta);
        yy = y + r*sin(theta);
        glTexCoord2f(cos(theta), sin(theta));
        glVertex2f(xx, yy);
    }
    glEnd();
}

int main()
{
    // initialize sdl
    int init_flags = SDL_INIT_VIDEO | SDL_INIT_TIMER;
    int sdl_flags = SDL_OPENGL;// | SDL_FULLSCREEN;
    if (SDL_Init(init_flags) != 0)
    {
        fprintf(stderr, "Error initializing SDL: %s\n", SDL_GetError());
        return 1;
    }
    atexit(SDL_Quit);
    SDL_EnableKeyRepeat(0, 0);
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);
    SDL_Surface *screen = SDL_SetVideoMode(640, 480, 16, sdl_flags);

    // initialize opengl
    glEnable(GL_TEXTURE_2D);
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
    glViewport(0, 0, 640, 480);
    glClear(GL_COLOR_BUFFER_BIT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0f, 640, 480, 0.0f, -1.0f, 1.0f);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    // load images
    printf("loading images\n");
    SDL_Surface *img = SDL_LoadBMP("trollface.bmp");
    if (img == NULL)
    {
        printf("image load fail :(\n");
        exit(1);
    }
    printf("creating textures\n");
    GLuint texture = genTexture(img);
    //drawSquare(10, 10, 200, texture);
    printf("drawing images\n");
    drawPoly(7, 200.0, 200.0, 100.0, texture);
    SDL_GL_SwapBuffers();
    SDL_Event event;
    char * keyname;
    while(true)
    {
        //printf("starting event loop...\n");
        while(SDL_PollEvent(&event) == 1)
        {
            switch(event.type)
            {
                case SDL_KEYDOWN:
                    keyname = SDL_GetKeyName(event.key.keysym.sym);
                    if (event.key.keysym.sym == SDLK_q)
                        exit(0);
                    printf("key %s pressed.\n",
                            keyname);
                    break;
                case SDL_KEYUP:
                    keyname = SDL_GetKeyName(event.key.keysym.sym);
                    printf("key %s released.\n", keyname);
                    break;
                case SDL_MOUSEMOTION:
                    printf("lololol\n");
                    break;
                default:
                    printf("other event\n");
            }
        }
        SDL_Delay(200);
        SDL_GL_SwapBuffers();
    }
}
