# Automated Image Resizing and Transfer System Using AWS Services

## Project Description:
This project focuses on building an automated system for image processing and management within the AWS ecosystem. The goal is to streamline the handling of images by automatically resizing them and transferring them to a designated storage location while keeping stakeholders informed through notifications. Key AWS services, such as Lambda, S3, and SNS, are used to orchestrate this workflow.

## Key Features:
1. Image processing automation: Automatically resize and optimize images upon upload.
2. Secure storage: Store processed images in a secure and reliable S3 bucket.
3. Real-time notifications: Receive immediate updates about image processing via SNS.
4. Scalable architecture: Design for scalability to handle image processing demands.
5. Cost-efficient solution: Leverage AWS serverless technologies to minimize operational costs.

## Overview :

![a1](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/d806e90a-365e-4f59-a6ac-2606c74b79e3)



## Steps :
### Step 1 :
### Creating Source and Designation s3 Buckets :

1. Navigate to the S3 Console.
2. Follow the Outlined Steps below.


![i1](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/fcf47c3c-3b40-4952-a0b5-5f53fe3d6444)


![i2](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/038c999c-e926-4613-9a23-2d5593c8fd95)


![i3](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/5cc0025f-29ac-40bd-8ee3-619271aaba58)

3. Create the destination bucket using the same steps and name it with a unique name.

![i4](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/2b98cf18-6e99-4154-81d9-c3ca5e864938)

4. As you can see above , I created two buckets one is Source bucket and another one is Destination bucket.

### Step 2 :
### Creating the SNS Notification :

1. Navigate to the SNS console.
2. Follow the Outlined Steps below.


![i5](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/50ae0833-cc4a-4cdd-9d03-2554cf981104)


![i6](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/bd101082-a68f-4f12-8131-412766a0835a)



![i7](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/12321adb-93ea-4715-9416-9ad0c3dd7ca3)


![i8](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/50d699f3-6501-418e-8303-9f4f113325ef)


![i9](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/96b45ba6-822d-4961-b5d1-e70fab104ac6)


![i10](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/9da24906-1523-4158-8c9c-0a3c23902dbc)
3. Scroll down and Click "Create subscription" <br>
4. After this , you will receive some mail for Subscription Confirmation and you have to confirm that.<br>
5. You can use any other protocols also like SQS, HTTP, SMS etc .,<br>


![i11](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/39c7c7d2-e9c0-41e7-b3e9-54802bf871d5)


![i12](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/3bb970d6-b6de-4d45-a7d7-8738987d32b7)


![i3](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/00b10697-1827-4304-b130-a4856e780570)



### Step 3 :
### Creating the Lambda :

1. Navigate to the Lambda Console.
2. Follow the Outlined steps below.

![i14](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/c90eaf3b-2a38-46dc-80f2-a097febf0e95)



![i15](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/1eeca065-8dbd-41d4-953d-59cec42c87bc)

3. Now replace the default code with the image-resizing-s3.py and deploy the changes , Don't test the code now we have to do some more actions before testing.
4. After that , We have to give some permission for our Lambda Function to do our process (resizing) , For that navigate to the IAM Console and follow the below steps.


![i16](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/c49c69dc-7e60-4fd1-835c-4b1581e3122e)

![i17](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/c983d5e0-e443-42c1-ab03-5bdea50434df)


![i18](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/2eb8707d-bb9c-40e6-a4cb-3fb9688fe4b2)


![i19](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/e7ab7943-e876-402c-b074-ad3b4873484e)


![i20](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/70bc666a-cda0-4374-b01f-1c91e5082770)


![i21](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/d0f40dad-c535-45c0-a19c-402aba93d555)


![i22](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/11be7629-4cf2-4318-adbf-d01873a4655c)

5. Now navigate to the Lambda Console and follow the steps below.


![i23](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/17797c6b-109c-455d-ae15-d412b83182fe)


![i24](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/fd489e94-5129-4bee-a682-ad24a2685233)


![i25](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/69779aa0-34d3-4502-9f9e-4ac15331db99)


6. Now we have to trigger the function.


![i26](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/166aadb1-4d3a-40d8-a70e-681ea507e1d1)


![i27](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/b8dcb311-1914-47bc-96a7-5df62a283954)


![i28](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/76164aba-a478-4590-a7e4-966d3f30078f)


7. Now we have to go to code section , and scroll down to  layers.<br>
8. We have to add layer .<br>
9. May be you can think , why ?<br>
10. It's because for resize the image we upload in our source S3 bucket , We need a python library called pillow in our code to resize the image . We can manually add Pillow library also, But it's very time consuming and you have to do lot more , Instead of manually adding pillow library we are going to use layers for Some easy action.<br>
11. Follow the outlined Steps below.


![i51](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/a4500c08-8a18-4a26-844a-5ad7712ba310)


![i52](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/d20cb878-d8a9-4757-8f42-7596f5448f0f)
12.You can copy the arn from below.

```
arn:aws:lambda:ap-south-1:770693421928:layer:Klayers-p39-pillow:1
```

13. After done all the actions above , now we can test our code.

![i49](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/fa884cf6-e858-44c4-ac03-fa4b4c0de763)


![i50](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/9f13561b-3839-495e-bf69-9ac34605f3c9)

14. It will show some results like below , It runs successfully but return some error because we still not upload the images in S3 yet.


![i50 1](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/d4d73c43-32aa-4ada-bed0-3aa30dd053e4)


### Step 4 :
### Results :

1. Navigate to the S3 Console.
2. Upload Some images in  Source Bucket.


![i29](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/43f39f6f-dc95-4df6-a7b2-7b4f7d631642)



![i30](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/4deb12e5-3597-4ebc-bf28-3b235b058969)


![i31](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/bc0585bd-0e6d-47e3-891b-e5dd3be0da2b)


![i32](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/c9eb1a36-198e-4b90-be94-0c95c9d877c6)


![i33](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/4e827762-b1f7-49d0-90ce-370ddaac014f)


![i34](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/b5933c6c-91d8-4eac-8940-389dbd64d101)


![i35](https://github.com/itz-mathesh/image-resizing-using-s3-lambda-and-sns/assets/144098846/d7bdb74a-9d8f-4d02-b9ad-c1c5e463e75a)

### It Successfully resized the Image and sends me the Notification.


