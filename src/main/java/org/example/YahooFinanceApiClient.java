package org.example;

import java.io.IOException;
import java.math.BigDecimal;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileWriter;
import java.io.IOException;
import org.json.JSONArray;
import org.json.JSONObject;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.ObjectMapper;


public class YahooFinanceApiClient {
    private static final String BASE_URL = "https://query1.finance.yahoo.com/v8/finance/chart/";

    public static void main(String[] args) throws IOException {
        String symbol = "AAPL";
        String interval = "1d";
        String range = "1mo";

        String url = BASE_URL + symbol + "?interval=" + interval + "&range=" + range;
        HttpGet request = new HttpGet(url);
        HttpResponse response = HttpClients.createDefault().execute(request);
        HttpEntity entity = response.getEntity();
        String responseJson = EntityUtils.toString(entity);

        JSONObject jsonObject = new JSONObject();
        jsonObject.put("value", responseJson);




        FileWriter writer = new FileWriter("output.json");
        writer.write(responseJson);
        writer.close();


    }


}


