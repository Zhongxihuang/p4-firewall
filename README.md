# Implementing a Firewall Using P4
## 1. P4 Program File 
See firewall.p4 

## 2. Execution and Test Results 

Firstly, we generated the firewall.json file, which is needed to load the P4 program into the BMv2 software switch by compiling with the commands seen on Figure 16. 

Figure 16. Compiling firewall.p4 and executing custom topography (topo.py) 

**Command** sudo python3 topo.py brings up a topology with 3 hosts (h1, h2, h3) connected to one switch. 


Although our P4 program compiled successfully, h1 was still unable to reach h3 during testing. We double-checked the IP/MAC settings and forwarding table entries, but the issue remained unsolved. This suggests there may have been a hidden misconfiguration in the switch setup or forwarding logic that we couldn’t identify within the experiment time. 

## 3. Analysis and Discussion 

The goal of this experiment is to implement a simple firewall using the P4 programming language to block traffic from host h1 to host h2 within a Mininet simulated environment. 

The implementation should successfully block all packets sent from h1 to h2. Communication from h1 to other hosts remains unaffected, indicating that the P4 program correctly identified and dropped specific traffic. 

**Before Applying the P4 Program:**

The Mininet network topology allowed unrestricted communication between all hosts. The network consisted of three hosts: 

- h1 (IP: 10.0.0.1) 

- h2 (IP: 10.0.0.2) 

- h3 (IP: 10.0.0.3) 

**After Applying the P4 Firewall Program:**

Once the P4 program was compiled and deployed to the switch, the firewall rule was enforced to specifically block traffic **from h1 (10.0.0.1) to h2 (10.0.0.2).**

P4 offers more programmable control over how packets are processed at the data plane, enabling highly customized firewall rules. In contrast, traditional firewalls operate at higher layers and may not provide as fine-grained or low-latency control. 

 

 

 
