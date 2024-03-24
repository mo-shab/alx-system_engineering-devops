# Distributed Web Infrastructure

![Image of a distributed web infrastructure](https://i.imgur.com/oG5aLxD.jpeg)


## Description

This distributed web infrastructure aims to alleviate traffic on the primary server by distributing some of the load to a replica server, facilitated by a load balancer responsible for balancing the workload between the two servers (primary and replica).

## Specifics About This Infrastructure

- **Distribution Algorithm of the Load Balancer**  
  The HAProxy load balancer is configured with the *Round Robin* distribution algorithm. This algorithm cycles through each server behind the load balancer in turns, distributing the workload according to their weights. It ensures smooth and fair distribution of processing time among servers. *Round Robin* is dynamic, allowing for adjustments to server weights on the fly.

- **Setup Enabled by the Load Balancer**  
  The HAProxy load balancer facilitates an *Active-Passive* setup instead of an *Active-Active* setup. In an *Active-Active* setup, workloads are distributed across all nodes to prevent overloading any single node, leading to improved throughput and response times. Conversely, in an *Active-Passive* setup, not all nodes are active simultaneously. For instance, if one node is active, the other remains passive or on standby, ready to become active if needed.

- **Functioning of a Database Primary-Replica (Master-Slave) Cluster**  
  A *Primary-Replica* setup designates one server as the *Primary* and another as the *Replica*. The *Primary* server handles read/write requests, while the *Replica* server only handles read requests. Data synchronization occurs whenever the *Primary* server executes a write operation.

- **Difference Between Primary and Replica Nodes in Application Handling**  
  The *Primary* node manages all write operations for the site, while the *Replica* node handles read operations, reducing read traffic to the *Primary* node.

## Issues With This Infrastructure

- **Multiple Single Points of Failure (SPOF)**  
  For instance, if the Primary MySQL database server goes down, the entire site becomes unable to make changes (such as adding or removing users). Additionally, the server housing the load balancer and the application server connecting to the primary database server are also potential SPOFs.

- **Security Vulnerabilities**  
  Data transmitted over the network lacks encryption via an SSL certificate, potentially exposing it to interception by hackers. Furthermore, the absence of a firewall on any server means there's no mechanism to block unauthorized IPs.

- **Lack of Monitoring**  
  Without monitoring, there's no visibility into the status of each server. Monitoring is essential for identifying issues and ensuring the infrastructure operates optimally.
