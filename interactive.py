import cherrypy
import rospy
from geometry_msgs.msg import PoseStamped
from launcher import Launcher

config = {
    'global' : {
        'server.socket_host' : '192.168.3.3',
        'server.socket_port' : 8080
    }
}
class HelloWorld(object):

    def __init__(self):
        self.laucher = Launcher()

    @cherrypy.expose
    def index(self):

        # <input type="button" value="goalA" onclick="location.href='192.168.3.3:8080/goalA_to'">
        # ERIC https://github.com/VirtuosoEric/robot_web_service/blob/pn60/home.html
        
        f = open("t.html", "r")
        return f

    @cherrypy.expose
    def start_roscore(self):
        self.laucher.roslauncher()
        return 'start roscore'
    
    @cherrypy.expose
    def kill_roscore(self):
        self.laucher.kill_roscore()
        return 'kill roscore'


    @cherrypy.expose
    def goalA_to(self):
        pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)          
        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = rospy.Time.now()
        goal.pose.position.x = 0
        goal.pose.position.y = -1
        goal.pose.position.z = 0
        goal.pose.orientation.w = 1.0
        pub.publish(goal)
        return 'goal to!'
    @cherrypy.expose
    def goalA_leave(self):
        pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)          
        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = rospy.Time.now()
        goal.pose.position.x = 0
        goal.pose.position.y = 1
        goal.pose.position.z = 0
        goal.pose.orientation.w = 1.0
        pub.publish(goal)
        return 'goal leave!'
    @cherrypy.expose
    def goalB_to(self):
        # f = open("latop.html", "r")
        return 'Hello!'
    @cherrypy.expose
    def goalB_leave(self):
        # f = open("latop.html", "r")
        return 'Hello!'
    @cherrypy.expose
    def goalC_to(self):
        # f = open("latop.html", "r")
        return 'Hello!'
if __name__ == '__main__':
    # laucher = Launcher()
    # laucher.launch_roscore()
    # rospy.init_node('berry_goal', anonymous=True)
    cherrypy.quickstart(HelloWorld(), '/',config)
    