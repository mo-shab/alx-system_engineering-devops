# Secured and Monitored Web Infrastructure

![Image of a secured and monitored infrastructure](https://i.imgur.com/CwSCTem.jpeg)


## Description

This is a 3-server web infrastructure that is secured, monitored, and serves encrypted traffic.

## Specifics About This Infrastructure

- **Purpose of Firewalls**  
  Firewalls protect the network, specifically the web servers, from unwanted and unauthorized users. They act as intermediaries between the internal and external networks, blocking incoming traffic that meets predefined criteria.

- **Purpose of SSL Certificate**  
  SSL certificates encrypt traffic between the web servers and the external network, preventing man-in-the-middle attacks (MITM) and network sniffers from intercepting valuable information. SSL certificates ensure privacy, integrity, and identification.

- **Purpose of Monitoring Clients**  
  Monitoring clients are responsible for observing the servers and the external network. They analyze server performance and operations, measuring overall health and alerting administrators to any unexpected issues. Monitoring tools provide key metrics about server operations, automatically testing accessibility, measuring response time, and alerting for errors such as corrupt or missing files, security vulnerabilities, and other issues.

## Issues With This Infrastructure

- **SSL Termination at Load Balancer Level**  
  Terminating SSL at the load balancer level leaves traffic between the load balancer and web servers unencrypted, potentially exposing sensitive data.

- **Single MySQL Server**  
  Having only one MySQL server is not scalable and can act as a single point of failure for the web infrastructure.

- **Homogeneous Server Components**  
  Servers with identical components contend for resources such as CPU, memory, and I/O, leading to potential performance issues. This setup is not easily scalable and can make troubleshooting difficult.
