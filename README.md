# DataFlowX: End-to-End Big Data Engineering on Azure ☁️

<div align="center">

![Azure](https://img.shields.io/badge/Microsoft_Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)

**A complete Azure-based data pipeline for Brazilian e-commerce analytics**

[Architecture](#architecture) • [Tech Stack](#tech-stack) • [Features](#features) • [Getting Started](#getting-started)

</div>

---

## 📋 Overview

DataFlowX is a production-grade big data engineering project that implements a complete Azure-based data pipeline for analyzing Brazilian e-commerce data. The project follows industry-standard **Medallion Architecture** (Bronze/Silver/Gold layers) and demonstrates end-to-end data engineering workflows—from ingestion to visualization.

This project is ideal for:
- 🎯 Data engineers seeking real-world Azure experience
- 📊 BI developers targeting cloud-based pipelines
- 🎓 Students preparing for data engineering interviews
- 💼 Professionals building portfolio projects

### Key Highlights
- **Multi-source ingestion**: HTTP endpoints, SQL databases, and NoSQL (MongoDB)
- **Scalable architecture**: Medallion pattern with Bronze, Silver, and Gold layers
- **Real-world dataset**: Olist Brazilian E-Commerce dataset (100k+ orders)
- **Cloud-native**: Built entirely on Azure ecosystem
- **Production-ready**: Includes monitoring, error handling, and best practices

---

## 🏗️ Architecture

### Medallion Architecture Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA SOURCES                                 │
├─────────────┬─────────────────┬─────────────────────────────────────┤
│   GitHub    │   SQL Database  │         MongoDB                     │
│  (HTTP/CSV) │   (MySQL)       │   (Category Enrichment)             │
└──────┬──────┴────────┬────────┴──────────────┬──────────────────────┘
       │               │                       │
       └───────────────┼───────────────────────┘
                       ▼
              ┌────────────────────┐
              │  Azure Data Factory │
              │   (Orchestration)   │
              └─────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────────┐
          │  Azure Data Lake Gen2       │
          ├─────────────────────────────┤
          │  🥉 BRONZE (Raw Data)        │
          │     - Raw CSV files          │
          │     - Original schema        │
          └─────────────┬───────────────┘
                        │
                        ▼
              ┌─────────────────────┐
              │  Azure Databricks   │
              │  (Spark Processing) │
              └─────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────────┐
          │  🥈 SILVER (Cleaned Data)    │
          │     - Cleaned & validated    │
          │     - Enriched with MongoDB  │
          │     - Standardized formats   │
          └─────────────┬───────────────┘
                        │
                        ▼
              ┌─────────────────────┐
              │  Azure Databricks   │
              │  (Aggregations)     │
              └─────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────────┐
          │  🥇 GOLD (Analytics Ready)   │
          │     - Business metrics       │
          │     - Aggregated tables      │
          │     - BI-optimized schemas   │
          └─────────────┬───────────────┘
                        │
                        ▼
              ┌─────────────────────┐
              │  Azure Synapse      │
              │  (Serving Layer)    │
              └─────────┬───────────┘
                        │
                        ▼
          ┌─────────────────────────────┐
          │    Power BI / Tableau       │
          │    (Visualization)          │
          └─────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose | Version/Details |
|------------|---------|-----------------|
| ![Azure Data Factory](https://img.shields.io/badge/-Azure_Data_Factory-0078D4?style=flat-square&logo=microsoft-azure) | **Orchestration & Ingestion** | ETL pipelines, data movement |
| ![Azure Data Lake Gen2](https://img.shields.io/badge/-Azure_Data_Lake-0078D4?style=flat-square&logo=microsoft-azure) | **Storage** | Bronze/Silver/Gold layer storage |
| ![Azure Databricks](https://img.shields.io/badge/-Databricks-FF3621?style=flat-square&logo=databricks) | **Data Processing** | Apache Spark transformations |
| ![Azure Synapse](https://img.shields.io/badge/-Synapse_Analytics-0078D4?style=flat-square&logo=microsoft-azure) | **Analytics & Serving** | External tables, analytical queries |
| ![MongoDB](https://img.shields.io/badge/-MongoDB-47A248?style=flat-square&logo=mongodb) | **Data Enrichment** | Category mapping (NoSQL) |
| ![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white) | **Relational Source** | Order payments data |
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | **Scripting** | Data transformation, database operations |
| ![Apache Spark](https://img.shields.io/badge/-Apache_Spark-E25A1C?style=flat-square&logo=apache-spark&logoColor=white) | **Distributed Processing** | PySpark for big data transformations |
| ![Power BI](https://img.shields.io/badge/-Power_BI-F2C811?style=flat-square&logo=power-bi&logoColor=black) | **Visualization** | Business intelligence dashboards |

---

## ✨ Features

### Data Pipeline Capabilities
- ✅ **Multi-source ingestion**: HTTP (GitHub CSVs), SQL, and NoSQL databases
- ✅ **Medallion architecture**: Industry-standard Bronze/Silver/Gold pattern
- ✅ **Data enrichment**: MongoDB integration for category translation
- ✅ **Scalable processing**: Apache Spark via Databricks for distributed computing
- ✅ **Analytics-ready**: Synapse Analytics for BI and reporting
- ✅ **Automated orchestration**: Azure Data Factory pipelines

### Business Metrics Calculated
- 📦 Order delivery performance and delays
- 💰 Payment analysis by type and installments
- ⭐ Customer review sentiment analysis
- 📍 Geographic distribution of orders
- 🏪 Seller and product performance metrics

### Data Quality & Governance
- 🔍 Data validation and cleansing
- 🗂️ Schema standardization
- 📊 Data lineage tracking
- 🔒 Secure credential management

---

## 📊 Dataset

**Olist Brazilian E-Commerce Dataset**

The project uses real-world e-commerce data from Olist, containing:

| Dataset | Records | Description |
|---------|---------|-------------|
| `olist_orders_dataset.csv` | 99,441 | Order information and status |
| `olist_order_items_dataset.csv` | 112,650 | Products within orders |
| `olist_customers_dataset.csv` | 99,441 | Customer demographics |
| `olist_products_dataset.csv` | 32,951 | Product catalog |
| `olist_sellers_dataset.csv` | 3,095 | Seller information |
| `olist_order_payments_dataset.csv` | 103,886 | Payment details |
| `olist_order_reviews_dataset.csv` | 99,224 | Customer reviews |
| `olist_geolocation_dataset.csv` | 1,000,163 | Geographic coordinates |
| `product_category_name_translation.csv` | 71 | Category translations |

**Total Data Volume**: ~1.3M records

---

## 🚀 Getting Started

### Prerequisites

- **Azure Account** (Free tier available)
- **Python 3.8+**
- **Git**
- Basic knowledge of SQL and Python
- (Optional) Power BI Desktop for visualizations

### Azure Resources Required

1. **Resource Group**
2. **Azure Data Lake Storage Gen2**
3. **Azure Data Factory**
4. **Azure Databricks Workspace**
5. **Azure Synapse Analytics**
6. **MongoDB Atlas** (Free tier)
7. **MySQL Database** (Free tier options available)

### Installation & Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/siddharths060/DataFlowX.git
cd DataFlowX
```

#### 2. Set Up Azure Resources
```bash
# Login to Azure
az login

# Create resource group
az group create --name DataFlowX-RG --location eastus

# Create storage account with Data Lake Gen2
az storage account create \
  --name dataflowxstorage \
  --resource-group DataFlowX-RG \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2 \
  --hierarchical-namespace true
```

#### 3. Configure Database Connection
Update credentials in `Database/connect_to_database.py`:
```python
hostname = "your-mysql-host"
database = "your-database-name"
username = "your-username"
password = "your-password"
port = "your-port"
```

#### 4. Upload Data to Bronze Layer
- Upload CSV files from `Data/` folder to Azure Data Lake Bronze container
- Or configure Data Factory to ingest from GitHub

#### 5. Configure MongoDB
- Set up MongoDB Atlas cluster
- Import `product_category_name_translation.csv`
- Update connection strings in Databricks notebooks

---

## 📂 Project Structure

```
DataFlowX/
│
├── Data/                                    # Raw datasets
│   ├── olist_customers_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   └── product_category_name_translation.csv
│
├── Database/                                # Database scripts
│   ├── connect_to_database.py              # MySQL connection test
│   └── add_table_and_values_to_database.py # Data upload script
│
├── LICENSE                                  # Project license
└── README.md                                # This file
```

---

## 🔄 Pipeline Workflow

### Step 1: Data Ingestion (Azure Data Factory)
```
Sources → ADF Pipelines → Bronze Layer (ADLS Gen2)
```
- HTTP connector for GitHub CSV files
- SQL connector for MySQL database
- MongoDB connector for enrichment data

### Step 2: Data Transformation (Databricks - Bronze → Silver)
```python
# Sample PySpark transformation
from pyspark.sql import functions as F

# Read from Bronze
df_orders = spark.read.parquet("/mnt/bronze/orders")

# Clean and transform
df_cleaned = df_orders \
    .dropDuplicates() \
    .na.drop() \
    .withColumn("order_date", F.to_date("order_purchase_timestamp")) \
    .withColumn("delivery_delay", 
                F.datediff("order_delivered_customer_date", 
                          "order_estimated_delivery_date"))

# Write to Silver
df_cleaned.write.mode("overwrite").parquet("/mnt/silver/orders")
```

### Step 3: Data Enrichment (MongoDB Integration)
- Join product data with category translations
- Standardize category names from Portuguese to English

### Step 4: Analytics Aggregation (Silver → Gold)
```python
# Calculate business metrics
order_metrics = df_orders \
    .groupBy("order_status", "customer_state") \
    .agg(
        F.count("order_id").alias("total_orders"),
        F.avg("delivery_delay").alias("avg_delay_days"),
        F.sum("payment_value").alias("total_revenue")
    )

# Write to Gold layer
order_metrics.write.mode("overwrite").parquet("/mnt/gold/order_metrics")
```

### Step 5: Serving Layer (Synapse Analytics)
```sql
-- Create external table in Synapse
CREATE EXTERNAL TABLE gold.order_metrics
WITH (
    LOCATION = '/gold/order_metrics/',
    DATA_SOURCE = AzureDataLake,
    FILE_FORMAT = ParquetFormat
);
```

---

## 📈 Business Insights Enabled

1. **Order Analytics**
   - Delivery performance tracking
   - Order status distribution
   - Peak ordering periods

2. **Customer Insights**
   - Geographic customer distribution
   - Customer satisfaction scores
   - Repeat customer analysis

3. **Financial Metrics**
   - Revenue by product category
   - Payment method preferences
   - Installment payment trends

4. **Operational Excellence**
   - Seller performance rankings
   - Delivery delay analysis
   - Inventory turnover rates

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

- ☑️ **Azure Cloud Services**: Data Factory, Databricks, Synapse, ADLS Gen2
- ☑️ **Big Data Processing**: Apache Spark, PySpark, distributed computing
- ☑️ **Data Architecture**: Medallion pattern, data lake design
- ☑️ **ETL/ELT**: Pipeline orchestration, data transformation
- ☑️ **Multi-source Integration**: HTTP, SQL, NoSQL data sources
- ☑️ **Data Modeling**: Dimensional modeling, star schema
- ☑️ **SQL & Python**: Advanced querying and scripting
- ☑️ **DevOps**: CI/CD for data pipelines (optional extension)

---

## 🔮 Future Enhancements

- [ ] Implement CI/CD with Azure DevOps
- [ ] Add real-time streaming with Event Hubs
- [ ] Machine learning integration (Azure ML)
- [ ] Advanced monitoring with Azure Monitor
- [ ] Data quality framework (Great Expectations)
- [ ] Cost optimization strategies
- [ ] Delta Lake integration for ACID transactions
- [ ] Automated testing for data pipelines

---

## 📚 Resources & References

### Tutorials
- [End-to-End Big Data Engineering Project - Part 1](https://www.youtube.com/watch?v=K0KPFoWwvwg)
- [End-to-End Big Data Engineering Project - Part 2](https://www.youtube.com/watch?v=zxYyJkNB3Q0)

### Documentation
- [Azure Data Factory Documentation](https://docs.microsoft.com/azure/data-factory/)
- [Azure Databricks Documentation](https://docs.microsoft.com/azure/databricks/)
- [Azure Synapse Analytics Documentation](https://docs.microsoft.com/azure/synapse-analytics/)
- [Medallion Architecture Pattern](https://docs.databricks.com/lakehouse/medallion.html)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

---

## 👤 Author

**Siddharth**

- GitHub: [@siddharths060](https://github.com/siddharths060)
- Project: [DataFlowX](https://github.com/siddharths060/DataFlowX)

---

## ⭐ Show Your Support

If this project helped you learn Azure data engineering, please give it a ⭐️!

---

<div align="center">

**Built with ❤️ using Azure Cloud Services**

![Microsoft Azure](https://img.shields.io/badge/Built_on-Microsoft_Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)

</div>
