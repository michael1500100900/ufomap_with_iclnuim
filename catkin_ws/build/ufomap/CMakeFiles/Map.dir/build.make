# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /root/catkin_ws/src/ufomap/ufomap

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/catkin_ws/build/ufomap

# Include any dependencies generated for this target.
include CMakeFiles/Map.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Map.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Map.dir/flags.make

CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.o: CMakeFiles/Map.dir/flags.make
CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.o: /root/catkin_ws/src/ufomap/ufomap/src/geometry/bounding_volume.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/catkin_ws/build/ufomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.o -c /root/catkin_ws/src/ufomap/ufomap/src/geometry/bounding_volume.cpp

CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/catkin_ws/src/ufomap/ufomap/src/geometry/bounding_volume.cpp > CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.i

CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/catkin_ws/src/ufomap/ufomap/src/geometry/bounding_volume.cpp -o CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.s

CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.o: CMakeFiles/Map.dir/flags.make
CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.o: /root/catkin_ws/src/ufomap/ufomap/src/geometry/collision_checks.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/catkin_ws/build/ufomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.o -c /root/catkin_ws/src/ufomap/ufomap/src/geometry/collision_checks.cpp

CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/catkin_ws/src/ufomap/ufomap/src/geometry/collision_checks.cpp > CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.i

CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/catkin_ws/src/ufomap/ufomap/src/geometry/collision_checks.cpp -o CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.s

CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.o: CMakeFiles/Map.dir/flags.make
CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.o: /root/catkin_ws/src/ufomap/ufomap/src/map/occupancy_map_color.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/catkin_ws/build/ufomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.o -c /root/catkin_ws/src/ufomap/ufomap/src/map/occupancy_map_color.cpp

CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/catkin_ws/src/ufomap/ufomap/src/map/occupancy_map_color.cpp > CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.i

CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/catkin_ws/src/ufomap/ufomap/src/map/occupancy_map_color.cpp -o CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.s

CMakeFiles/Map.dir/src/map/occupancy_map.cpp.o: CMakeFiles/Map.dir/flags.make
CMakeFiles/Map.dir/src/map/occupancy_map.cpp.o: /root/catkin_ws/src/ufomap/ufomap/src/map/occupancy_map.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/catkin_ws/build/ufomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/Map.dir/src/map/occupancy_map.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Map.dir/src/map/occupancy_map.cpp.o -c /root/catkin_ws/src/ufomap/ufomap/src/map/occupancy_map.cpp

CMakeFiles/Map.dir/src/map/occupancy_map.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Map.dir/src/map/occupancy_map.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/catkin_ws/src/ufomap/ufomap/src/map/occupancy_map.cpp > CMakeFiles/Map.dir/src/map/occupancy_map.cpp.i

CMakeFiles/Map.dir/src/map/occupancy_map.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Map.dir/src/map/occupancy_map.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/catkin_ws/src/ufomap/ufomap/src/map/occupancy_map.cpp -o CMakeFiles/Map.dir/src/map/occupancy_map.cpp.s

# Object files for target Map
Map_OBJECTS = \
"CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.o" \
"CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.o" \
"CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.o" \
"CMakeFiles/Map.dir/src/map/occupancy_map.cpp.o"

# External object files for target Map
Map_EXTERNAL_OBJECTS =

libMap.so.1.0.0: CMakeFiles/Map.dir/src/geometry/bounding_volume.cpp.o
libMap.so.1.0.0: CMakeFiles/Map.dir/src/geometry/collision_checks.cpp.o
libMap.so.1.0.0: CMakeFiles/Map.dir/src/map/occupancy_map_color.cpp.o
libMap.so.1.0.0: CMakeFiles/Map.dir/src/map/occupancy_map.cpp.o
libMap.so.1.0.0: CMakeFiles/Map.dir/build.make
libMap.so.1.0.0: CMakeFiles/Map.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/root/catkin_ws/build/ufomap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX shared library libMap.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Map.dir/link.txt --verbose=$(VERBOSE)
	$(CMAKE_COMMAND) -E cmake_symlink_library libMap.so.1.0.0 libMap.so.1 libMap.so

libMap.so.1: libMap.so.1.0.0
	@$(CMAKE_COMMAND) -E touch_nocreate libMap.so.1

libMap.so: libMap.so.1.0.0
	@$(CMAKE_COMMAND) -E touch_nocreate libMap.so

# Rule to build all files generated by this target.
CMakeFiles/Map.dir/build: libMap.so

.PHONY : CMakeFiles/Map.dir/build

CMakeFiles/Map.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Map.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Map.dir/clean

CMakeFiles/Map.dir/depend:
	cd /root/catkin_ws/build/ufomap && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/catkin_ws/src/ufomap/ufomap /root/catkin_ws/src/ufomap/ufomap /root/catkin_ws/build/ufomap /root/catkin_ws/build/ufomap /root/catkin_ws/build/ufomap/CMakeFiles/Map.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Map.dir/depend

