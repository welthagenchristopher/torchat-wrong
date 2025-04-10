I Found this buried deep amongst some old projects, and while it contains the python literacy of an Amazonian tribe Shaman,
it got me interested in picking it up again to do it properly.

Basically, what was attempted here, was a chatroom hosted through a broswer instance running on the chromedriver-manager, 
filtered through a tor proxy. Obviously didn't go to plan - _I didn't even initialise the instances I created under the
entrypoint to the script . . ._

-------------------------------------------------------------------------------------------------------------------------------------

Off the bat, if all you're after is internet-traffic anonymity, there is a much easier way to go about it:

    1. Download the Tor bundle: https://www.torproject.org/download/tor/
    2. Open the torrc config file:
      i. Control port : 9051
      ii. enable a security method
    3. Configure your internet options -> connections -> lan settings to route through your loopback + port 9051
    4. start the service using the executable (--service start) 

Now your internet traffic is routed accordingly. You can then fire up any old chatroom and rejoice in your geographical anonymity.

----------------------------------------------------------------------------------------------------------------------------------------

However, for those of you who like to get your hands dirty, or want to witness the beauty of built in security at a level that evades
streaming and chat services - this is (to some degree) where you start.

Obviously, I'm not exactly proud of this at the current moment - I certainly did not know enough at the time to attempt this,
but I will be re-visiting it, and currently plan on the following configuration:

  Stack: Python & React (websocket communication)
  Proxy: rotating Tor proxy enabled via use of the stem library, and its Signal method.
  Result: A useless, albiet interesting and versatile piece of software

---------------------------------------------------------------------------------------------------------------------------------------
This method would do wonders for web-scraping capabilities as well, which would follow the exact same principle. However, you'd have to
explicitly deny browser caching - that would defeat the entire purpose.



THIS IS NOT A CURRENT PROJECT | THIS IS NOT A REPRESENATION OF ME AS A DEVELOPER, OR A HUMAN BEING
