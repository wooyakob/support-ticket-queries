# Support Ticket Queries

This project provides tools to query and analyze customer support tickets stored in a Couchbase Capella cluster. It includes scripts for retrieving data based on various criteria and demonstrates the performance benefits of indexing.

---

## Setup Capella Free Tier Cluster

1. **Cluster Configuration**:
   - **Bucket**: `customer-support`
   - **Scope**: `2025-tickets`
   - **Collection**: `us-customers`

2. **Import Dataset**:
   - Use the file `us-customers-2025.json` to populate the collection.

3. **JSON Schema**:
   - The dataset is adapted from the [Customer Support Ticket Dataset](https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset) and customized to represent customer support interactions.

---

## Cluster Access

1. Create a `.env` file with the following variables:
   ```bash
   CLUSTER_ACCESS = ""
   CB_USERNAME = ""
   CB_PASSWORD = ""
   CB_ENDPOINT = ""
   ```

2. Set up cluster access credentials in Couchbase Capella.
3. Add your IP address as an authorized network.
4. Load the environment variables.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wooyakob/support-ticket-queries
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Queries

Navigate to the `/queries` directory to run the following scripts:

- **`customer.py`**: Retrieve support data by customer name.
- **`feedback.py`**: Fetch support data based on customer satisfaction scores (e.g., happy customers with a score of 5).
- **`id.py`**: Retrieve support data using a specific document ID.
- **`price.py`**: Search for tickets where the product price is greater than $1,000.
- **`product.py`**: Retrieve support data for a specific product (e.g., Capella Free Trials).

---

## Indexing

Indexes are created to improve query performance by enabling Couchbase to locate documents faster without scanning the entire collection. Below are the indexes used in this project:

- **Customer Name**:
  ```sql
  CREATE INDEX idx_customer_name ON `us-customers`(`Customer`);
  ```

- **Satisfaction Score**:
  ```sql
  CREATE INDEX idx_satisfaction ON `us-customers`(`Satisfaction`);
  ```

- **Document ID**:
  ```sql
  CREATE INDEX idx_document_id ON `us-customers`(`ID`);
  ```

- **Product Price**:
  ```sql
  CREATE INDEX idx_product_price_first ON `us-customers`(`Product Price`[0]);
  ```

- **Product Name**:
  ```sql
  CREATE INDEX idx_product ON `us-customers`(`Product`);
  ```

---

## Performance Comparison

| **Scenario**   | **Elapsed Time** | **Execution Time** |
|-----------------|------------------|--------------------|
| **Before Index** | 841.2ms         | 841.1ms            |
| **After Index**  | 4.6ms           | 4.6ms              |

---

## Notes

- Ensure your Couchbase Capella cluster is properly configured before running the scripts.
- The dataset and queries are designed for demonstration purposes and may require adjustments for production use.