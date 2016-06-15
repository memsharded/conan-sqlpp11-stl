PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
add_definitions(-std=c++11)
ADD_EXECUTABLE(example SampleTest.cpp)
TARGET_LINK_LIBRARIES(example ${CONAN_LIBS})
