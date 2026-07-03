class robot :
    robot_1="Jerry"
    robot_2="Tom"

    def intro (self) :
        print ("Hi am a robot .")
        
    def name (self) :
        print("My name is",self.robot_1)

    def otherintro (self):
        print("Hi I am also a robot")

    def othername (self):
        print("My name is ",self.robot_2)

ob=robot()
ob.intro()
ob.name()
ob.otherintro()
ob.othername()

    
