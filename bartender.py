#!/usr/bin/python

from flask import Flask, request, render_template
from flask_socketio import SocketIO
import rospy
import time

from motion_transitioner_msgs.msg import GoToMotionStateActionGoal

go_to_motion_state_publisher = rospy.Publisher('/motion_state_deduction/go_to_motion_state/goal', GoToMotionStateActionGoal, queue_size=1)

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

dynaarmState = "idle"

@app.route("/", methods=['GET', 'POST'])
def index():
    global dynaarmState

    # All possible drinks are defined here
    buttons = [
        {
            'text': 'Gin & Tonic',
            'command': 'gin_tonic',
        },
        {
            'text': 'Gin & Matte',
            'command': 'gin_matte',
        },
        {
            'text': 'Vodka & Matte',
            'command': 'vodka_matte',
        },
        {
            'text': 'Vodka & Cola',
            'command': 'vodka_cola',
        },
        {
            'text': 'Rum & Cola',
            'command': 'rum_cola',
        },
    ]
    if request.method == 'POST':
        if next(iter(request.form.keys())) == 'rstatus_check':
            print('checking robot status')
            if dynaarmState == "idle":
                return render_template('main.html', buttons = buttons)
            if dynaarmState == "bottle_empty":
                return render_template('bottle_empty.html', buttons = buttons)
            elif dynaarmState == "busy":
                return render_template('robot_serving.html')
            elif dynaarmState == "undetected_glass":
                return render_template('no_glass_available.html')
        elif next(iter(request.form.keys())) == 'return_main':
            print('return to main page')
            return render_template('main.html', buttons = buttons)
        else:
            separateStrings = next(iter(request.form.keys())).split(';')
            print(separateStrings)
            dynaarmState = "busy"
            rospy.set_param('/barman/drink_strength', int(separateStrings[1])/100.0)
            motion_state_goal = GoToMotionStateActionGoal()
            motion_state_goal.goal.goal_motion_state = separateStrings[0]
            go_to_motion_state_publisher.publish(motion_state_goal)
            return render_template('robot_serving.html')

    # Is being excecuted when a GET method is detected
    if request.method == 'GET':
        print('inside GET')
        if(request.args.get('undetected_glass')):
            print('undetected glass')
            dynaarmState = "undetected_glass"
        elif(request.args.get('bottle_empty')):
            print('bottle empty')
            dynaarmState = "bottle_empty"
        elif(request.args.get('busy')):
            print('robot is busy')
            dynaarmState = "busy"
        elif(request.args.get('idle')):
            print('robot is idle')
            dynaarmState = "idle"

    # Renders the main page, landing page.
    print('rendering main page')
    return render_template('main.html', buttons = buttons)

if __name__ == '__main__':
    rospy.init_node('bartender')
    app.run(host= '0.0.0.0')
