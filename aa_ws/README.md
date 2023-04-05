# Build and Launch Mobile Warehouse Robot and Environment in Gazebo


## Moving the Robot Autonomously


In the terminal, navigate to directory, build packages and set environment variables: 
```
cd ~/SET-BETA-SPRING2023/aa_ws/
colcon build
source install/setup.bash
```
Launch robot spawner:
```
ros2 launch warehouse_robot_spawner_pkg gazebo_world.launch.py
```
In another terminal window, launch robot controller and estimator:
```
ros2 launch warehouse_robot_controller_pkg controller_estimator.launch.py
```


## Moving the Robot Around Manually


Install the Turtlebot3 package:
```
sudo apt install ros-foxy-turtlebot3*
```
Once the turtlebot3 package is installed, we can launch the robot in the terminal:
```
ros2 launch warehouse_robot_spawner_pkg gazebo_world.launch.py
```
And in another terminal window, run this command to remap keyboard commands from the /cmd_vel topic to the /demo/cmd_vel topic:
```
ros2 run turtlebot3_teleop teleop_keyboard --ros-args --remap /cmd_vel:=/demo/cmd_vel
```
