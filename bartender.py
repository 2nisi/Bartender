#!/usr/bin/python

from flask import Flask, request, render_template
import rospy
import time

from motion_transitioner_msgs.msg import GoToMotionStateActionGoal

go_to_motion_state_publisher = rospy.Publisher('/motion_state_deduction/go_to_motion_state/goal', GoToMotionStateActionGoal, queue_size=1)

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route("/", methods=['GET', 'POST'])
def index():

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
        separateStrings = next(iter(request.form.keys())).split(';')
        print(separateStrings)
        # rospy.set_param('/barman/drink_strength', int(separateStrings[1])/100.0)
        # motion_state_goal = GoToMotionStateActionGoal()
        # motion_state_goal.goal.goal_motion_state = separateStrings[0]
        # go_to_motion_state_publisher.publish(motion_state_goal)

    # Is being excecuted when a GET method is detected
    if request.method == 'GET':
        print('inside GET')

        # Checks if the glass is being detected
        if(request.args.get('robot_status') == 'undetected_glass'):
            print('undetected glass')

            if next(iter(request.form.keys())) == 'return_main':
                print('return to main page')
                return render_template('main.html', buttons = buttons)
            return render_template('no_glass_available.html')

        # Runs while the robot is serving
        elif(request.args.get('robot_status') == 'busy'):
            print('robot is busy')
            return render_template('robot_serving.html')
            while reguest.args.get('robot_status') == 'busy':
                time.sleep(2) # (seconds) Wait before the next robot status udpate

    # Renders the main page, landing page.
    return render_template('main.html', buttons = buttons)

if __name__ == '__main__':
    # rospy.init_node('bartender')
    app.run(host= '0.0.0.0')
