nanobind_add_module(_core _core.cpp)
target_include_directories(_core PRIVATE ${CMAKE_SOURCE_DIR}/include)


# Output directly into the Python package directory
set_target_properties(_core PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/cevian
)