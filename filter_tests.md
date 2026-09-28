\# Network Traffic Filtering Tests



\## 1. Lab Environment



The firewall tests were performed in an authorised Ubuntu Server laboratory environment using UFW (Uncomplicated Firewall).



The laboratory service used for testing was a Python HTTP server running on TCP port 8080.



The service was started with:



```bash

python3 -m http.server 8080 --bind 0.0.0.0

```



\## 2. Firewall Objective



The firewall configuration was designed to:



1\. Block unauthorised guest access to the protected service.

2\. Permit authorised staff access to the service.

3\. Block other unauthorised inbound access.



\## 3. Planned Firewall Configuration



The intended UFW configuration is:



```bash

sudo ufw default deny incoming

sudo ufw default allow outgoing

sudo ufw allow from <STAFF\_IP> to any port 8080 proto tcp

sudo ufw deny from <GUEST\_IP> to any port 8080 proto tcp

sudo ufw enable

sudo ufw status numbered

```



`<STAFF\_IP>` and `<GUEST\_IP>` represent the IP addresses assigned to the authorised staff and guest laboratory clients.



\## 4. Test Cases



| Test | Source                    | Destination   | Expected Result      | Actual Result                 |

| ---- | ------------------------- | ------------- | -------------------- | ----------------------------- |

| 1    | Authorised staff client   | TCP port 8080 | Connection permitted | To be recorded after lab test |

| 2    | Guest client              | TCP port 8080 | Connection blocked   | To be recorded after lab test |

| 3    | Other unauthorised client | TCP port 8080 | Connection blocked   | To be recorded after lab test |



\## 5. Test Procedure



For the permitted connection, the staff client should use:



```bash

curl http://<SERVER\_IP>:8080

```



For a blocked connection, the client should use:



```bash

curl --max-time 5 http://<SERVER\_IP>:8080

```



The expected result for the authorised client is that the HTTP directory listing is returned.



The expected result for unauthorised clients is that the connection is blocked or times out.



\## 6. Evidence



The final UFW status and the actual connection results will be recorded after completing the authorised laboratory firewall test.



No unauthorised network systems were tested.



