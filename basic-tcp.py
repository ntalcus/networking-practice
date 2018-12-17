class Router:

    def __init__(self, name):
        self.known_hosts = {}
        self.name = name

    def addHost(self, name, sender):
        if name in self.known_hosts:
            print(name, " already in use, please try another.")
        else:
            self.known_hosts[name] = sender

    def transmitMessage(self, targetName, senderName, message):
        receiver = self.known_hosts[targetName]
        receiver.receiveMessage(self.name, senderName, message)
        

    def queryStatus(self, targetName, senderName):
        if not self.confirmHost(targetName) or not confirmHost(senderName):
            return False
        receiver = self.known_hosts[targetName]
        status = receiver.confirmConnection(senderName)
        if status:
            print(f"{senderName} is connected to {targetName}")
            return True:
        else:
            print(f"{senderName} is *NOT* connected to {targetName}, query failed.")
            return False


    def confirmHost(self, host):
        if sender in known_hosts:
            return True
        else:
            print(f"{host} is not known by router {self.name}.")
            return False

    
class EndSystem:

    def __init__(self, name):
        self.name = name
    
    def establishConnection(self, targetName, router):
        if not router.confirmHost(self.name) or not router.confirmHost(targetName):
            print("Connection not established between {self.name} and {targetName}.")
            return False
        response = router.queryStatus(targetName, self)
        if not response:
            print("Cannot establish connection.")
            return False
        else:
            router.establishConnection(self, targetName, self.name)
            print(f"Connection established from {self.name} with {targetName}.")
            return True

    def sendMessage(self, targetName, router, message):
        if not router.confirmHost(self.name) or not router.confirmHost(targetName):
            print("Message not sent between {self.name} and {targetName}.")
            return False
        
        

    def registerSelf(self, router):
        router.addHost(self.name, self)
        print(f"Device {self.name} registered to router {router.name}.")
        return True

router = Router("yeet-master-1337")
host1 = EndSystem("yoot-lover-462")
host2 = EndSystem("golden-dog")
router.addHost(host1.name)

# these should all fail (host 2 not registered)
print("failing connection and message")
host1.establishConnection(host2.name, router)
host1.sendMessage(host2.name, router, "I cannot quite yet yote my dude")

# this should also fail as host1 and host2 are not connected
print("failing message")
host1.sendMessage(host2.name, router, "yeet we will soon my dude, but not yet")

# host1 establishes connection and sends message
print("functional connection and message")
host1.establishConnection(host2.name, router)
host1.sendMessage(host2.name, router, "dareth I presume that thou has yoton'd my yought?")