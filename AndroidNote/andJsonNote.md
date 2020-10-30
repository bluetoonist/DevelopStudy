# JSON Array Note
```
다음과 같은 자료형 이 있을 때
[{"id1":"1"},{"id2":"2"},...]
Android에서 JSON으로 사용가능하게 만들 수 있는 방법

nodejs에서 다음과 같은 코드를 Android로 전송한 경우에 성공함
client.query("select time,device_id from readings LIMIT 20" ,(err, queryRes) => {
        var obj = JSON.stringify(queryRes.rows);    
        res.send(obj);
    });
```

## Android
```
final StringBuilder retstr =  new StringBuilder(""); <-- 

try {
    JSONArray jobject = new JSONArray(param1); 

    for (int i=0; i<jobject.length(); i++) {
    JSONObject jsonobject = jobject.getJSONObject(i);  <-- getJSONObject로 한번 더 변환
    String time = jsonobject.getString("time"); <-- Key 값으로 얻어옴(Key=time)
    retstr.append(time); 
    retstr.append("\n"); <-- 안드로이드 단말에서 \n 처리를 위해 추가
    }
System.out.println(retstr);
```