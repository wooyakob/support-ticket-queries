import os
import traceback
import json
from datetime import timedelta

from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions

from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv("CB_ENDPOINT")
username = os.getenv("CB_USERNAME")
password = os.getenv("CLUSTER_ACCESS")

if not isinstance(password, str):
    raise ValueError("The password must be a string.")

auth = PasswordAuthenticator(username, password)
options = ClusterOptions(auth)

try:
    cluster = Cluster(endpoint, options)
    cluster.wait_until_ready(timedelta(seconds=5))

    # Get support data for a specific product e.g. Capella Free Trials!

    query = """
    SELECT r.*
    FROM `customer-support`.`2025-tickets`.`us-customers` AS r
    WHERE r.Product = "Couchbase Enterprise Edition License";
    """
    result = cluster.query(query)
    for row in result:
        print(json.dumps(row, indent=4))

except Exception as e:
    print("An error occurred:")
    traceback.print_exc()