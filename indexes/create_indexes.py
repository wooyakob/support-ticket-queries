import os
from dotenv import load_dotenv
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

load_dotenv()

username = os.getenv("CB_USERNAME")
password = os.getenv("CLUSTER_ACCESS")
couchbase_url = os.getenv("CB_ENDPOINT")

cluster = Cluster(
    couchbase_url,
    ClusterOptions(PasswordAuthenticator(username, password))
)

index_queries = [
    # Customer name index
    "CREATE INDEX idx_customer_name ON `customer-support`.`2025-tickets`.`us-customers`(`Customer`);",
    # Satisfaction index
    "CREATE INDEX idx_satisfaction ON `customer-support`.`2025-tickets`.`us-customers`(`Satisfaction`);",
    # Document ID index
    "CREATE INDEX idx_document_id ON `customer-support`.`2025-tickets`.`us-customers`(`ID`);",
    # Product price (first element) index
    "CREATE INDEX idx_product_price_first ON `customer-support`.`2025-tickets`.`us-customers`(`Product Price`[0]);",
    # Product name index
    "CREATE INDEX idx_product ON `customer-support`.`2025-tickets`.`us-customers`(`Product`);"
]

for query in index_queries:
    try:
        cluster.query(query).execute()
        print(f"Executed: {query}")
    except Exception as e:
        print(f"Error executing: {query}\n{e}")