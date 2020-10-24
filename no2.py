import rospy
from std_msgs.msg import String

rospy.init_node('no2')
mat_string = String()

def subCallBack(msg):
    global mat_string
    mat_string = msg

def timerCallBack(event):
    soma = 0
    for i in range(len(mat_string.data)):
        soma = soma + int(mat_string.data[i])
    #print('somando matricula . . . ('+mat_string.data + ')')
    
    msg_soma = String()
    msg_soma.data = str(soma)
    pub.publish(msg_soma)

sub = rospy.Subscriber('/no1/mat', String, subCallBack)
pub = rospy.Publisher('no2/sum', String, queue_size=1)

timer = rospy.Timer(rospy.Duration(1), timerCallBack)

rospy.spin()