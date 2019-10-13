"""A gaga ros2-launch"""

from launch import LaunchDescription
import launch.actions
import launch.substitutions
import launch_ros.actions




def generate_launch_description():
  """Launch the nodes publishing_on_tralala and melting_pot"""
  return LaunchDescription([
    launch.actions.DeclareLaunchArgument(
      'node_prefix',
      default_value=[launch.substitutions.EnvironmentVariable('USER'), '_'],
      description='prefix for node names'),
    launch_ros.actions.Node(
      package='py_simple_publishing', node_executable='publish_on_tralala', output='screen',
      node_name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'bibi_publishing_on_tralala']),
    launch_ros.actions.Node(
      package='py_heritages', node_executable='melting_pot', output='screen'),
    launch_ros.actions.Node(
      package='gogo_launch', node_executable='simplet_z', output='screen'),
  ])

