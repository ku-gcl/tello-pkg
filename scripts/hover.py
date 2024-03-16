import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Quaternion
from ros_tello.Command as Command


def mocap_cb(msg):
    global visp_pub
    state = PoseStamped()
    state.pose.pose.position.x = msg.pose.position.x
    state.pose.pose.position.y = msg.pose.position.y
    state.pose.pose.position.z = msg.pose.position.z
    state.pose.pose.orientation.x = msg.pose.orientation.x
    state.pose.pose.orientation.y = msg.pose.orientation.y
    state.pose.pose.orientation.z = msg.pose.orientation.z
    state.pose.pose.orientation.w = msg.pose.orientation.w
    visp_pub.publish(state)

rospy.init_node('tello_node', anonymous=True)


# TODO: Typeを入れること
mocap_sub = rospy.Subscriber("/mocap_node/Robot_1/pose", Type, mocap_cb)
visp_pub = rospy.Publisher("/tello/vision_pose/pose", Type, queue_size=1)
# traj_pub = rospy.Publisher("/tello/trajectory/pose", Type, queue_size=1)
# sp_sub = rospy.Subscriber("/tello/setpoint_position/relative", Type, callback)




# TODO: Telloに接続するコード
# Tello側のローカルIPアドレス(デフォルト)、宛先ポート番号(コマンドモード用)
# TELLO_IP = '192.168.10.1'
# TELLO_PORT = 8889

# cmd = Command(TELLO_IP, TELLO_PORT)

# cmd.takefoff()
# cmd.up(10)
# cmd.land()




# ##############

# # ROS
# start_time = rospy.Time.now()
# duration = 20.0
# rate = rospy.Rate(20.0)

# rospy.loginfo("Start autonomous control mode...")
# while (not rospy.is_shutdown() 
#         and (rospy.Time.now() - start_time) < rospy.Duration(duration)):
    
#     # generate trajectory
#     # time_sec = (rospy.Time.now() - start_time).to_sec()
#     # x, y, z = trajectory.circle(time_sec=time_sec, radius=radius, altitude=altitude)
    
#     # desired position
#     xd = 1.0
#     yd = 0.5
#     zd = 1.0
    
#     # current position
#     x = 0
#     y = 0
#     z = 0
    
#     # calculate position error and convert meter to cm 
#     ex = (x - xd) * 100
#     ey = (y - yd) * 100
#     ez = (z - zd) * 100
    
#     # Move Tello

#     rate_ctrl.sleep()


# # TODO: 着陸


