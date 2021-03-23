An Simulator for FRC robots using ROS, Gazebo, and WPILib

To-do:
- URDF for a simple tank drive robot
- figure out how to use the wpilib simulation websocket api
- 


lots of stuff taken from Triton Robotics 
https://github.com/Triton-Robotics/ROS-Simulation

the ros2d2 URDF model is taken from the ROS/Gazebo tutorials
http://wiki.ros.org/urdf_tutorial

The included Robot code is from the WPILib State Space Drive Simulation Example

Python deps:

- robotpy
- websocket-client (https://github.com/websocket-client/websocket-client)

Using onshape-to-robot to generate URDFs
https://github.com/Rhoban/onshape-to-robot

how to make generated urdfs work with ROS/Gazebo:
- make sure the parent link is called base_link
- change the urdf to a urdf.xacro
- change meshes from <mesh filename="package://file.stl"/> to <mesh filename="package://package_name/folder/file.stl"/>
= <mesh filename="package://wheel.stl"/> becomes <mesh filename="package://frc_ros_sim/my_robot/wheel.stl"/>
- change revolute joints for wheels to continuous joints
- add gazebo block to the bottom
- add transmissions

If velocity controllers aren't installed run sudo apt install ros-noetic-velocity-controllers