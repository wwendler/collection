// based on code found here: http://gpwiki.org/index.php/SDL:Tutorials:Using_SDL_with_OpenGL
// Willis Wendler
#include "SDL.h"
#include "SDL_opengl.h"

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
    glGenTextures(1, &texture);
    // bind texture??
    glBindTexture(GL_TEXTURE_2D, texture);
    // set scaling properties
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR); 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    // give texture data from sdl surface
    glTexImage2D(GL_TEXTURE_2D, 0, nOfColors, surface->w, surface->h, 0,
            texture_format, GL_UNSIGNED_BYTE, surface->pixels);
    return texture;
}

void drawSquare(float x, float y, float s, GLuint texture)
{
    glBindTexture(GL_TEXTURE_2D, texture);
    glBegin(GL_QUADS);
    glTexCoord2i( 0, 0 );
    glVertex3f( 100.f, 100.f, 0.0f );
    glTexCoord2i( 1, 0 );
    glVertex3f( 228.f, 100.f, 0.f );
    glTexCoord2i( 1, 1 );
    glVertex3f( 228.f, 228.f, 0.f );
    glTexCoord2i( 0, 1 );
    glVertex3f( 100.f, 228.f, 0.f );
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
    SDL_Surface *img = SDL_LoadBMP("texture.bmp");
    GLuint texture = genTexture(img);
    drawSquare(10, 10, 200, texture);
    SDL_GL_SwapBuffers();
    SDL_Event event;
    char * keyname;
    while(true)
    {
        while(SDL_PollEvent(&event));
        {
            switch(event.type)
            {
                case SDL_KEYDOWN:
                    keyname = SDL_GetKeyName(event.key.keysym.sym);
                    if (keyname[0] == 'q')
                        exit(0);
                    printf("key %s pressed.\n", keyname);
                    break;
                case SDL_KEYUP:
                    keyname = SDL_GetKeyName(event.key.keysym.sym);
                    printf("key %s released.\n", keyname);
                    break;
            }
        }
        SDL_Delay(100);
    }
    SDL_Quit();
}
