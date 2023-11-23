#!/usr/bin/python

from flask import Flask, render_template
from flask import request
import rospy

from motion_transitioner_msgs.msg import GoToMotionStateActionGoal

go_to_motion_state_publisher = rospy.Publisher('/motion_state_deduction/go_to_motion_state/goal', GoToMotionStateActionGoal, queue_size=1)

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        separateStrings = next(iter(request.form.keys())).split(';')
        print(separateStrings)
        # rospy.set_param('/barman/drink_strength', int(separateStrings[1])/100.0)
        # motion_state_goal = GoToMotionStateActionGoal()
        # motion_state_goal.goal.goal_motion_state = separateStrings[0]
        # go_to_motion_state_publisher.publish(motion_state_goal)
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
    return render_template('main.html', buttons = buttons)

if __name__ == '__main__':
    # rospy.init_node('bartender')
    app.run(host= '0.0.0.0')
