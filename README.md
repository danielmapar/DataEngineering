# Data Engineer Nanodegree 

## Welcome to the Nanodegree Program

### Introduction to Data Engineering

* ![intro](./images/into.png)

* ![de_tasks](./images/de_tasks.png)

## Data Modeling

### Introduction to Data Modeling

* Introduction to Databases and DBMS
    * Databases: A database is a structured repository or collection of data that is stored and retrieved electronically for use in applications. Data can be stored, updated, or deleted from a database.

    * Database Management System (DBMS): The software used to access the database by the user and application is the database management system. Check out these few links describing a DBMS in more detail.

* DDL = Data Definition Language 
    * Materialize a logical data model to a database model (physical data modeling)

* ![relational_model](./images/relational_model.png)

* A schema is a collection of tables in some database terminology.

* ![advantages_relational_dbs](./images/advantages_relational_dbs.png)

    * **Flexibility for writing in SQL queries**: With SQL being the most common database query language.
    * **Modeling the data not modeling queries**
    * Ability to do **JOINS**
    * Ability to do **aggregations** (SUM, COUNT, AVG) and analytics
    * **Secondary Indexes available**: You have the advantage of being able to add another index to help with quick searching.
    * **Smaller data volumes**: If you have a smaller data volume (and not big data) you can use a relational database for its simplicity.
    * **ACID Transactions**: Allows you to meet a set of properties of database transactions intended to guarantee validity even in the event of errors, power failures, and thus maintain data integrity.
    * Easier to change to business requirements

* ACID Transactions
    * Properties of database transactions intended to guarantee validity even in the event of errors or power failures.

    * `Atomicity`: The whole transaction is processed or nothing is processed. A commonly cited example of an atomic transaction is money transactions between two bank accounts. The transaction of transferring money from one account to the other is made up of two operations. First, you have to withdraw money in one account, and second you have to save the withdrawn money to the second account. An atomic transaction, i.e., when either all operations occur or nothing occurs, keeps the database in a consistent state. This ensures that if either of those two operations (withdrawing money from the 1st account or saving the money to the 2nd account) fail, the money is neither lost nor created. Source Wikipedia for a detailed description of this example.

    * `Consistency`: Only transactions that abide by constraints and rules are written into the database, otherwise the database keeps the previous state. The data should be correct across all rows and tables. Check out additional information about consistency on Wikipedia.

    * `Isolation`: Transactions are processed independently and securely, order does not matter. A low level of isolation enables many users to access the data simultaneously, however this also increases the possibilities of concurrency effects (e.g., dirty reads or lost updates). On the other hand, a high level of isolation reduces these chances of concurrency effects, but also uses more system resources and transactions blocking each other. Source: Wikipedia

    * `Durability`: Completed transactions are saved to database even in cases of system failure. A commonly cited example includes tracking flight seat bookings. So once the flight booking records a confirmed seat booking, the seat remains booked even if a system failure occurs. Source: Wikipedia.

* When Not to Use a Relational Database
    * **Have large amounts of data**: Relational Databases are not distributed databases (by default) and because of this they can only scale vertically by adding more storage in the machine itself. You are limited by how much you can scale and how much data you can store on one machine. You cannot add more machines like you can in NoSQL databases.
    * **Need to be able to store different data type formats**: Relational databases are not designed to handle unstructured data (not true, it can handle JSON/XML).
    * Need high throughput -- fast reads: While ACID transactions bring benefits, they also slow down the process of **reading and writing data** (if you are writing it may impact reads). If you need very fast reads and writes, using a relational database may not suit your needs.
    * **Need a flexible schema**: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space (not necessarily).
    * **Need high availability**: The fact that relational databases are not distributed (and even when they are, they have a coordinator/worker architecture), they have a single point of failure. When that database goes down, a fail-over to a backup system occurs and takes time.
    * Need horizontal scalability: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data.

* `l1-demo-1-creating-a-table-with-postgres.ipynb`

* Introduction to NoSQL Databases
    * NoSQL databases were created do some of the issues faced with Relational Databases. NoSQL databases have been around since the 1970’s but they became more popular in use since the 2000’s as data sizes has increased, and outages/downtime has decreased in acceptability.

    * NoSQL Database Implementations:
        * Apache Cassandra (Partition Row store)
        * MongoDB (Document store)
        * DynamoDB (Key-Value store)
        * Apache HBase (Wide Column Store)
        * Neo4J (Graph Database)
    
    * ![cassandra1](./images/cassandra1.png)

    * ![cassandra2](./images/cassandra2.png)

* ![cassandra3](./images/cassandra3.png)

* Common Questions:
    * What type of companies use Apache Cassandra?
        * All kinds of companies. For example, Uber uses Apache Cassandra for their entire backend. Netflix uses Apache Cassandra to serve all their videos to customers. Good use cases for NoSQL (and more specifically Apache Cassandra) are :

            * Transaction logging (retail, health care)
            * Internet of Things (IoT)
            * Time series data
            * Any workload that is heavy on writes to the database (**since Apache Cassandra is optimized for writes**).

* Would Apache Cassandra be a hindrance (a thing that provides resistance, delay, or obstruction to something or someone) for my analytics work? If yes, why?
    * Yes, if you are trying to do analysis, such as using `GROUP BY` statements. Since Apache Cassandra requires data modeling based on the query you want, you can't do ad-hoc queries. However you can add clustering columns into your data model and create new tables.

* When to use a NoSQL Database  
    * **Need to be able to store different data type formats**: NoSQL was also created to handle different data configurations: structured, semi-structured, and unstructured data. JSON, XML documents can all be handled easily with NoSQL.
    * **Large amounts of data**: Relational Databases are **not distributed databases (by design)** and because of this they can only scale vertically by adding more storage in the machine itself. NoSQL databases were created to be able to be horizontally scalable. The more servers/systems you add to the database the more data that can be hosted with high availability and low latency (fast reads and writes).
    * **Need horizontal scalability**: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data
    * **Need high throughput**: While **ACID** transactions bring benefits they also **slow down the process of reading and writing data** (locks on pages). If you need very fast reads and writes using a relational database may not suit your needs.
    * **Need a flexible schema**: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.
    * **Need high availability**: Relational databases have a single point of failure. When that database goes down, a failover to a backup system must happen and takes time.

* When NOT to use a NoSQL Database?
    * **When you have a small dataset**: NoSQL databases were made for big datasets not small datasets and while it works it wasn’t created for that.
    * **When you need ACID Transactions**: If you need a consistent database with ACID transactions, then most NoSQL databases will not be able to serve this need. NoSQL database are eventually consistent and do not provide ACID transactions. However, there are exceptions to it. Some non-relational databases like MongoDB can support ACID transactions.
    * **When you need the ability to do JOINS across tables**: NoSQL does not allow the ability to do `JOINS`. This is not allowed as this will result in full table scans.
    * **If you want to be able to do aggregations and analytics**
    * **If you have changing business requirements** : Ad-hoc queries are possible but difficult as the data model was done to fix particular queries
    * **If your queries are not available and you need the flexibility** : You need your queries in advance. If those are not available or you will need to be able to have flexibility on how you query your data you might need to stick with a relational database

* `l1-demo-2-creating-a-table-with-apache-cassandra.ipynb`

* ![cassandra4](./images/cassandra4.png)

    * **The first element in our PRIMARY KEY is what we call a partition key**

* `l1-exercise-2-solution-creating-a-table-with-cassandra.ipynb`

### Relational Data Models

* Importance of Relational Databases:
    * **Standardization of data model**: Once your data is transformed into the rows and columns format, your data is standardized and you can query it with SQL
    * **Flexibility in adding and altering tables**: Relational databases gives you flexibility to add tables, alter tables, add and remove data.
    * **Data Integrity**: Data Integrity is the backbone of using a relational database.
    * **Structured Query Language (SQL)**: A standard language can be used to access the data with a predefined language.
    * **Simplicity** : Data is systematically stored and modeled in tabular format.
    * **Intuitive Organization**: The spreadsheet format is intuitive but intuitive to data modeling in relational databases.

* **Online Analytical Processing (OLAP)**:

    * Databases optimized for these workloads allow for complex analytical and ad hoc queries, including aggregations. These type of databases are **optimized for reads**.

* **Online Transactional Processing (OLTP)**:

    * Databases optimized for these workloads allow for **less complex queries in large volume**. The types of queries for these databases are **read, insert, update, and delete.**

    * The key to remember the difference between OLAP and OLTP is **analytics (A) vs transactions (T)**. If you want to get the price of a shoe then you are using OLTP (this has very little or no aggregations). If you want to know the total stock of shoes a particular store sold, then this requires using OLAP (since this will require aggregations).

    * **OLTP queries will have little aggregations really, if any, while OLAP will heavily focus on aggregations.**

* Normalization and Denormalization

    * Normalization will feel like a natural process, you will **reduce the number of copies of the data and increase the likelihood that your data is correct in all locations.**

    * Normalization organizes the columns and tables in a database to **ensure that their dependencies are properly enforced by database integrity constraints.**

    * We don’t want or need extra copies of our data, this is data redundancy. We want to be able to **update data in one place and have that be the source of truth, that is data integrity.**

    * **Denormalization** will not feel as natural, as you will have duplicate copies of data, and tables will be more focused on the queries that will be run.

    * ![normalized1](./images/normalized1.png)  

    * Here is an example table we will be using later in our demo and exercises. Let’s say we have a table called music_library, looks pretty standard but this is not a normalized table.

    * ![normalized](./images/normalized.png) 

* **Objectives of Normal Form**:
    * To free the database from unwanted insertions, updates, & deletion dependencies
    * To reduce the need for refactoring the database as new types of data are introduced
    * To make the relational model more informative to users
    * To make the database neutral to the query statistics

* **How to reach First Normal Form (1NF)**:
    * **Atomic values**: each cell contains unique and single values
    * Be able to add data without altering tables
    * Separate different relations into different tables
    * Keep **relationships** between tables together with **foreign keys**

* Second Normal Form (2NF):
    * Have reached 1NF
    * **All columns in the table** must rely on the **Primary Key**

* Third Normal Form (3NF):

    * Must be in 2nd Normal Form
    * No transitive dependencies
    * **Remember, transitive dependencies you are trying to maintain is that to get from A-> C, you want to avoid going through B.**

* When to use 3NF:

    * When you want to update data, we want to be able to do in just 1 place. We want to avoid updating the table in the Customers Detail table (in the example in the lecture slide).

* Exercise: `Lesson 2 Exercise 1 Creating Normalized Tables--ANSWER KEY.ipynb`

* Denormalization

    * ![denormalization](./images/denormalization.png)

    * **JOINS on the database allow for outstanding flexibility but are extremely slow.** If you are dealing with heavy reads on your database, you may want to think about denormalizing your tables. You get your data into normalized form, and then you proceed with denormalization. So, denormalization comes after normalization.

    * ![denormalization2](./images/denormalization2.png)

    * `lesson-2-demo-2-creating-denormalized-tables.ipynb`

    * Let's take a moment to make sure you understand what was in the demo regarding denormalized vs. normalized data. These are important concepts, so make sure to spend some time reflecting on these.

    * **Normalization** is about trying to **increase data integrity by reducing the number of copies of the data**. Data that needs to be added or updated will be done in as few places as possible.

    * **Denormalization** is trying to increase performance by reducing the number of joins between tables (as joins can be slow). Data integrity will take a bit of a potential hit, as there will be more copies of the data (**to reduce JOINS**).

    * `Lesson 2 Exercise 2 Creating Denormalized Tables--ANSWER KEY.ipynb`

* Fact and Dimensions Table

    * The following image shows the relationship between the fact and dimension tables for the example shown in the video. As you can see in the image, the unique primary key for each Dimension table is included in the Fact table.

    * In this example, it helps to think about the Dimension tables providing the following information:

        * `Where` the product was bought? (Dim_Store table)
        * `When` the product was bought? (Dim_Date table)
        * `What` product was bought? (Dim_Product table)

    * The Fact table provides the metric of the business process (here Sales).

        * `How` many units of products were bought? (Fact_Sales table)
    
    * ![fact_and_dims](./images/fact_and_dims.png) 

    * If you are familiar with `Entity Relationship Diagrams (ERD)`, you will find the depiction of `STAR and SNOWFLAKE` schemas in the demo familiar. The `ERDs` show the data model in a concise way that is also easy to interpret. `ERDs` can be used for any data model, and are not confined to `STAR or SNOWFLAKE` schemas. Commonly available tools can be used to generate ERDs. However, more important than creating an ERD is to learn more about the data through conversations with the data team so as a data engineer you have a strong understanding of the data you are working with.

    * ![dimension](./images/dimension.png)

    * ![fact](./images/fact.png)

* **Star Schema**

    * Star Schema is the simplest style of data mart schema. The star schema consists of one of more fact tables referencing any number of dimension tables.

    * Gets its name from the physical model resembling a star shape
    * A fact table is at its center
    * Dimension table surrounds the fact table representing the star’s points.

    * Benefits of Star Schema
        * **Getting a table into 3NF is a lot of hard work, JOINs can be complex even on simple data**
        * Star schema allows for the relaxation of these rules and makes **queries easier with simple JOINS**
        * Aggregations perform **calculations and clustering of our data** so that we do not have to do that work in our application. Examples : **COUNT, GROUP BY etc**
    
    * ![star](./images/star.png)

    * ![star_example](./images/star_example.png)

* **Snowflake Schema**
    * Star Schema is a special, simplified case of the snowflake schema.
    * **Star schema does not allow for one to many relationships while the snowflake schema does.**
    * **Snowflake schema is more normalized** than Star schema but only in 1NF or 2NF

    * ![snowflake](./images/snowflake.png)

    * `lesson-2-demo-3-creating-fact-and-dimension-tables-with-star-schema.ipynb`

    * `Lesson 2 Exercise3_Solution Creating Fact and Dimension Tables with Star Schema-ANSWER KEY.ipynb`

* Data Definition and Constraints

    * The `CREATE` statement in `SQL` has a few important constraints that are highlighted below.

    * **NOT NULL**
        * The `NOT NULL` constraint indicates that the column cannot contain a null value.

        * Here is the syntax for adding a `NOT NULL` constraint to the `CREATE` statement:

        * ```sql
            CREATE TABLE IF NOT EXISTS customer_transactions (
                customer_id int NOT NULL, 
                store_id int, 
                spent numeric
            );
            ```
    
    * You can add `NOT NULL` constraints to more than one column. Usually this occurs when you have a `COMPOSITE KEY`, which will be discussed further below.

    * Here is the syntax for it:

        * ```sql
            CREATE TABLE IF NOT EXISTS customer_transactions (
                customer_id int NOT NULL, 
                store_id int NOT NULL, 
                spent numeric
            );
            ```

    * **UNIQUE**
        * The **UNIQUE** constraint is used to specify that the data across all the rows in one column are unique within the table. The **UNIQUE** constraint can also be used for multiple columns, so that the combination of the values across those columns will be **unique within the table**. In this latter case, the values within 1 column do not need to be unique.

        * Let's look at an example.

        * ```sql
            CREATE TABLE IF NOT EXISTS customer_transactions (
                customer_id int NOT NULL UNIQUE, 
                store_id int NOT NULL UNIQUE, 
                spent numeric 
            );
            ```
        * Another way to write a `UNIQUE` constraint is to add a table constraint using commas to separate the columns.

        * ```sql
            CREATE TABLE IF NOT EXISTS customer_transactions (
                customer_id int NOT NULL, 
                store_id int NOT NULL, 
                spent numeric,
                UNIQUE (customer_id, store_id, spent)
            );
            ```
    
    * **PRIMARY KEY**
        * The **PRIMARY KEY** constraint is defined on a **single column**, and **every table should contain a primary key**. The values in this column uniquely identify the rows in the table. **If a group of columns are defined as a primary key, they are called a composite key**. That means the combination of values in these columns will uniquely identify the rows in the table. By default, the **PRIMARY KEY constraint has the unique and not null constraint built into it**.

        * Let's look at the following example:

        * ```sql
            CREATE TABLE IF NOT EXISTS store (
                store_id int PRIMARY KEY, 
                store_location_city text,
                store_location_state text
            );
            ```
        
        * Here is an example for a group of columns serving as `composite key`.

        * ```sql
            CREATE TABLE IF NOT EXISTS customer_transactions (
                customer_id int, 
                store_id int, 
                spent numeric,
                PRIMARY KEY (customer_id, store_id)
            );
            ```

    * Upsert

        * In `RDBMS language`, the term `upsert` refers to the idea of `inserting a new row in an existing table`, or `updating the row if it already exists in the table`. The action of updating or inserting has been described as `"upsert"`.

        * The way this is handled in PostgreSQL is by using the `INSERT` statement in combination with the `ON CONFLICT` clause.

        * **INSERT**

            * The **INSERT** statement adds in new rows within the table. The values associated with specific target columns can be added in any order.

            * Let's look at a simple example. We will use a customer address table as an example, which is defined with the following CREATE statement:

            * ```sql
                CREATE TABLE IF NOT EXISTS customer_address (
                    customer_id int PRIMARY KEY, 
                    customer_street varchar NOT NULL,
                    customer_city text NOT NULL,
                    customer_state text NOT NULL
                );
                ```
            
            * ```sql
                INSERT into customer_address (
                VALUES
                    (432, '758 Main Street', 'Chicago', 'IL'
                );
                ```
        
        * Now let's assume that the customer moved and we need to update the customer's address. However we do not want to add a new customer id. In other words, if there is any conflict on the `customer_id`, we do not want that to change.

        * This would be a good candidate for using the `ON CONFLICT DO NOTHING` clause.

        * ```sql
            INSERT INTO customer_address (customer_id, customer_street, customer_city, customer_state)
            VALUES
            (
            432, '923 Knox Street', 'Albany', 'NY'
            ) 
            ON CONFLICT (customer_id) 
            DO NOTHING;
            ```

        * Now, let's imagine we want to add more details in the existing address for an existing customer. This would be a good candidate for using the `ON CONFLICT DO UPDATE` clause.

        * ```sql
            INSERT INTO customer_address (customer_id, customer_street)
            VALUES
                (
                432, '923 Knox Street, Suite 1' 
            ) 
            ON CONFLICT (customer_id) 
            DO UPDATE
                SET customer_street  = EXCLUDED.customer_street;
            ```

### NoSQL Data Models

* ![no_sql](./images/no_sql.png) 

* ![cassandra](./images/cassandra.png)

* When to Use NoSQL:
    * Need high **Availability** in the data: 
        * Indicates the system is always up and there is no downtime
    * Have Large Amounts of Data
    * Need Linear Scalability: 
        * The need to add more nodes to the system so performance will increase linearly
    * Low Latency: 
        * Shorter delay before the data is transferred once the instruction for the transfer has been received.
    * Need fast reads and write

* Eventual Consistency:

    * Over time (if no new changes are made) each copy of the data will be the same, but if there are new changes, the data may be different in different locations. The data may be inconsistent for only milliseconds. There are workarounds in place to prevent getting stale data.

* Commonly Asked Questions:

    * What does the network look like? Can you share any examples?

        * In Apache Cassandra every node is connected to every node -- it's peer to peer database architecture.

    * Is data deployment strategy an important element of data modeling in Apache Cassandra?

        * Deployment strategies are a great topic, but have very little to do with data modeling. Developing deployment strategies focuses on determining how many clusters to create or determining how many nodes are needed. These are topics generally covered under database architecture, database deployment and operations, which we will not cover in this lesson.

        * In general, the size of your data and your data model can affect your deployment strategies. You need to think about how to create a cluster, how many nodes should be in that cluster, how to do the actual installation. More information about deployment strategies can be found on this DataStax documentation page
    
* Cassandra Architecture

    * We are not going into a lot of details about the Apache Cassandra Architecture. However, if you would like to learn more about it for your job, here are some links that you may find useful.

    * Apache Cassandra Data Architecture:


        * [Understanding the architecture](https://docs.datastax.com/en/archived/cassandra/3.0/cassandra/architecture/archTOC.html)
        * [Cassandra Architecture](https://www.tutorialspoint.com/cassandra/cassandra_architecture.htm)

* ![cassandra_eventual](./images/cassandra_eventual.png)

* The design goal of Cassandra is to handle big data workloads across multiple nodes without any single point of failure. Cassandra has peer-to-peer distributed system across its nodes, and data is distributed among all the nodes in a cluster.

    * All the nodes in a cluster play the same role. Each node is independent and at the same time interconnected to other nodes.

    * Each node in a cluster can accept read and write requests, regardless of where the data is actually located in the cluster.

    * When a node goes down, read/write requests can be served from other nodes in the network.

* Data Replication in Cassandra

    * In Cassandra, one or more of the nodes in a cluster act as replicas for a given piece of data. If it is detected that some of the nodes responded with an out-of-date value, Cassandra will return the most recent value to the client. After returning the most recent value, Cassandra performs a read repair in the background to update the stale values.

    * The following figure shows a schematic view of how Cassandra uses data replication among the nodes in a cluster to ensure no single point of failure.

    * ![data_replication](./images/data_replication.jpeg)

* CAP Theorem:

    * **Consistency**: Every read from the database gets the latest (and correct) piece of data or an error

    * **Availability**: Every request is received and a response is given -- **without a guarantee that the data is the latest update**

    * **Partition Tolerance**: The system continues to work **regardless of losing network connectivity between nodes**

* Commonly Asked Questions:

    * Is **Eventual Consistency the opposite of what is promised by SQL database per the ACID principle?**
        * Much has been written about how Consistency is interpreted in the ACID principle and the CAP theorem. **Consistency in the ACID principle refers to the requirement that only transactions that abide by constraints and database rules are written into the database, otherwise the database keeps previous state**. In other words, the data should be correct across all rows and tables. **However, consistency in the CAP theorem refers to every read from the database getting the latest piece of data or an error.**

    * Which of these combinations is desirable for a production system - Consistency and Availability, Consistency and Partition Tolerance, or Availability and Partition Tolerance?
        * As the CAP Theorem Wikipedia entry says, **"The CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability."** So there is **no such thing as Consistency and Availability** in a distributed database since it must always tolerate network issues. You can only have *Consistency and Partition Tolerance (CP)** or **Availability and Partition Tolerance (AP)**. Remember, relational and non-relational databases do different things, and that's why most companies have both types of database systems.

    * **Does Cassandra meet just Availability and Partition Tolerance in the CAP theorem?**
        * According to the CAP theorem, a database can actually only guarantee two out of the three in CAP. So supporting Availability and Partition Tolerance makes sense, since Availability and Partition Tolerance are the biggest requirements.
    
    * If Apache Cassandra is not built for consistency, won't the analytics pipeline break?
        * If I am trying to do analysis, such as determining a trend over time, e.g., how many friends does John have on Twitter, and if you have one less person counted because of "eventual consistency" (the data may not be up-to-date in all locations), that's OK. In theory, that can be an issue but only if you are not constantly updating. If the pipeline pulls data from one node and it has not been updated, then you won't get it. Remember, in Apache Cassandra it is about **Eventual Consistency**.
    
    * ![cap_theorem](./images/cap_theorem.png)

    * ![cassandra_denormalized](./images/cassandra_denormalized.png)

* ![cassandra_datamodeling](./images/cassandra_datamodeling.png)

* Data Modeling in Apache Cassandra:
    * **Denormalization is not just okay -- it's a must**
    * Denormalization must be done for fast reads
    * **Apache Cassandra has been optimized for fast writes**
    * **ALWAYS think Queries first**
    * **One table per query is a great strategy**
    * Apache Cassandra does not allow for JOINs between tables

    * Commonly Asked Questions:
        * I see certain downsides of this approach, since in a production application, requirements change quickly and I may need to improve my queries later. Isn't that a downside of Apache Cassandra?
            * In Apache Cassandra, you want to model your data to your queries, and **if your business need calls for quickly changing requirements, you need to create a new table to process the data**. That is a requirement of Apache Cassandra. If your business needs calls for ad-hoc queries, these **are not a strength of Apache Cassandra**. However keep in mind that it is **easy to create a new table that will fit your new query**.
        
    * ![relational_vs_cassandra](./images/relational_vs_cassandra.png)

* Cassandra Query Language (CQL)
    * ![cql](./images/cql.png) 

    * Cassandra query language is the way to interact with the database and is very similar to SQL. The following are not supported by CQL
        * JOINS
        * GROUP BY
        * Subqueries

* `lesson-3-demo-1-2-queries-2-tables.ipynb`

* In this article, we learned that Cassandra uses a partition key or a composite partition key to determine the placement of the data in a cluster. **The clustering key provides the sort order of the data stored within a partition.** All of these keys also uniquely identify the data

* `Lesson 3 Exercise 1 Three Queries Three Tables-ANSWER KEY.ipynb`

* Primary Key

    * ![primary_key](./images/primary_key.png)

    * Must be unique
    * The `PRIMARY KEY` is made up of either just the `PARTITION KEY` or may also include additional `CLUSTERING COLUMNS`
    * A Simple  `PRIMARY KEY` is just one column that is also the `PARTITION KEY`. A Composite `PRIMARY KEY` is made up of more than one column and will assist in creating a unique value and in your retrieval queries
    * The `PARTITION KEY` will determine the distribution of data across the system

    * `lesson-3-demo-2-primary-key.ipynb`

* `Lesson 3 Exercise 2 Primary Key-ANSWER KEY.ipynb`

* Clustering Columns:
    * The clustering column will sort the data in `sorted ascending` order, e.g., alphabetical order.*
    * **More than one clustering column can be added (or none!)**
    * From there the **clustering columns will sort in order of how they were added to the primary key**

* Commonly Asked Questions:

    * How many `clustering columns` can we add?

        * You can use **as many clustering columns as you would like**. You cannot use the clustering columns out of order in the `SELECT` statement. You may choose to omit using a clustering column in your `SELECT` statement. That's OK. **Just remember to use them in order when you are using the `SELECT` statement.**

    * Additional Resources:
        * [DataStax](https://docs.datastax.com/en/cql/3.3/cql/cql_using/useCompoundPrimaryKeyConcept.html)
        * **(i.e. you can query by just the partition key, even if you have clustering keys defined)**
    
    * ![clustering_columns](./images/clustering_columns.png) 

    * `lesson-3-demo-3-clustering-column.ipynb`

* Results in `Cassandra CQL` will always come back in order of the `hashed token value` of the `partition key` (which you can see by using token). Within the partition keys, your `CLUSTERING ORDER` will be enforced.

* That's key to understand. **Result set ordering in Cassandra can only be enforced within a partition key. You have no control over the order that the partition keys come back in.**

* `Lesson 3 Exercise 3 Clustering Column-ANSWER KEY.ipynb`

* `WHERE` clause

    * Data Modeling in Apache Cassandra is query focused, and that focus needs to be on the WHERE clause
    * **Failure to include a WHERE clause will result in an error**

* Additional Resource
    **AVOID using "ALLOW FILTERING"**: Here is a reference [in DataStax](https://www.datastax.com/dev/blog/allow-filtering-explained-2) that explains ALLOW FILTERING and why you should not use it.

* Commonly Asked Questions:
    * Why do we need to use a `WHERE` statement since we are not concerned about analytics? Is it only for debugging purposes?

        * The `WHERE` statement is allowing us to do the **fast reads**. With Apache Cassandra, we are talking about big data -- think terabytes of data -- so we are making it fast for read purposes. **Data is spread across all the nodes**. By using the `WHERE` statement, we know **which node to go to**, from which node to get that data and serve it back. For example, imagine we have 10 years of data on 10 nodes or servers. So 1 year's data is on a separate node. By using the `WHERE year = 1` statement we know which node to visit fast to pull the data from.

* Important note: **the partition key is the minimum-specifier needed to perform a query using a where clause**. If you have a composite partition key, like the following

    * eg: `PRIMARY KEY((col1, col2), col10, col4))`

* You can perform query only by passing at least both `col1` and `col2`, these are the 2 columns that define the `partition key`. The "general" rule to make query is you must pass at least **all partition key columns, then you can add optionally each clustering key in the order they're set**.

* `lesson-3-demo-4-using-the-where-clause.ipynb`

## Cloud Data Warehouses

### Introduction to Data Warehouses

* Operational vs Analytical Business Processes
    * Operational Processes: Make it Work
        * Find goods & make orders (for customers)
        * Stock and find goods (for inventory staff)
        * Pick up & deliver goods (for delivery staff)
    
    * Analytical Processes: What is Going On?
        * Assess the performance of sales staff (for HR)
        * See the effect of different sales channels (for marketing)
        * Monitor sales growth (for management)
    
* ![oltp_vs_olap](./images/oltp_vs_olap.png)

* Data Warehouse Definitions
    * A data warehouse is a copy of transaction data specifically structured for query and analysis. - `Kimball`
    * A data warehouse is a subject-oriented, integrated, nonvolatile, and time-variant collection of data in support of management's decisions. - `Inmon`
    * A data warehouse is a system that retrieves and consolidates data periodically from the source systems into a dimensional or normalized data store. It usually keeps years of history and is queried for business intelligence or other analytical activities. It is typically updated in batches, not every time a transaction happens in the source system. - `Rainard`

* Data Warehouse: Technical Perspective
    * Extract the data from the source systems used for operations, transform the data, and load it into a dimensional model

* ![dwh_tech](./images/dwh_tech.png)

* Dimensional Model Review
    * Goals of the Star Schema
        * Easy to understand
        *  **Fast analytical query performance**
    * Fact Tables
        * **Record business events, like an order, a phone call, a book review**
        * Fact tables **columns record events recorded in quantifiable metrics** like quantity of an item, duration of a call, a book rating
    * Dimension Tables
        * Record the **context of the business events, e.g. who, what, where, why, etc..**
        * **Dimension tables columns contain attributes like the store at which an item is purchased or the customer who made the call, etc.**

    * ![star_schema_vs_3nf](./images/star_schema_vs_3nf.png) 

    * ![fact_or_dimensions_table](./images/fact_or_dimensions_table.png)

    * ![naive_etl](./images/naive_etl.png)

    * ![3nf_vs_star](./images/3nf_vs_star.png)

    * ![fact_vs_dimension](./images/fact_vs_dimension.png)

    * ![fact_vs_dimension2](./images/fact_vs_dimension2.png)


* Demo 01 -  Sakila Star Schema & ETL: `L1 E1 - Solution.ipynb`

* ![dwh_architectures](./images/dwh_architectures.png)

* **Kimball's Bus Architecture**

    * ![kimball](./images/kimball.png)

    * ETL: A Closer Look
        * Extracting:
            * Transfer data to the warehouse
        * Transforming:
            * Integrates many sources together
            * Possibly cleansing: inconsistencies, duplication, missing values, etc..
            * Possibly producing diagnostic metadata
        * Loading:
            * Structuring and loading the data into the dimensional data model

    * ![kimball_1](./images/kimball_1.png)

* **Independent Data Marts**

    * Departments have separate ETL processes & dimensional models
    * These separate dimensional models are called “Data Marts”
    * Different fact tables for the same events, no conformed dimensions
    * Uncoordinated efforts can lead to inconsistent views
    * Despite awareness of the emergence of this architecture from departmental autonomy, it is generally discouraged

    * ![independent_data_marts](./images/independent_data_marts.png)

* **Inmon's Corporate Information Factory (CIF)**

    * ![inmon](./images/inmon.png)

    * 2 ETL Process
    * Source systems → 3NF database
    * 3NF database → Departmental Data Marts
    * The 3NF database acts an enterprise-wide data store.
    * Single integrated source of truth for data-marts
    * Could be accessed by end-users if needed
    * Data marts dimensionally modeled & unlike Kimball’s dimensional models, they are mostly aggregated

    * ![cif](./images/cif.png)

* **Best of Both Worlds: Hybrid Kimball Bus & Inmon CIF**

    * ![hybrid_kimball_and_inmon](./images/hybrid_kimball_and_inmon.png)

    * Removes Data Marts
    * Brings back conformed dimensions across the business
    * Exposes the enterprise data warehouse

* OLAP Cubes

    * ![olap_cubes](./images/olap_cubes.png)

    * Once we have a `star schema`, we can create `OLAP` cubes.
        * An OLAP cube is an **aggregation of at a number of dimensions**
            * Movie, Branch, Month
        * Easy to communicate to business users

* OLAP Cubes Operations: Roll-up & Drill Down

    * ![cube_rollup_drill_down](./images/cube_rollup_drill_down.png)

    * `Roll-up`: Sum up the sales of each city by Country: e.g. US, France (less columns in branch dimension)

    * `Drill-Down`: Decompose the sales of each city into smaller districts (more columns in branch dimension)

* OLAP Cubes: Slice and Dice

    * `Slice`: Reducing `N` dimensions to `N-1` dimensions by restricting one dimension to a single value

    * ![olap_slice](./images/olap_slice.png)

    * `Dice`: Same dimensions but computing a sub-cube by restricting, some of the values of the dimensions

    * ![olap_dice](./images/olap_dice.png)

* ![olap_operations](./images/olap_operations.png)

* **OLAP Cubes: Query Optimization**

    * ![olap_q_optm](./images/olap_q_optm.png)

    * `GROUP by CUBE` Statement
        * Do one pass through the facts table
        * Aggregate all possible combinations.
    
    * ![group_by_cube](./images/group_by_cube.png)
        * Think of `grouping sets` as passes. At first you group by nothing, the by `month`, then `country` and then both.
    
    * ![group_by_cube2](./images/group_by_cube2.png) 

        * `group by CUBE` is the same as `grouping sets`
    
    * ![group_by_cube3](./images/group_by_cube3.png)
        * Various permutations of aggregations in a single table.

* Notebook: `L1 E2 - 0 - OLAP Cubes - Solution.ipynb`

* ![olap_cubes_tech](./images/olap_cubes_tech.png)

* Column format in `ROLAP`: `L1 E3 - Columnar Vs Row Storage - Solution.ipynb`

### Introduction to Cloud Computing on AWS

* Did not take notes of this section, it mostly covers the basics of AWS and how to spin services (Redshift, IAM roles, S3, etc.)

### Implementing Date Warehouses on AWS

* Requirements for Implementation of a Data Warehouse
    * `Data Sources`: Different types, skill sets, upgrades, locations, etc. (high heterogeneity)
    * `ETL`: Many processes - a “grid” of machines with different schedules and pipeline complexities
    * More resources need to be added as data increases. We have different workloads; some need one machine and some need many (scalability & elasticity)
    * `Business Intelligence Apps & Visualizations`: Also need a hybrid deployment of tools for interaction, reporting, visualizations, etc.

    * ![l3-datawarehousing-on-aws](./images/l3-datawarehousing-on-aws.png)

* Data Warehouse Implementation Choices
    * On-Premise
        * Heterogeneity, scalability, elasticity of the tools, technologies, and processes
        * Need for diverse IT staff skills & multiple locations
        * Cost of ownership
    * Cloud:
        * Lower barrier to entry
        * May add as you need - it’s ok to change your opinion
        * Scalability & elasticity out of the box

* ![dwh_cloud](./images/dwh_cloud.png)

* Dimensional Model Storage on AWS
    * Cloud-Managed
        * Amazon RDS, Amazon DynamoDB, Amazon S3
        * Re-use of expertise; way less IT Staff for security, upgrades, etc. and way less OpEx
        * Deal with complexity with techniques like: “Infrastructure as code”
    * Self-Managed
        * EC2 + Postgresql, EC2 + Cassandra
        * EC2 + Unix FS
        * Always “catch-all” option if needed

* ![amazon_redshift](./images/amazon_redshift.png)

* ![amazon_redshift](./images/amazon_redshift1.png)

* ![amazon_redshift](./images/amazon_redshift2.png)

    * Redshift tables are partitioned and partitions are processed in parallel

    * Amazon Redshift is a cloud-managed, column- oriented, MPP database

* ![amazon_redshift](./images/amazon_redshift3.png)

* ![amazon_redshift](./images/amazon_redshift4.png)

* ![amazon_redshift](./images/amazon_redshift5.png)

* Amazon Redshift Architecture
    * **LeaderNode**:
        * `Coordinates compute nodes`
        * **Handles external communication**
        * **Optimizes query execution**

    * **Compute Nodes**:
        * Each with `own CPU, memory, and disk` (determined by the node type)
        * Scale up: get more powerful nodes
        * Scale out: get more nodes

    * **Node Slices**:
        * Each compute `node is logically divided into a number of slices`
        * A `cluster with n slices can process n partitions of tables simultaneously`
            * Let's consider that a `slice` is a `CPU`. That means that each `CPU` will process part of a tables partition. 

* ![amazon_redshift](./images/amazon_redshift6.png)
    * Correct!! The total number of slices in a cluster is our unit of parallelism and it is equal to the sum of all slices on the cluster.

* ![amazon_redshift](./images/amazon_redshift7.png)

* ![amazon_redshift](./images/amazon_redshift7.png)

* ![amazon_redshift](./images/amazon_redshift8.png)

* ![amazon_redshift](./images/amazon_redshift9.png)
    * Setting Billing Alarms are suggested 

* Redshift Node Types and Slices
    * Compute Optimized Nodes:
        * **Start with these for lower costs and a capacity of 5 terabytes**
    * Storage Optimized Nodes:
        * **Higher costs, not as fast, but higher capacity**

* SQL to SQL ETL

    * ![amazon_redshift](./images/amazon_redshift10.png)

    * ![amazon_redshift](./images/amazon_redshift11.png)

    * ![datawarehousing](./images/l3-datawarehousing-on-aws-2.png)

    * ![sql-to-etl](./images/sql-to-etl.png)

    * ![l3-datawarehousing-on-aws-3](./images/l3-datawarehousing-on-aws-3.png)

    * ![sql-to-etl](./images/sql-to-etl1.png)

* **Transferring Data from an S3 Staging Area to Redshift**
    * Use the `COPY` Command
        * Inserting data row by using `INSERT` will be very slow
    * If the file is large:
        * It is better to `break it up into multiple files`
        * **Ingest in Parallel**
    * Other considerations:
        * Better to ingest from the **same AWS region**
        * Better to **compress all the CSV files**
    * Can also specify the delimiter to be used

    * ![sql-to-etl](./images/sql-to-etl3.png)

    * ![sql-to-etl](./images/sql-to-etl4.png)

    * ![sql-to-etl](./images/sql-to-etl5.png)

    * ![sql-to-etl](./images/sql-to-etl6.png)

    * ![sql-to-etl](./images/sql-to-etl7.png)

        * While not as scalable as using S3 as a staging area, you can also ingest data directly from EC2 machines storage.
            * Usually you'll want to use S3 as a staging area, but for very small data, you might want to copy it directly from the EC2 machine.

* Configuring Redshift Access and Security

    * The cluster created by the Quick Launcher is a fully-functional one, but we need more functionality.

    * Security:
        * The cluster is accessible only from the virtual private cloud
        * We need to access it from our jupyter workspace

    * Access to S3:
        * The cluster needs to access an S3 bucket
    * ![sql-to-etl](./images/sql-to-etl8.png)

* `L3 Exercise 2 - IaC - Solution.ipynb`

* `L3 Exercise 3 - Parallel ETL - Solution.ipynb`

* Optimizing Table Design
    * When a table is partitioned up into many pieces and distributed across slices in different machines, this is done blindly.

    * If there is knowledge about the frequent access pattern of a table, you can choose a more performant strategy.

    * The 2 possible strategies are:

    * Distribution Style
        * `EVEN` distribution
            * Round-robin over all slices to achieve load-balancing
            * Good if a table won’t be joined
            * ![distribution](./images/distribution.png)
            * ![distribution](./images/distribution1.png)
            * ![distribution](./images/distribution2.png)
        * `ALL` distribution
            * Small tables could be replicated on all slices to speed up joins
            * Used frequently for dimension tables
            * AKA “broadcasting”
            * ![distribution](./images/distribution3.png)
            * ![distribution](./images/distribution4.png)
        * `AUTO` distribution
            * Leave decision to Redshift
            * “Small enough” tables are distributed with an `ALL` strategy
            * Large tables are distributed with `EVEN` strategy
        * `KEY` distribution
            * Rows having similar values are placed in the same slice
            * ![distribution](./images/distribution5.png)
            * ![distribution](./images/distribution6.png)
            * ![distribution](./images/distribution7.png)
            * ![distribution](./images/distribution8.png)
            * ![distribution](./images/distribution9.png)
    * Sorting key
        * Define columns as sort key
        * Rows are sorted before distribution to slices
        * Minimizes the query time
        * Useful for columns that are used frequently in sorting like the date dimension and its corresponding foreign key in the fact table
        * ![distribution](./images/distribution10.png)
        * ![distribution](./images/distribution11.png)
        * ![l3-datawarehousing-on-aws-7](./images/l3-datawarehousing-on-aws-7.png)

* `L3 Exercise 4 - Table Design - Solution.ipynb`