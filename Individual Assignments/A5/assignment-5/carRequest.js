const AWS = require('aws-sdk');

AWS.config.update({ region: 'us-east-1' });

const sqsVersion = new AWS.SQS({ apiVersion: '2012-11-05' });
const queueURL = "https://sqs.us-east-1.amazonaws.com/092998724104/HalifaxCarsSQS";
exports.handler = async (event) => {
    console.log("EVENT");
    console.log(event);
    try {
        const params = {
            MessageBody: JSON.stringify(event),
            QueueUrl: queueURL
        };
        let sqsResponse = await sqsVersion.sendMessage(params).promise();
        console.log("Message sent to SQS");
        console.log(sqsResponse);
    }
    catch (e) {
        console.log(e);
    }
    const response = {
        statusCode: 200,
        body: 'Success!',
    };
    return response;
};