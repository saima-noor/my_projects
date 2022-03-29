import boto3
import json

import botocore
# import operator
list_buckets = []

total_size = 0
rank = 0
try:
    print("Here are all the S3 Buckets")
    

    s3_client = boto3.client('s3')

    response1 = s3_client.list_buckets() 
    # print(response1)
    print("count of buckets" + str(len(response1['Buckets'])))                                                            
    for bucket in response1['Buckets']:
        object_count = 0
        print("..................................................................................................")

        print(bucket['Name'])
        
        total_size_objects = 0
        storage_class_list = []

        response2 = s3_client.list_objects(Bucket= bucket['Name'])
        

        # print(response2['IsTruncated'])
        
        # print(response2['KeyCount'])

        try:
            print("count of objects: " + str(len(response2['Contents'])))
            object_count = len(response2['Contents'])
            # print(object_count)
            

   
            for obj in response2['Contents']:
             
                # print(obj['Owner'])
                total_size_objects = total_size_objects + obj['Size']

                # print(obj['StorageClass'])
                storage_class = obj['StorageClass']

                if storage_class == 'STANDARD':
                    storage_class_list.append(1)
                if storage_class == 'REDUCED_REDUNDANCY':
                    storage_class_list.append(2)
                if storage_class == 'GLACIER':
                    storage_class_list.append(3)
                if storage_class == 'STANDARD_IA':
                    storage_class_list.append(4)
                if storage_class == 'ONEZONE_IA':
                    storage_class_list.append(5)
                if storage_class == 'INTELLIGENT_TIERING':
                    storage_class_list.append(6)
                if storage_class == 'DEEP_ARCHIVE':
                    storage_class_list.append(7)
                if storage_class == 'OUTPOSTS':
                    storage_class_list.append(8)
                if storage_class == 'GLACIER_IR':
                    storage_class_list.append(9)
                    

                # 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'|'OUTPOSTS'|'GLACIER_IR',

                object_key = obj['Key']
                # print(object_key)

                # response3 = s3_client.get_object(Bucket= bucket['Name'], Key =object_key )
                # print("::::::::::::::::::::::::::::::::")
                # print(response3)


            # response4 = s3_client.get_bucket_tagging(Bucket= bucket['Name'])
            # # print("::::::::::::::::::::::::::::::::")
            # # print(len(response4['TagSet']))
            # tag_count = len(response4['TagSet'])

            # print(storage_class_list)

            sum_storage_class = 0

            for sc in range(0, len(storage_class_list)):
                sum_storage_class = sum_storage_class + storage_class_list[sc]

            print(sum_storage_class)

 
            total_size =total_size + total_size_objects
            total_size_in_gb = total_size * (9.31 * (10E-10)) # converting size in byte to gb
            size_per_object = total_size_in_gb/object_count
            rank = object_count + size_per_object + (sum_storage_class * (sum_storage_class/object_count))
            rank = round(rank, 5)

            list_buckets.append((bucket['Name'],object_count, total_size_objects, rank) )
            
        except Exception as e:
            print ( "Exception occured ")

            print(e)
            object_count = 0
            total_size_objects = 0
            # tag_count = 0 
            total_size_in_gb = total_size * (9.31 * (10E-10))
            size_per_object = 0
            sum_storage_class = 0
            rank = object_count + size_per_object + sum_storage_class
            rank = round(rank, 5)
            list_buckets.append((bucket['Name'],object_count, total_size_objects, rank) )

            continue

            


            

        # # if 'NextToken' in  response1.keys():
        # #     next_token = response1['NextToken']
            
        # # else:
        # #     break
        
    
    # print("here")
    # def myFunc(e):
    #     return e[3]
    # list_buckets.sort(key=myFunc)
    # print(list_buckets)


except Exception as e:
    print ( "Exception occured ")
    print(e)
    # continue
print(list_buckets)
print(len(list_buckets))
print(total_size)

print("here")
def myFunc(e):
    return e[3]
list_buckets.sort(key=myFunc)
print(list_buckets)

            