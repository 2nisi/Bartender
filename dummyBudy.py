# ROS Node with HTTP Server
import rospy
from std_msgs.msg import String
from http.server import BaseHTTPRequestHandler, HTTPServer

# triggered = False

# def publish_message():
#     rospy.init_node('trigger_publisher', anonymous=True)
#     pub = rospy.Publisher('trigger_topic', String, queue_size=10)
#     rate = rospy.Rate(10)  # 10 Hz
#     print("Trigger publisher started")
#     message = "Trigger message"
#     rospy.loginfo(message)
#     pub.publish(message)
#     # Make an HTTP request to the Flask application
#     make_http_request()
#     triggered = True

#     # while not rospy.is_shutdown():
#     #     if not should_trigger():
#     #         message = "Trigger message"
#     #         rospy.loginfo(message)
#     #         pub.publish(message)
#     #         # Make an HTTP request to the Flask application
#     #         make_http_request()
#     #         triggered = True
#     #     rate.sleep()

# def should_trigger():
#     # Implement your condition here
#     return triggered

def make_http_request():
    # Make an HTTP request to the Flask application
    print("Making HTTP request")
    import urllib.request
    url = 'http://127.0.0.1:5000/'  # Change thargument_valuee URL to match your Flask app
    params = {'busy': True}
    url = url + '?' + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        # rospy.loginfo(html.decode('utf-8'))


# def arm_state_callback(data):
#     print('inside GET')

#     # Checks if the glass is being detected
#     if(data == 'undetected_glass'):
#         print('undetected glass')
#         return render_template('no_glass_available.html')
#     # Runs while the robot is serving
#     elif(data == 'busy'):
#         print('robot is busy')
#         return render_template('robot_serving.html')
#     else:
#         return render_template('main.html', buttons = buttons)

# arm_state_subscriber = rospy.Subscriber('/bartender/result', String, arm_state_callback)

if __name__ == '__main__':
    # rospy.init_node('bartender_bridge')
    try:
        print("Starting trigger publisher")
        # start_http_server()
        print("Starting HTTP server")
        make_http_request()
    except rospy.ROSInterruptException:
        pass