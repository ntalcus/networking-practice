# This is a personal learning program, not really intended to be a display of any sort of end product. 
# Author: Noah Alcus
# I started working on it prior to reading a book about networking to help brainstorm some of the issues and 
# hurdles that might arise in networking. Without the background, it definitely confused me a bit to consider
# what might happen in various edge cases. This simple program amounts to a circuit-switched network more than 
# anything else and really isn't even a representation of TCP so don't use this as a model for your own learning.
# Cheers!

class Router:

    def __init__(self, name):
        self.known_hosts = {}
        self.name = name

    def addHost(self, name, sender):
        if name in self.known_hosts:
            print(name, " already in use, please try another.")
        else:
            self.known_hosts[name] = sender
            print(self.known_hosts)

    def transmitMessage(self, targetName, senderName, message):
        if targetName not in self.known_hosts:
            return False
        receiver = self.known_hosts[targetName]
        response = receiver.receiveMessage(senderName, message)
        return response
        

    def queryStatus(self, targetName, senderName):
        if not self.confirmHost(targetName) or not self.confirmHost(senderName):
            return False
        receiver = self.known_hosts[targetName]
        status = receiver.confirmConnection(senderName)
        if status:
            print(f"{senderName} is connected to {targetName}")
            return True
        else:
            print(f"{senderName} is *NOT* connected to {targetName}, query failed.")
            return False

    def establishConnection(self, senderName, targetName):
        sender = self.known_hosts[senderName]
        target = self.known_hosts[targetName]
        sender.setConnection(targetName)
        target.setConnection(senderName)
        return True

    def confirmHost(self, host):
        print(host)
        if host in self.known_hosts:
            return True
        else:
            print(f"{host} is not known by router {self.name}.")
            return False
    

    
class EndSystem:

    def __init__(self, name):
        self.name = name
        self.currentConnection = None
    
    def establishConnection(self, targetName, router):
        if not router.confirmHost(self.name) or not router.confirmHost(targetName):
            print(f"Connection not established between {self.name} and {targetName}.")
            return False
        # response = router.queryStatus(targetName, self.name)
        # if not response:
        #     print("Cannot establish connection.")
        #     return False
        # else:
        router.establishConnection(self.name, targetName)
        print(f"Connection established from {self.name} with {targetName}.")
        return True
    
    def setConnection(self, name):
        self.currentConnection = name

    def sendMessage(self, targetName, router, message):
        # This is not correct and I should change it so that the sender is checked on reception
        if not self.confirmConnection(targetName):
            print(f"Message not sent between {self.name} and {targetName}.")
            return False
        response = router.transmitMessage(targetName, self.name, message)
        return response

    def receiveMessage(self, senderName, message):
        print(f"Aww, sick, {senderName} send me the message '{message}''.")
        
    
    def confirmConnection(self, senderName):
        return self.currentConnection == senderName
        
    def endConnection(self):
        self.currentConnection = None 


    def registerSelf(self, router):
        router.addHost(self.name, self)
        print(f"Device {self.name} registered to router {router.name}.")
        return True

router = Router("yeet-master-1337")
host1 = EndSystem("yoot-lover-462")
host2 = EndSystem("golden-dog")
router.addHost(host1.name, host1)

# these should all fail (host 2 not registered)
print("failing connection and message")
host1.establishConnection(host2.name, router)
host1.sendMessage(host2.name, router, "I cannot quite yet yote my dude")
router.addHost(host2.name, host2)


# this should also fail as host1 and host2 are not connected
print("failing message")
host1.sendMessage(host2.name, router, "yeet we will soon my dude, but not yet")

# host1 establishes connection and sends message
print("functional connection and message")
host1.establishConnection(host2.name, router)
host1.sendMessage(host2.name, router, "dareth I presume that thou has yoton'd my yote?")