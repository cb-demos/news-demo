# Import Rollout SDK
from rox.server.rox_server import Rox
from rox.server.flags.rox_flag import RoxFlag
from rox.server.flags.rox_variant import RoxVariant
from rox.server.rox_options import RoxOptions
import sys
import time

from decouple import config

# Create Roxflags in the Flags container class
class Flags:
    def __init__(self):
        # Define the feature flags
        self.score = RoxFlag(False)
        self.scoreMigration = RoxFlag(False)
        self.dbName = RoxVariant("HN_ONE")


flags = Flags()
# undefined
# Register the flags container with Rollout
Rox.register("default", flags)

cancel_event = Rox.setup(config("CB_FF_KEY")).result()
