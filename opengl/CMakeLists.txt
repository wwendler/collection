# seeing if I can get cmake + sdl + opengl working
cmake_minimum_required (VERSION 2.6)
project (GLTESTPROJECT)

#see /usr/local/share/cmake-2.6/Modules/Find*.cmake for more examples
find_package(OpenGL REQUIRED)
find_package(SDL REQUIRED)
find_package(SDL_image REQUIRED)

include_directories(${SDL_INCLUDE_DIR})
include_directories(${SDLIMAGE_INCLUDE_DIR})

add_executable(gltest test.cpp)
target_link_libraries(gltest m ${OPENGL_LIBRARY} ${SDL_LIBRARY} ${SDLIMAGE_LIBRARY})
