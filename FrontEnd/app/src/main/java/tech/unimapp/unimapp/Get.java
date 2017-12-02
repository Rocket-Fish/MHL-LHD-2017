package tech.unimapp.unimapp;

import android.os.AsyncTask;
import android.util.Log;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import javax.net.ssl.HttpsURLConnection;

public class Get extends AsyncTask<String[], Integer, String>{
    private String url;
    private final String USER_AGENT = "Mozilla/5.0";

    public Get(String url) {
        this.url = url;
    }

    private String get(String[] args) throws IOException {
        URL obj = new URL(url);
        HttpsURLConnection con = (HttpsURLConnection) obj.openConnection();

        //add reuqest header

        con.setRequestProperty("User-Agent", USER_AGENT);
        con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");

        String urlParameters = "";
        for(String arg:args){
            urlParameters += "&"+arg;
        }
        urlParameters = urlParameters.substring(1);

        // Send post request
        con.setRequestMethod("GET");
        con.setDoOutput(false);
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.writeBytes(urlParameters);
        wr.flush();
        wr.close();

        int responseCode = con.getResponseCode();
        System.out.println("\nSending 'GET' request to URL : " + url);
        System.out.println("GET parameters : " + urlParameters);
        System.out.println("Response Code : " + responseCode);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();
        return String.valueOf(response);
    }

    @Override
    protected String doInBackground(String[]... args) {
        try {
            Log.wtf("response", get(args[0]));
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
