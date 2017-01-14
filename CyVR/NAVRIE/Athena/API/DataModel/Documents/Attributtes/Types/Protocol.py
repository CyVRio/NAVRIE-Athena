import logging
from CyVR.NAVRIE.Athena.API.DataModel.Documents.Attributtes.AttributeTools import AttributeTools

class Protocol(object):
    """description of class"""

    def Protcol_SelfSet(protocol):
        attribute = AttributeTools.setAttribute("Network_Protocol", protocol)
        return attribute

    def Protocol_ICMP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "icmp")
        return attribute

    def Protocol_IGMP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "igmp")
        return attribute

    def Protocol_GGP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "ggp")
        return attribute

    def Protocol_IPv4():
        attribute = AttributeTools.setAttribute("Network_Protocol", "ipv4")
        return attribute

    def Protocol_Stream():
        attribute = AttributeTools.setAttribute("Network_Protocol", "st")
        return attribute

    def Protocol_TCP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "tcp")
        return attribute

    def Protocol_CBT():
        attribute = AttributeTools.setAttribute("Network_Protocol", "cbt")
        return attribute

    def Protocol_EGP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "egp")
        return attribute

    def Protocol_IGP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "igp")
        return attribute

    def Protocol_BBN_RCC_MON():
        attribute = AttributeTools.setAttribute("Network_Protocol", "bbn-rcc-mon")
        return attribute

    def Protocol_NVP_II():
        attribute = AttributeTools.setAttribute("Network_Protocol", "nvp-ii")
        return attribute

    def Protocol_PUP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "pup")
        return attribute

    def Protocol_ARGUS():
        attribute = AttributeTools.setAttribute("Network_Protocol", "argus")
        return attribute

    def Protocol_EMCON():
        attribute = AttributeTools.setAttribute("Network_Protocol", "emcon")
        return attribute

    def Protocol_XNET():
        attribute = AttributeTools.setAttribute("Network_Protocol", "xnet")
        return attribute

    def Protocol_Chaos():
        attribute = AttributeTools.setAttribute("Network_Protocol", "chaos")
        return attribute

    def Protocol_UDP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "udp")
        return attribute

    def Protocol_MUX():
        attribute = AttributeTools.setAttribute("Network_Protocol", "mux")
        return attribute

    def Protocol_DCN_MEAS():
        attribute = AttributeTools.setAttribute("Network_Protocol", "dcn-meas")
        return attribute

    def Protocol_HMP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "hmp")
        return attribute

    def Protocol_IGP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "igp")
        return attribute

    def Protocol_IPv6():
        attribute = AttributeTools.setAttribute("Network_Protocol", "ipv6")
        return attribute

    def Protocol_IPv6_Hop_Option():
        attribute = AttributeTools.setAttribute("Network_Protocol", "hopopt")
        return attribute

    def Protocol_IPv6_Route():
        attribute = AttributeTools.setAttribute("Network_Protocol", "ipv6-route")
        return attribute

    def Protocol_IPv6_Frag():
        attribute = AttributeTools.setAttribute("Network_Protocol", "ipv6-frag")
        return attribute

    def Protocol_IPv6_ICMP():
        attribute = AttributeTools.setAttribute("Network_Protocol", "ipv6-icmp")
        return attribute

    def Protocol_IPv6_Nonxt():
        attribute = AttributeTools.setAttribute("Network_Protocol", "ipv6-nonxt")
        return attribute

    def Protocol_IPv6_Opts():
        attribute = AttributeTools.setAttribute("Network_Protocol", "ipv6-opts")
        return attribute

    def Protocol_PRM():
        attribute = AttributeTools.setAttribute("Network_Protocol", "prm")
        return attribute

    def Protocol_Trunk_1():
        attribute = AttributeTools.setAttribute("Network_Protocol", "trunk-1")
        return attribute

    def Protocol_Trunk_2():
        attribute = AttributeTools.setAttribute("Network_Protocol", "trunk-2")
        return attribute





'''
# This list is based on IEEE data at
xns-idp          22  # XEROX NS IDP
leaf-1           25  # Leaf-1
leaf-2           26  # Leaf-2
rdp              27  # Reliable Data Protocol
irtp             28  # Internet Reliable Transaction
iso-tp4          29  # ISO Transport Protocol Class 4
netblt           30  # Bulk Data Transfer Protocol
mfe-nsp          31  # MFE Network Services Protocol
merit-inp        32  # MERIT Internodal Protocol
dccp             33  # Datagram Congestion Control Protocol
3pc              34  # Third Party Connect Protocol
idpr             35  # Inter-Domain Policy Routing Protocol
xtp              36  # XTP
ddp              37  # Datagram Delivery Protocol
idpr-cmtp        38  # IDPR Control Message Transport Proto
tp++             39  # TP+
il               40  # IL Transport Protocol
sdrp             42  # Source Demand Routing Protocol
idrp             45  # Inter-Domain Routing Protocol
rsvp             46  # Reservation Protocol
gre              47  # General Routing Encapsulation
dsp              48  # Dynamic Source Routing Protocol. Historically MHRP
bna              49  # BNA
esp              50  # Encap Security Payload
ah               51  # Authentication Header
i-nlsp           52  # Integrated Net Layer Security  TUBA
swipe            53  # IP with Encryption
narp             54  # NBMA Address Resolution Protocol
mobile           55  # IP Mobility
tlsp             56  # Transport Layer Security Protocol using Kryptonet key management
skip             57  # SKIP
anyhost          61  # any host internal protocol
cftp             62  # CFTP
anylocalnet      63  # any local network
sat-expak        64  # SATNET and Backroom EXPAK
kryptolan        65  # Kryptolan
rvd              66  # MIT Remote Virtual Disk Protocol
ippc             67  # Internet Pluribus Packet Core
anydistribfs     68  # any distributed file system
sat-mon          69  # SATNET Monitoring
visa             70  # VISA Protocol
ipcv             71  # Internet Packet Core Utility
cpnx             72  # Computer Protocol Network Executive
cphb             73  # Computer Protocol Heart Beat
wsn              74  # Wang Span Network
pvp              75  # Packet Video Protocol
br-sat-mon       76  # Backroom SATNET Monitoring
sun-nd           77  # SUN ND PROTOCOL-Temporary
wb-mon           78  # WIDEBAND Monitoring
wb-expak         79  # WIDEBAND EXPAK
iso-ip           80  # ISO Internet Protocol
vmtp             81  # VMTP
secure-vmtp      82  # SECURE-VMTP
vines            83  # VINES
iptm             84  # Internet Protocol Traffic Manager. Historically TTP
nsfnet-igp       85  # NSFNET-IGP
dgp              86  # Dissimilar Gateway Protocol
tcf              87  # TCF
eigrp            88  # EIGRP
ospfigp          89  # OSPFIGP
sprite-rpc       90  # Sprite RPC Protocol
larp             91  # Locus Address Resolution Protocol
mtp              92  # Multicast Transport Protocol
ax.25            93  # AX.
ipip             94  # IP-within-IP Encapsulation Protocol
micp             95  # Mobile Internetworking Control Pro.
scc-sp           96  # Semaphore Communications Sec.
etherip          97  # Ethernet-within-IP Encapsulation
encap            98  # Encapsulation Header
anyencrypt       99  # any private encryption scheme
gmtp            100  # GMTP
ifmp            101  # Ipsilon Flow Management Protocol
pnni            102  # PNNI over IP
pim             103  # Protocol Independent Multicast
aris            104  # ARIS
scps            105  # SCPS
qnx             106  # QNX
a/n             107  # Active Networks
ipcomp          108  # IP Payload Compression Protocol
snp             109  # Sitara Networks Protocol
compaq-peer     110  # Compaq Peer Protocol
ipx-in-ip       111  # IPX in IP
vrrp            112  # Virtual Router Redundancy Protocol
pgm             113  # PGM Reliable Transport Protocol
any0hop         114  # any 0-hop protocol
l2tp            115  # Layer Two Tunneling Protocol
ddx             116  # D-II Data Exchange (
iatp            117  # Interactive Agent Transfer Protocol
stp             118  # Schedule Transfer Protocol
srp             119  # SpectraLink Radio Protocol
uti             120  # UTI
smp             121  # Simple Message Protocol
sm              122  # Simple Multicast Protocol
ptp             123  # Performance Transparency Protocol
isis-ipv4       124  # ISIS over IPv4
fire            125
crtp            126  # Combat Radio Transport Protocol
crudp           127  # Combat Radio User Datagram
sscopmce        128
iplt            129
sps             130  # Secure Packet Shield
pipe            131  # Private IP Encapsulation within IP
sctp            132  # Stream Control Transmission Protocol
fc              133  # Fibre Channel
rsvp-e2e-ignore 134
mobility-hdr    135  # Mobility Header
udplite         136  # UDP-Lite [RFC3828]
mpls-in-ip      137  # MPLS-in-IP [RFC4023]
manet           138  # MANET Protocols [RFC5498]
hip             139  # Host Identity Protocol
shim6           140  # Shim6 Protocol [RFC5533]
wesp            141  # Wrapped Encapsulating Security Payload
rohc            142  # Robust Header Compression
experimental1   253  # Use for experimentation and testing
experimental2   254  # Use for experimentation and testing
'''