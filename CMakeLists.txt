cmake_minimum_required(VERSION 3.0.2)
project(frc_ros_sim)

find_package(catkin REQUIRED COMPONENTS rospy geometry_msgs std_msgs)

catkin_package(
  INCLUDE_DIRS scripts
  LIBRARIES urdf_sim_tutorial
  CATKIN_DEPENDS rospy geometry_msgs std_msgs
  DEPENDS system_lib
)

catkin_install_python(PROGRAMS 
  scripts/test_script.py 
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/scripts
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)





install(DIRECTORY config launch urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})