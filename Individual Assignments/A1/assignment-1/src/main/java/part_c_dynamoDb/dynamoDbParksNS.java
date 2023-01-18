package part_c_dynamoDb;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.model.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class dynamoDbParksNS {
    // method to insert data into the table
    public static void insertIntoTable(String tableName) {
        JSONParser jsonParser = new JSONParser();
        try {
            Reader reader = Files.newBufferedReader(Paths.get("/Users/ruhityagi/Downloads/sdp_assignment1_s22/src/main/java/part_c_dynamoDb/campsites.json"));
            Object obj = jsonParser.parse(reader);
            JSONArray campSites = (JSONArray) obj;
            campSites.forEach(camp -> {
                HashMap<String, AttributeValue> item_values =
                        new HashMap<String, AttributeValue>();
                item_values.put("name", new AttributeValue((String) ((JSONObject) camp).get("name")));
                item_values.put("place", new AttributeValue((String) ((JSONObject) camp).get("place")));
                if (((JSONObject) camp).get("size") != null) {
                    item_values.put("size", new AttributeValue((String) ((JSONObject) camp).get("size")));
                }
                item_values.put("properties", new AttributeValue((ArrayList<String>) ((JSONObject) camp).get("properties")));
                final AmazonDynamoDB ddb = AmazonDynamoDBClientBuilder.defaultClient();
                try {
                    ddb.putItem(tableName, item_values);
                } catch (AmazonServiceException e) {
                    e.printStackTrace();
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    //method to update types_ofcampsites in table
    public static void updateTable(String tableName) {
        JSONParser jsonParser = new JSONParser();
        try {
            Reader reader = Files.newBufferedReader(Paths.get("/Users/ruhityagi/Downloads/sdp_assignment1_s22/src/main/java/part_c_dynamoDb/campsites.json"));
            Object obj = jsonParser.parse(reader);
            JSONArray campSites = (JSONArray) obj;
            campSites.forEach(camp -> {
                UpdateItemRequest request = new UpdateItemRequest();
                request.setTableName(tableName);
                request.setReturnConsumedCapacity(ReturnConsumedCapacity.TOTAL);
                request.setReturnValues(ReturnValue.UPDATED_OLD);
                Map<String, AttributeValue> keysMap = new HashMap<>();
                keysMap.put("name", new AttributeValue(
                        (String) ((JSONObject) camp).get("name")));
                keysMap.put("place", new AttributeValue((String) ((JSONObject) camp).get("place")));
                request.setKey(keysMap);
                Map<String, AttributeValueUpdate> map = new HashMap<>();
                map.put("types_of_Campsites", new AttributeValueUpdate(
                        new AttributeValue((ArrayList<String>) ((JSONObject) camp).get("properties")), "PUT"));
                request.setAttributeUpdates(map);
                try {
                    AmazonDynamoDB dbClient = AmazonDynamoDBClientBuilder.defaultClient();
                    dbClient.updateItem(request);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        insertIntoTable("Parks_NovaScotia");
        updateTable("Parks_NovaScotia");
    }
}