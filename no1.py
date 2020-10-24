import rospy
from std_msgs.msg import String

rospy.init_node('no1')
soma_string = String()

def subCallBack(msg):
    global soma_string
    soma_string = msg

def timerCallBack(event):
    msg = String()
    msg.data = '2017001160'
    pub.publish(msg)
    
    print('Resultado da soma dos digitos da matricula: '+soma_string.data)
    

sub = rospy.Subscriber('/no2/sum', String, subCallBack)
pub = rospy.Publisher('no1/mat', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)

rospy.spin()