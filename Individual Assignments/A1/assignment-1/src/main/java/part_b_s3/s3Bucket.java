package part_b_s3;
/**
 * Author: Ruhi Rajnish Tyagi
 * Banner Id: B00872269
 */

import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicSessionCredentials;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.AmazonS3Exception;
import com.amazonaws.services.s3.model.Bucket;

import java.io.File;
import java.nio.file.Paths;

public class s3Bucket {

    //method to connect to the AWS account
    public AmazonS3 getConnection(){

        //provide credentials to create connection
        BasicSessionCredentials sessionCredentials = new BasicSessionCredentials(
                "ASIARLJZH5IEGDGIMJFK",
                "vKsjChT5EZsbYOgFJtMoYbed7Ibdi+dGLTf18j6R",
            "FwoGZXIvYXdzEPL//////////wEaDB9Mv/we577twI7uCSLAAZWqW8x1lzAOPm" +
                    "FycWiL0RuydxJQjHmfBt+EOuFePmsAnPlYI5LK/kFp2LI+D7ji271FahA8AFyJ5gjAe" +
                    "CC015ns3nmXWhYwLgP03hFCoAMdeQpMICXjnl4YPaXQp7nt+qTttSYlKQoP6ewTtxQ9BOWj" +
                    "Ze8k9IErbos4S3ibCS8iP4fwtgSemg8c1ePnHnYSq5ejTMikWXt2KFLaGdeYcKFWZKiKk1W1A" +
                    "D88ZwNGUA6I5bLax06KagmNAPs8FIgZWijx48WUBjIt51Gz7u0FEGANCgM2YeeXyFO+njavK5+" +
                    "R7P8oqcsMNCl50KzB7ofWAR1DflPB"
                 );

        //Connect to AmazonS3 service and store in an object
        AmazonS3 s3Obj = AmazonS3ClientBuilder.standard().withCredentials
                (new AWSStaticCredentialsProvider(sessionCredentials))
                .withRegion(Regions.US_EAST_1)
                .build();

        return s3Obj;
    }

    // The public method to create a new S3 bucket
    public void createBucket (AmazonS3 s30bj, String bucketname) {
        Bucket b = null;
        //Specify bucketname as per rules
        //check if bucket exists otherwise create new.
        if (s30bj.doesBucketExistV2(bucketname)) {
            System.out.format("Bucket %s already exists.", bucketname);
        }
        else {
            try{
                s30bj.createBucket (bucketname);
                System.out.format ("A new bucket %s is created.",bucketname);
            }
            catch (AmazonS3Exception e) {
                e.printStackTrace();
                System.err.println(e.getMessage());
            }
        }
    }

    //method to upload txt file to S3bucket
    public void fileUploadToAmazonS3Bucket(AmazonS3 s3Obj,
                                           String bucketname){
        try {
            //File path to txt file
            String filepath ="./src/main/java/part_b_s3/ruhi.txt";
            //Create new file with passed filename
            File file = new File(filepath);
            //extract filename and store it in a variable
            String keyName = Paths.get(filepath).getFileName().toString();
            //Upload file to S3 Bucket
            s3Obj.putObject(bucketname,keyName,file);

            System.out.format("The file %s uploaded to AmazonS3 bucket %s successfully!",keyName,bucketname);
        }
        catch (AmazonServiceException e){
            e.printStackTrace();
            System.err.println(e.getMessage());
        }

    }

    public static void main(String[] args){
        // Creating a new s3bucket object
        s3Bucket s3object = new s3Bucket();
        String bucketname = "ruhi-tyagi-bucket";
        //Calling the getConnection method and storing connection object in s3object
        AmazonS3 s3Obj = s3object.getConnection();
        //Calling createBucket Method
        s3object.createBucket(s3Obj, bucketname);
        //Uploading the ruhi.txt file to ruhi-tyagi-bucket
        s3object.fileUploadToAmazonS3Bucket(s3Obj, bucketname);
    }
}

