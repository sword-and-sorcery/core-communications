cmake_minimum_required(VERSION 2.8.12)
project(sword_and_sorcery)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(SOURCES src/communications.cpp)
# set(HEADERS include/communications.h)

add_library(communications ${SOURCES})
set_target_properties(communications PROPERTIES CXX_STANDARD 17)
target_link_libraries(communications PUBLIC CONAN_PKG::core-messages)

target_include_directories(
    communications PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)
