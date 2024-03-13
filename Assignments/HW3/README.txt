Homework Assignment 3

Task 1 QnA
What is the output of “nodes” and “net”

Output of command nodes
mininet> nodes
available nodes are: 
c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7


Output of command net
mininet> net
h1 h1-eth0:s3-eth1
h2 h2-eth0:s3-eth2
h3 h3-eth0:s4-eth1
h4 h4-eth0:s4-eth2
h5 h5-eth0:s6-eth1
h6 h6-eth0:s6-eth2
h7 h7-eth0:s7-eth1
h8 h8-eth0:s7-eth2
s1 lo:  s1-eth1:s2-eth3 s1-eth2:s5-eth3
s2 lo:  s2-eth1:s3-eth3 s2-eth2:s4-eth3 s2-eth3:s1-eth1
s3 lo:  s3-eth1:h1-eth0 s3-eth2:h2-eth0 s3-eth3:s2-eth1
s4 lo:  s4-eth1:h3-eth0 s4-eth2:h4-eth0 s4-eth3:s2-eth2
s5 lo:  s5-eth1:s6-eth3 s5-eth2:s7-eth3 s5-eth3:s1-eth2
s6 lo:  s6-eth1:h5-eth0 s6-eth2:h6-eth0 s6-eth3:s5-eth1
s7 lo:  s7-eth1:h7-eth0 s7-eth2:h8-eth0 s7-eth3:s5-eth2
c0


What is the output of “h7 ifconfig”
Output of command h7 ifconfig
mininet> h7 ifconfig
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::d82e:38ff:fea1:2145  prefixlen 64  scopeid 0x20<link>
        ether da:2e:38:a1:21:45  txqueuelen 1000  (Ethernet)
        RX packets 64  bytes 4896 (4.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11  bytes 866 (866.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

Task 2 QnA

Draw the function call graph of this controller. For example, once a packet comes to the controller, which function is the first to be called, which one is the second, and so forth?

To begin, launch the POX listener by executing the command ./pox.py log.level --DEBUG misc.of_tutorial, which activates the start switch. Following this initialization, the _handle_PacketIn() method is invoked by the start switch to manage incoming packet messages from the switch. Subsequently, the _handle_PacketIn() function triggers the act_like_hub() function. The act_like_hub() function is designed to mimic a hub environment by broadcasting packets to all ports except the incoming port. Afterward, the resend_packet() method is invoked. This method appends a packet to the message data and executes an action on it. It instructs the switch to retransmit the packet to a specified port via this message. The sequence of operations is depicted as follows 
start switch: _handle_PacketIn() → act_like_hub() → resend_packet() → send(msg)


Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).

How long does it take (on average) to ping for each case?

mininet> h1 ping -c100 h2

           The average time to ping in the case of h1 ping h2 with 100 packets is 2.945ms           

mininet> h1 ping -c100 h8

      The average time to ping in the case of h1 ping h8 with 100 packets is 11.315ms.


What is the minimum and maximum ping you have observed?

Minimum ping observed
For h1 ping -c100 h2 - 1.707ms
For h1 ping -c100 h8 - 5.522ms


Maximum ping observed
For h1 ping -c100 h2 - 6.285ms
For h1 ping -c100 h8 - 20.286ms


What is the difference, and why?
The ping time between h1 and h8 (11.315ms, as shown in the initial screenshot) is greater than that between h1 and h2 (2.945ms, as displayed in the screenshot). This disparity arises from the differing network paths taken by the packets. To reach h8 from h1, the packets traverse through switches s3, s2, s1, s5, and s7. Conversely, there's only one switch between h1 and h2. Consequently, the ping time is prolonged in the latter scenario, specifically for the route between h1 and h8.


Run “iperf h1 h2” and “iperf h1 h8”
What is “iperf” used for?’
iPerf, is an Internet Performance Working Group. It is an open-source utility for conducting speed tests and assessing network performance. Its functionality is straightforward: it generates TCP and UDP streams to transmit traffic from one host to another, subsequently providing users with reports detailing the maximum bandwidth achieved. This capability enables users to ascertain network throughput and identify peak bandwidth capabilities.


What is the throughput for each case?

mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2 
.*** Results: ['14.1 Mbits/sec', '13.9 Mbits/sec']


mininet> iperf h1 h8
*** Iperf: testing TCP bandwidth between h1 and h8 
*** Results: ['9.11 Mbits/sec', '8.84 Mbits/sec']

What is the difference, and explain the reasons for the difference.
The difference in performance is attributed to differences in network topology and latency levels. Fewer intermediary stops between h1 and h2 contribute to lower latency and reduced congestion, allowing for smoother data flow and higher throughput. Contrarily, the greater number of stops between h1 and h8 introduces more latency and potential congestion spots, thus hindering data transfer speed.


Which of the switches observes traffic? Please describe your way of observing such traffic on switches (e.g., adding some functions in the “of_tutorial” controller).
To identify which switches are monitoring traffic, we can implement a method within the of_tutorial controller. By adding the line log.info("Switch observing traffic: %s" % (self.connection)) to line number 133 of the controller, we can log information about switch activity. This allows us to determine that all switches are indeed monitoring traffic, especially during periods of high packet load. Also, the event listener function _handle_PacketIn is triggered whenever a switch receives a packet, providing additional insight into traffic observation mechanisms.

Task 3 QnA
Describe how the above code works, such as how the "MAC to Port" map is established.
You could use a ‘ping’ example to describe the establishment process (e.g., h1 ping h2).

Within our code, the act-like-switch function serves a crucial role in identifying the whereabouts of MAC addresses. Therefore, when a MAC address is identified as the intended recipient of a message, the controller is capable of efficiently associating this MAC address with a specific port, simplifying the routing process. This optimization notably enhances the controller's efficiency in transmitting packets to addresses already within its knowledge, as packets can be swiftly directed to their designated ports. Where the destination MAC address remains unknown, the function resorts to flooding the packet to all possible destinations. With the reduction in the frequency of flooding, courtesy of the MAC Learning Controller, overall network performance experiences significant improvements in terms of both ping times and throughput.


(Comment out all prints before doing this experiment)
Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).

How long did it take (on average) to ping for each case?

For h1 ping -c100 h2 

The Average time to ping in the case of h1 ping h2 is 0.104 ms

For h1 ping -c100 h8

The average time to ping in the case of h1 ping h8 is 0.324 ms
































Screenshot for  h1 ping -c100 h2
 






Screenshot for  h1 ping -c100 h8


What is the minimum and maximum ping you have observed?

Minimum ping Observed -
For h1 ping -c100 h2 - 0.053ms
For h1 ping -c100 h8 - 0.074ms


Maximum ping Observed -
For h1 ping -c100 h2 - 0.298ms
For h1 ping -c100 h8 - 18.099ms


Any difference from Task 2, and why do you think there is a change if there is?

Task 3 displays a slightly shorter duration compared to Task 2 when evaluating the ping time between h1 and h2, even though the discrepancy is minor. However, the ping time disparity between h1 and h8 is notably significant due to the extensive routing involved. In Task 3, where only the initial few packets are subjected to flooding, it becomes evident that this task operates notably quicker or demonstrates reduced ping times. This efficiency arises from the fact that once the destination MAC address is identified within the "Mac to port" mapping, subsequent packets are promptly directed to their designated ports without the need for flooding. Consequently, future pings experience considerable acceleration owing to diminished network congestion.


Q.3 Run “iperf h1 h2” and “iperf h1 h8”.
What is the throughput for each case?

What is the difference from Task 2 and why do you think there is a change if there is?
In both scenarios, Task 3 demonstrates excellent throughput compared to Task 2. This can be attributed to the reduced network congestion inherent in Task 3. As the "Mac to port" mapping has already learned all the necessary port associations, there is no need for packet flooding, thereby alleviating the burden on switches. The implementation of pre-computed and learned routes, coupled with controller updates, is evident in the significant throughput enhancements observed between Task 2 and Task 3 for h1 and h2. Contrarily, the throughput improvement is less pronounced for h1 and h8 due to the higher number of hops and increased likelihood of packet dropping along the route.


