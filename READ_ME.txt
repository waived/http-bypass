┬  ┌─┐┬ ┬┌─┐┬─┐     ┌─┐   ┌┐ ┬ ┬┌─┐┌─┐┌─┐┌─┐
│  ├─┤└┬┘├┤ ├┬┘ ───  ─┼─  ├┴┐└┬┘├─┘├─┤└─┐└─┐
┴─┘┴ ┴ ┴ └─┘┴└─       ┴   └─┘ ┴ ┴  ┴ ┴└─┘└─┘

Overview:
      When launching Application-Layer DDoS attacks against a website, one may encounter some sort of
      reverse-proxy infrastructure. This may come in the form of a CDN (Content Delivery Network) or Load
      Balancers, WAF (Web Application Firewall), IDS/IPS (Intrusion Detection/Prevention System), or any
      other sort of medium that regulates caching, rate limiting, and filters for malicious traffic.

      Ideally, when flooding a website protected by one of these reverse-proxy services, one would first
      want to use proper reconnaissance techniques to bypass the service altogether. If one is unable to
      properly identify the IP address of the origin server, then negotiation with the reverse-proxy service
      will be necessary in order to pass traffic to the target and take down the site.

      This script serves as a benchmark for how this process may be conducted. The attacker will load in
      a list of proxies (in the format of: <protocol>://<ip>:<port>). This script supports HTTP, HTTPS, and
      SOCK4 proxy servers. Each request will be sent through said proxy(s). The HTTP request will have
      randomized headers, including the user-agent, referer, and a random header will be picked from an
      alternative list to ensure each request remains esoteric and more difficult to filter/block.

Known bugs / issues:
      Socket exhaustion! It is possible that (depending on your system and device specs) this script will
      use up all the local sockets before they exit the TIME_WAIT status and are available again for use.
      With Python, a 'OSError' will be thrown and caught via the generic 'except' clause. It may be
      adventageous to reuse the proxy-server / local-socket multiple times before switching to a new one.
      I may implement this feature in future updates. 

      Although not necessarily a bug, the Socket Timeout is set to endure for 1-second before throwing out
      the request. This is done for effeciency. This value can be changed to accomidate slower connections.

Updates:
      No, lol. Good luck!
