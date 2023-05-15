cmake_minimum_required(VERSION 3.15)
project(dkm CXX)




add_library(dkm src/dkm.cpp)
target_include_directories(dkm PUBLIC include)



set_target_properties(dkm PROPERTIES PUBLIC_HEADER "include/dkm.h")
install(TARGETS dkm)
