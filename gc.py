import os
import logging
import datetime
from dotenv import load_dotenv
import pandas as pd
import json

from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)


# Configure debug logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Example dates
today = datetime.date.today()
lastweek = today - datetime.timedelta(days=7)

# Load Garmin Connect credentials from environment variables
load_dotenv()

## Initialize Garmin api with your credentials using environement variables,
# instead of hardcoded sensitive data.
api = Garmin(os.getenv("EMAIL"), os.getenv("PASSWORD"))

## Login to Garmin Connect portal
api.login()

logger.info(api.get_full_name())

# logger.info(api.get_last_activity())

last_activity = api.get_last_activity()
all_activity = api.get_activities_by_date('2022-01-01', today)

outputfile_name = 'data/' + 'all_activities' + '.json'

with open(outputfile_name, "w") as outfile:
    json.dump(all_activity, outfile)