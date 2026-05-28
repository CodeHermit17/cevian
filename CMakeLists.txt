cmake_minimum_required(VERSION 3.28.3)
project(cevian LANGUAGES CXX CUDA)

# cevian is restricted to C++17
set(CMAKE_CXX_STANDARD 17)  
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CUDA_STANDARD 17)
set(CMAKE_CUDA_STANDARD_REQUIRED ON)

find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Module)

# Find nanobind cmake directory via Python
execute_process(
  COMMAND "${Python_EXECUTABLE}" -c "import nanobind; print(nanobind.cmake_dir())"
  OUTPUT_VARIABLE nanobind_cmake_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
list(APPEND CMAKE_PREFIX_PATH "${nanobind_cmake_dir}")

find_package(nanobind 2.12 CONFIG REQUIRED)

add_subdirectory(cevian)
