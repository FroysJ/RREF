cmake_minimum_required(VERSION 3.28)
project(RREF)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_VERBOSE_MAKEFILE ON)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

add_executable(RREF main.cpp Solution.cpp Rat.cpp)
target_link_libraries(RREF PRIVATE ${Python3_LIBRARIES})
target_include_directories(RREF PRIVATE ${Python3_INCLUDE_DIRS})