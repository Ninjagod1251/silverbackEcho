<<<<<<< Updated upstream
from math import log2, floor

from ape import convert, project
=======
from ape import convert, project, accounts
>>>>>>> Stashed changes
from silverback import SilverbackApp

from ape_farcaster import Warpcast
import os

app = SilverbackApp()
warper = accounts.load("warpNinjagod")
client = Warpcast(warper)
my_contract = project.Echo.at("0xE8116A0Fb2D4Ee04F570fbEA4460F9C7B0121D76")

@app.on_(my_contract.Received)
def payment_received(log):
    response = client.post_cast(text="A" + "H" * floor(log2(log.amount)))
    print(response.cast.hash)
    #print(client.get_healthcheck())
