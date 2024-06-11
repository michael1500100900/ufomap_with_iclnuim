#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
import os

class MapPublisher:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_pub = rospy.Publisher("/camera/rgb/image_raw", Image, queue_size=10)
        self.depth_pub = rospy.Publisher("/camera/depth/image_raw", Image, queue_size=10)
        self.info_pub = rospy.Publisher("/camera/info", CameraInfo, queue_size=10)

        self.image_folder = os.path.expanduser(rospy.get_param('~image_folder', '/path/to/your/data/'))
        self.rate = rospy.Rate(1)  # 1 Hz

        # Camera calibration matrix K
        self.camera_info_msg = CameraInfo()
        self.camera_info_msg.K = [481.20, 0, 319.50, 0, -480.00, 239.50, 0, 0, 1]

    def publish_data(self):
        for i in range(882):
            img_file = os.path.join(self.image_folder, f'scene_{i:03d}.png')
            depth_file = os.path.join(self.image_folder, f'scene_{i:03d}.depth')
            info_file = os.path.join(self.image_folder, f'scene_{i:03d}.txt')

            rospy.loginfo(f"Checking files for scene {i}:")
            rospy.loginfo(f"  Image file: {img_file}")
            rospy.loginfo(f"  Depth file: {depth_file}")
            rospy.loginfo(f"  Info file: {info_file}")

            if not (os.path.exists(img_file) and os.path.exists(depth_file) and os.path.exists(info_file)):
                rospy.logwarn(f"Files for scene {i} are missing.")
                continue

            # Read image
            img = cv2.imread(img_file, cv2.IMREAD_COLOR)

            # Read depth
            with open(depth_file, 'r') as f:
                raw_data = f.read()
            depth_values = list(map(float, raw_data.split()))
            depth_array = np.array(depth_values).reshape((480, 640)).astype(np.float32)

            # Read camera info
            with open(info_file, 'r') as f:
                camera_info_data = f.readlines()

            # Update camera info from txt file (if needed)
            # Example: parsing cam_pos, cam_dir, etc.
            # ...

            # Publish RGB image
            img_msg = self.bridge.cv2_to_imgmsg(img, "bgr8")
            self.image_pub.publish(img_msg)

            # Publish Depth image
            depth_msg = self.bridge.cv2_to_imgmsg(depth_array, "32FC1")
            self.depth_pub.publish(depth_msg)

            # Publish Camera Info
            self.info_pub.publish(self.camera_info_msg)

            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('map_publisher')
    publisher = MapPublisher()
    try:
        publisher.publish_data()
    except rospy.ROSInterruptException:
        pass
