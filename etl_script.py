import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame

# Initialize Glue context
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'SOURCE_S3_PATH', 'TARGET_S3_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define the source and target S3 paths
source_s3_path = args['SOURCE_S3_PATH']
target_s3_path = args['TARGET_S3_PATH']

# Extract: Read the data from the source S3 path
source_df = spark.read.option("header", "true").csv(source_s3_path)
source_dyf = DynamicFrame.fromDF(source_df, glueContext, "source_dyf")

# Transform: Convert names to uppercase
def transform_data(rec):
    rec["name"] = rec["name"].upper()
    return rec

transformed_dyf = Map.apply(frame=source_dyf, f=transform_data)

# Load: Write the transformed data to the target S3 path
transformed_df = transformed_dyf.toDF()
transformed_df.write.mode("overwrite").option("header", "true").csv(target_s3_path)
#addding test
# Commit job
job = glueContext.create_dynamic_frame.from_options(connection_type="s3", connection_options={"paths": [target_s3_path]})
job.commit()
