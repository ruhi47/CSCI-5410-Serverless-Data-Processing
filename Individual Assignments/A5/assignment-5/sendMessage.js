const AWS = require('aws-sdk');

AWS.config.update({ region: 'us-east-1' });

const sqsVersion = new AWS.SQS({ apiVersion: '2012-11-05' });
const queueURL = "https://sqs.us-east-1.amazonaws.com/092998724104/HalifaxCarsSQS";
const snsARN = "arn:aws:sns:us-east-1:092998724104:HalifaxCars";

exports.handler = async (event) => {
    console.log('Lambda function carRequest in execution...');
    console.log(event);

    const params = {
        QueueUrl: queueURL
    };

    try {
        const receivedMsg = await sqsVersion.receiveMessage(params).promise();
        console.log("Data from SQS");
        console.log(receivedMsg);

        for (const message of receivedMsg.Messages) {

            sendEmail(message.Body);
            const deleteParams = {
                QueueUrl: queueURL,
                ReceiptHandle: message.ReceiptHandle,
            }
            const deleteMsg = await sqsVersion.deleteMessage(deleteParams).promise();
            console.log("Message deleted")
            console.log({ deleteMsg })
        }
    }
    catch (e) {
        console.log(e);
    }

    const response = {
        statusCode: 200,
        body: JSON.stringify("SUCCESS"),
    };
    return response;
};

let sendEmail = (message) => {
    console.log("Sending Email...");
    let body = formatEmailBody(message);
    console.log(body);
    var params = {
        Message: body,
        TopicArn: snsARN
    };

    var snsVersion = new AWS.SNS({ apiVersion: '2010-03-31' }).publish(params).promise();
    snsVersion.then(
        function(data) {
            console.log(`Message sent to the topic ${params.TopicArn}`);
            console.log("MessageID is " + data.MessageId);
        }).catch(
        function(err) {
            console.error(err, err.stack);
        });
}

let formatEmailBody = (bodyStr) => {
    let body = JSON.parse(bodyStr);
    let title = "Hi, " + body.name ;
    let carType = " we see you have booked a " + body.brand + " " + body.model+". ";
    let dateDelivery = "From Date " + body.bookingFromDate + " To Date " + body.bookingToDate + ". ";
    let addressDelivery = "We will be delivering the car to the registered address: " + body.address + ". ";
    let endingMsg = "Thank you for choosing Halifax Cars. Have a good one!"

    return title + carType + dateDelivery + addressDelivery + endingMsg;
}