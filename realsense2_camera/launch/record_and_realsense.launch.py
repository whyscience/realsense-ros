# 文件名：record_and_realsense.launch.py

import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 获取 realsense2_camera 的 launch 文件路径
    realsense_launch_dir = get_package_share_directory('realsense2_camera')
    realsense_launch_file = os.path.join(realsense_launch_dir, 'launch', 'rs_launch.py')

    return LaunchDescription([
        # 包含 realsense2_camera 的 launch 文件
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(realsense_launch_file),
            launch_arguments={}
        ),

        # 启动 ros2 bag record 命令
        ExecuteProcess(
            cmd=[
                'ros2', 'bag', 'record', 
                '/camera/camera/imu',
                '/camera/camera/color/image_raw',
                '/camera/camera/aligned_depth_to_color/image_raw',
                '--compression-format', 'zstd',
                '--compression-mode', 'file'
            ],
            output='screen'
        )
    ])

