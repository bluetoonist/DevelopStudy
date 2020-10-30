# Android URL Connection Note
```
안드로이드에서 URL Connection을 사용하기 위해서 사용 된 Method
```
```
 public String getData(String param1) {
        try {
            System.out.println(param1);
            String ConnectUrl = "http://{IP}:{PORT}"+param1;
            URL reqURL = new URL(ConnectUrl);

            HttpURLConnection urlConn = (HttpURLConnection) reqURL.openConnection();
            urlConn.setRequestMethod("GET");
            urlConn.setRequestProperty("Accept", "/");

            int resCode = urlConn.getResponseCode();
            System.out.println("resCode : " + resCode);

            if (resCode != HttpURLConnection.HTTP_OK) {
                return null;
            }

            BufferedReader reader = new BufferedReader(new InputStreamReader(urlConn.getInputStream()));
            String input;
            StringBuffer sb = new StringBuffer();

            while ((input = reader.readLine()) != null) {
                sb.append(input);
            }
            return sb.toString();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
```
```
Android에서 URL Connection을 맺기 위해 Thead가 필요함(ChangUi.md 파일을 참조)
```