class Polcy :
    def __init__(self , local_subnet , remote_subnet , mode , pfs , esp):
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.mode = mode
        self.esp =esp
        self.pfs = pfs

class Connection:
    def __init__(self , local_IP , remote_IP):
        self.local_IP = local_IP
        self.remote_IP = remote_IP

        self.policies = []
        self.shared_key = None

    def addPoliy(self, policy):
        self.policies.append(policy)

    def set_psk(self , shared_key):
        self.shared_key =shared_key

    def up(self):
        print("IPSEC conection establishing ..")
        print("Local ip is ", self.local_IP)
        print("remote ip is ", self.remote_IP)

        for policy in self.policies:
            print("policy")
            print("LOCAL subnet : ", policy.local_subnet)
            print("REmote Subent : ", policy.remote_subnet)
            print(":Mode : ", policy.mode)
            print("ESP :", policy.esp)
            print("pfs : ", policy.pfs)
        print("SHared key is : ", self.shared_key)
        print("IPSEC connection is established")
            
local_ip = "192.168.0.0"
remote_ip = "192.168.1.0"

c= Connection(local_ip , remote_ip)

loacl_subnet = "10.0.0.0/24"
remote_subnet = "10.0.1.0/24"

outbound_policy = Polcy(loacl_subnet , remote_subnet , mode="tunnel" , esp="SHa246" , pfs="grp14")
c.addPoliy(outbound_policy)
c.set_psk("shared_key")
c.up()