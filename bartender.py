#!/usr/bin/python

from flask import Flask, render_template
from flask import request
# import rospy

# from rocoma_msgs.srv import SwitchController

# switch_controller = rospy.ServiceProxy('/KinovaNoesisController/go_to_mode', SwitchController)
# rospy.wait_for_service('/KinovaNoesisController/go_to_mode')
print("Service available")

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(next(iter(request.form.keys())))
        # switch_controller(next(iter(request.form.keys())))
        #rospy.ServiceProxy('SwitchController', command)
    buttons = [
        {
            'text': 'Gin Tonic',
            'command': 'home_pose',
        },
        {
            'text': 'Sparkling Mint-Lime Iced Tea',
            'command': 'command_B',
        },
        {
            'text': 'Raspberry Frost Sodas',
            'command': 'command_C',
        },
        {
            'text': 'Pineapple Ginger Sparkler',
            'command': 'command_D',
        },
        {
            'text': 'Sparkling Pear Punch',
            'command': 'command_E',
        }       
    ]
    return render_template('main.html', buttons = buttons)

if __name__ == '__main__':
    app.run(host= '10.6.152.117')