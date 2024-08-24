cmake_minimum_required(VERSION 3.15)

project(HelloWorld)

add_executable(HelloWorldEXE source/main.cpp)

target_include_directories(HelloWorldEXE PRIVATE lib)
target_link_directories(HelloWorldEXE PRIVATE lib/build )
target_link_libraries( HelloWorldEXE PRIVATE AddF)

