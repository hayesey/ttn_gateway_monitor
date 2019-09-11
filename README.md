# The Things Network Gateway Status Checker

This simple script gets the timestamp from the Things Network (TTN) for a list of gateways and pushes it to Nodeping.

The timestamp is the time the gateway was last seen by TTN's Network Server so when this is combined with an appropriately configured Nodeping check, you will get alerts if a gateway has gone offline.

## How To Use

This assumes you already have a working TTN account with at least one gateway talking to it and that you have a Nodeping account.

* log in to Nodeping and create a new check of the type PUSH.  In the fields section you need to add one per gateway to be monitored.  In "Name" put the gateway EUI, either as the 8 byte EUI on it's own or the full TTN format (i.e. "eui-0000000000000000").  Which ever format you choose, the entry in settings.py (see next step) **must** match this.  The "max" time (in minutes) will depend on how busy the gateway is, if it is receiving a lot of uplink messages then this can be quite short, if it's not receiving many then it needs to be longer.  I have mine set to 30 minutes as if my gateway hasn't sent an uplink in that time, something is wrong.  Set "min" to 0 as it doesn't matter.  Make sure to have "fail when results are old" checked so you know if this script isn't working.  I have check frequency set to 5 minutes.
* copy settings.py.sample to settings.py
* edit settings.py, put all the gateway IDs you want to monitor into the list called gw_euis.  This can either be the gateway EUI on it's own or the TTN format "eui-0000000000000000" ID but it has to match whatever you put into the Nodeping check field.
* Fill out the Nodeping check ID and token.  You can see these on the Nodeping website in the new check you created in the first step.
* Create a cronjob to run the script "ttn_gw_mon.py", the frequency should match what you put as the frequency in Nodeping.  E.G. `*/5 * * * * /usr/bin/python3 /path/to/script/ttn_gw_mon.py`

