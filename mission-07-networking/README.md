# Mission 7 - How computers communicate

## 1. Task / objective
Explain basic network types and concepts, check network connectivity and DNS lookup from the Terminal, and describe what happens when a website is opened.

## 2. Work completed
- Filled in the network concepts table with my own explanations and examples.
- Used `ping` and `nslookup` on `example.com` and wrote down what they showed.
- Wrote a numbered explanation of what happens when I open a website.

### Task 7.1 - Network concepts

| Concept | In my own words | Example |
|---|---|---|
| LAN | A network for a small area where devices are close together | The Wi-Fi at home or the network in a college lab |
| MAN | A network that covers a whole city or a big campus, bigger than a LAN | A network linking all the buildings of a university in one city |
| WAN | A network that covers large areas like countries, joining many smaller networks | The internet |
| DNS | The system that looks up a website name and gives back its IP address, like a phone book | Turning `example.com` into `104.20.23.154` |
| Router | A device that joins networks and sends data packets towards where they need to go | My home Wi-Fi router connecting my devices to the internet |
| Protocol | A set of rules that devices follow so they can understand each other | HTTP/HTTPS for web pages, TCP/IP for sending data |
| Packet switching | Data is cut into small pieces (packets) that travel separately and are put back together at the end | A large photo sent over the internet in many packets |
| Client-server | A client asks for something and a server answers with it | My browser (client) asking a website's server for a page |

### Task 7.2 - Network observations
Connectivity test with `ping`:

```
$ ping -c 3 example.com
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=57 time=6.805 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=57 time=12.797 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=57 time=9.834 ms

3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 6.805/9.812/12.797/2.446 ms
```

DNS lookup with `nslookup`:

```
$ nslookup example.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154
```

I also pinged a site name that does not exist (`notarealsite-xyz-123.invalid`) and got `ping: cannot resolve ... Unknown host`.

Answers:
- **What a connectivity test helps me check:** whether my computer can reach another computer over the network, and how long it takes. All 3 packets arrived (0% loss) in about 10 ms on average, so my connection to the site works and is fast.
- **What a DNS lookup shows:** the IP address (here two addresses) that belongs to a domain name, and which DNS server answered. The server shown is a public DNS server, not anything private about my network.
- **Role of DNS when I type a website name:** computers use IP addresses to find each other, not names. DNS translates the name I type into the IP address so my browser knows where to send the request.

Privacy: the IP addresses above belong to the public example website and a public DNS server. I did not include my own IP address, my Wi-Fi name or any other detail of my network.

### Task 7.3 - What happens when I open a website
1. I type a website address (for example `example.com`) in the **browser** and press Enter. The browser is the **client** that will ask for the page.
2. The browser needs the IP address, so it asks **DNS** to translate the name into an IP address.
3. The request leaves my computer through my **router**, which passes it on towards the internet, using the rules of a **protocol** (HTTPS over TCP/IP).
4. The data travels as small **packets** across many networks and routers (packet switching) until it reaches the website's **server**.
5. The **server** receives the request, finds the page and sends back a **response** (the page's HTML, images and so on) as packets.
6. The packets come back through the routers and my computer puts them back together in the right order.
7. The browser reads the response and shows the web page on my screen.

## 3. Commands / tools used
- `ping -c 3 example.com` - sends 3 test packets and shows if the site replies and how fast
- `nslookup example.com` - asks DNS for the IP address of a domain name
- A text editor - to write the tables and the explanation

## 4. My understanding
A network connects devices so they can share data, and the type (LAN, MAN, WAN) depends on how large the area is. Devices follow protocols so they understand each other, and routers pass the packets along. I learnt that DNS is needed before anything else, because the browser must know the IP address before it can contact the server. Web pages travel in small packets that are put back together, and the whole thing is a client asking and a server answering.

## 5. Difficulties faced
- `nslookup` showed two IP addresses for `example.com`, and `ping` used one of them, so at first it was not clear which address was "the" address.
- The `ping` output had a lot of numbers (ttl, time, stddev) that I did not know the meaning of.
- It was hard to be sure which information is private, because the output included IP addresses.

## 6. How I resolved them
- I understood that one domain can have several IP addresses, and `ping` picks one of them, so both are correct.
- I focused on the lines that matter for this task, which are packets transmitted and received, packet loss and the average time.
- I checked that the addresses shown were the public example site and a public DNS server (not my own IP or Wi-Fi name), and I only included those.

## 7. Evidence / files
- Command outputs shown above (only public addresses)

## 8. Commit details
Commit message: "Explain networking concepts and website communication"
Pushed to GitHub and checked that the file shows up there.
