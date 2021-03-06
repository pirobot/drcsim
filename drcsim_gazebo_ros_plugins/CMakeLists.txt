cmake_minimum_required(VERSION 2.8.3)
project(drcsim_gazebo_ros_plugins)
set(CMAKE_BUILD_TYPE "RelWithDebInfo")

# Check for 32/64 bits support
STRING (REGEX MATCH "Linux" LINUX ${CMAKE_SYSTEM_NAME})
STRING (REGEX MATCH "BSD" BSD ${CMAKE_SYSTEM_NAME})

if (NOT DEFINED USE_ATLASSIMINTERFACE_BLOB)
  if (LINUX)
    # Check for 64bits machines
    if(CMAKE_SIZEOF_VOID_P EQUAL 8)
      set(USE_ATLASSIMINTERFACE_BLOB True)
    else()
      set(USE_ATLASSIMINTERFACE_BLOB False)
      message(FATAL_ERROR "WARNING: AtlasSIMINTERFACE binary will *NOT* be used in 32 bits systems. If you want to use DRCSim without the AtlasSimInterface binary interface, run cmake with -DUSE_ATLASSIMINTERFACE_BLOB:BOOL=False")
    endif() 
  elseif(BSD)
    message(STATUS "Warning: system check for 32/64 bit is not implemented for")
    message(STATUS "Warning: BSD system, assuming 64bit machine. Please use")
    message(STATUS "Warning: please use USE_ATLASSIMINTERFACE_BLOB flag if you want")
    message(STATUS "Warning: not to use 64 bits AtlasSIMINTERFACE library")
    set(USE_ATLASSIMINTERFACE_BLOB True)
  endif()
endif()

set(ATLAS_INTERFACE_PROJECT_PATH "${PROJECT_SOURCE_DIR}/../drcsim_model_resources/AtlasSimInterface_1.1.1")

find_package(catkin REQUIRED COMPONENTS
             drcsim_model_resources
             drcsim_gazebo_plugins
             osrf_msgs
             sandia_hand_msgs
             actionlib
             roscpp
             std_msgs
             sensor_msgs
             geometry_msgs
             trajectory_msgs
             control_msgs
             image_transport
             tf
             actionlib
             atlas_msgs
             handle_msgs
             gazebo_plugins
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES drcsim_gazebo_ros_plugins
  CATKIN_DEPENDS gazebo_plugins
#  DEPENDS system_lib
)

find_package(gazebo REQUIRED)

###########
## Build ##
###########

if (USE_ATLASSIMINTERFACE_BLOB)
  add_definitions(-DWITH_ATLASSIMINTERFACE_BLOB=1)
endif()

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${PROJECT_SOURCE_DIR}/include
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)

link_directories(
  ${GAZEBO_LIBRARY_DIRS}
)

## Declare a cpp library
add_library(VRCPlugin src/VRCPlugin.cpp)
add_dependencies(VRCPlugin atlas_msgs_gencpp)
target_link_libraries(VRCPlugin ${catkin_LIBRARIES})

add_library(SandiaHandPlugin src/SandiaHandPlugin.cpp)
target_link_libraries(SandiaHandPlugin ${catkin_LIBRARIES})
add_dependencies(SandiaHandPlugin atlas_msgs_gencpp)

#add_library(IRobotHandPlugin src/IRobotHandPlugin.cpp)
#set_target_properties(IRobotHandPlugin PROPERTIES LINK_FLAGS "${ld_flags}")
#set_target_properties(IRobotHandPlugin PROPERTIES COMPILE_FLAGS "${cxx_flags}")
#target_link_libraries(IRobotHandPlugin ${catkin_LIBRARIES})
#add_dependencies(IRobotHandPlugin handle_msgs_gencpp atlas_msgs_gencpp)

add_library(MultiSenseSLPlugin src/MultiSenseSLPlugin.cpp)
target_link_libraries(MultiSenseSLPlugin ${catkin_LIBRARIES})

add_library(DRCVehicleROSPlugin src/DRCVehicleROSPlugin.cpp)
target_link_libraries(DRCVehicleROSPlugin ${catkin_LIBRARIES})
add_dependencies(DRCVehicleROSPlugin DRCVehiclePlugin)

add_library(ContactModelPlugin src/ContactModelPlugin.cpp)
target_link_libraries(ContactModelPlugin ${catkin_LIBRARIES})

add_library(AtlasPlugin src/AtlasPlugin.cpp)
set_target_properties(AtlasPlugin PROPERTIES LINK_FLAGS "-L${ATLAS_INTERFACE_PROJECT_PATH}/lib64/")
set_target_properties(AtlasPlugin PROPERTIES COMPILE_FLAGS "-I${ATLAS_INTERFACE_PROJECT_PATH}/include")
if (USE_ATLASSIMINTERFACE_BLOB)
  target_link_libraries(AtlasPlugin ${catkin_LIBRARIES} AtlasSimInterface)
endif()
add_dependencies(AtlasPlugin atlas_msgs_gencpp AtlasSimInterface_include AtlasSimInterface_lib)

add_library(VRCScoringPlugin src/VRCScoringPlugin.cc)
target_link_libraries(VRCScoringPlugin ${catkin_LIBRARIES})
add_dependencies(VRCScoringPlugin atlas_msgs_gencpp)

add_library(test_ros_plugin src/test_ros_plugin.cc)
target_link_libraries(test_ros_plugin ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})

### executables, utilities for debugging atlas simulation, should not depend on gazebo
add_executable(pub_atlas_joint_trajectory_test src/pub_atlas_joint_trajectory_test.cpp)
target_link_libraries(pub_atlas_joint_trajectory_test ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})

add_executable(pub_joint_states src/pub_joint_states.cpp)
target_link_libraries(pub_joint_states ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})
add_dependencies(pub_joint_states atlas_msgs_gencpp)

add_executable(pub_joint_commands src/pub_joint_commands.cpp)
target_link_libraries(pub_joint_commands ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})
add_dependencies(pub_joint_commands osrf_msgs_gencpp)

add_executable(pub_atlas_state src/pub_atlas_state.cpp)
target_link_libraries(pub_atlas_state ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})
add_dependencies(pub_atlas_state atlas_msgs_gencpp)

add_executable(pub_atlas_command_fast src/pub_atlas_command_fast.cpp)
target_link_libraries(pub_atlas_command_fast ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})
add_dependencies(pub_atlas_command_fast atlas_msgs_gencpp)

add_executable(pub_atlas_command src/pub_atlas_command.cpp)
target_link_libraries(pub_atlas_command ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})
add_dependencies(pub_atlas_command atlas_msgs_gencpp)

add_executable(gz_model_teleport src/gz_model_teleport.cpp)
target_link_libraries(gz_model_teleport ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})

## example actionlib implementation
add_executable(actionlib_server src/actionlib_server.cpp)
target_link_libraries(actionlib_server ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})
add_dependencies(actionlib_server atlas_msgs_gencpp) # or atlas_msgs_generate_messages_cpp)

#############
## Install ##
#############
# IRobotHandPlugin 
install(TARGETS VRCPlugin SandiaHandPlugin MultiSenseSLPlugin DRCVehicleROSPlugin ContactModelPlugin AtlasPlugin VRCScoringPlugin test_ros_plugin pub_atlas_joint_trajectory_test pub_joint_states pub_joint_commands pub_atlas_state pub_atlas_command_fast pub_atlas_command gz_model_teleport actionlib_server
  DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}/${PROJECT_NAME}/plugins/
)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
  PATTERN ".svn" EXCLUDE
)
