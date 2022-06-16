# Sparkify

## Introduction

* This project aims to `ETL` data from a fictitious music app called **Sparkify**, this applications is similar to Spotify / Apple Music. The extracted data from this app enables us to query informations about `users`, `artists`, `songs` related to those `artists` and `listened songs`. On that note, this dataset could be utilized by data scientists to understand `users` listening `patterns`, `users` preferred `songs`, `users` preferred `artists` and much more. Potentially we could use this data to train a Machine Learning model to suggest `songs` to `users`.

## How to run the project

* You need to setup a [Amazon EMR](https://aws.amazon.com/emr/) cluster, follow the instructions [here](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-launch.html) to create one.

* After your EMR Cluster is up and running, `ssh` to the `master` node (EC2 machine).
    * Instructions can be found on the Amazon EMR Dashboard.

* Create an `Amazon S3` bucket. This bucket will host the results of our `ETL` process.

* Inside the `master` machine you can clone this repository by running: `git clone git@github.com:danielmapar/DataEngineering.git`.

* Edit the `dl.cfg` file with your credentials and bucket informations.

* Kick-off the Spark application by doing: `spark-submit --master yarn etl.py`.

## Files

* `etl.py`
    * This python script reads `log` and `song` data from S3, transforms it into **facts** and **dimensions** tables then loads them back to S3 as `parquet` files.

* `dl.cfg`
    * A configurations file to setup AWS credentials and S3 bucket paths.