from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    '''
    ld= LaunchDescription()

    talker_node= Node(
        package= "lab1_pkg",
        executable= "talker.py",
        namespace= "talker",
        parameters= [
                {"v": 3.0},
                {"d": 4.0}
            ]
    )

    listener_node= Node(
        package= "lab1_pkg",
        executable= "relay.py",
        namespace= "relay",
    )
    ld.add_action(talker_node)
    ld.add_action(listener_node)
    return ld
    '''
    return LaunchDescription([
        Node(
            package='lab1_pkg',
            namespace='talker',
            executable='talker.py',
            name='sim_talker',
            parameters= [
                {"v": 3.0},
                {"d": 4.0}
            ]
        ),
        Node(
            package='lab1_pkg',
            namespace='relay',
            executable='relay.py',
            name='sim2'
        ),
    ])