#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

class BartenderBridge(object):

    def __init__(self):
        rospy.Subscriber("/bartender/state", String, self.bartender_state_callback)

    def bartender_state_callback(self, msg):
        if msg.data == "idle":
            self.make_http_request("idle")
        elif msg.data == "busy":
            self.make_http_request("busy")
        elif msg.data == "undetected_glass":
            self.make_http_request("undetected_glass")
        elif msg.data == "bottle_empty":
            self.make_http_request("bottle_empty")

    def make_http_request(self, state):
        # Make an HTTP request to the Flask application
        print("Making HTTP request")
        import urllib.request
        url = 'http://127.0.0.1:5000/'  # Change thargument_valuee URL to match your Flask app
        params = {state: True}
        url = url + '?' + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url) as response:
            html = response.read()

if __name__ == '__main__':
    rospy.init_node('bartender_bridge')
    rospy.loginfo("Bartender Bridge Started")
    bartender_bridge = BartenderBridge()
    rospy.spin()
