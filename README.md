Found this buried deep amongst some old projects, and while it contains the python literacy of an Amazonian tribe Shaman, It got me interested in picking it up again to do it properly.

Basically, what was attempted here, was a chatroom hosted through a broswer instance running on the chromedriver-manager, filtered through a tor proxy.
Obviously didn't go to plan - I didn't even initialise the instances I created under the entrypoint to the script lol.

Cool concept, but if you really wanted to, you could achieve the exact same thing, on a more permanent basis, as follows:

1. Download the full Tor bundle,
2. configure the control port in the torrc config file to filter through loopback / port 9051
3. Set an Auth method (please)

Run it - your internet traffic is routed accordingly. Then you can fire up any old chatroom and rejoice in your geographical anonymity.


I'll take this apart and rebuild it befitting someone with actual tech-literacy - you know, not using flask for starters.
I'll go through react, and see if I can set up a rotating proxy instead of a static instance.


THIS IS NOT A CURRENT PROJECT | THIS IS NOT A REPRESENATION OF ME AS A DEVELOPER, OR A HUMAN BEING
