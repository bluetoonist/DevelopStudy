# Change UI Note
```
한 쪽 View가 다른 한 쪽의 View의 상태를 변경하는 방법
```

## What is Probs?
```
안드로이드에서는 Main Thread와 Sub Thread가 동시 접근하여 동기화 이슈를 발생시키는 것을
방지시키기 위해 UI 자원 사용은 UI Thread에서만 가능하도록 만듬
```

## How to USE?
```
: Method -> runOnUiThread 개념
```
```
다음과 같이 어떤 View에 관해 동작을 하는 메소드가 있다고 가정할 때
```
```
@Override
 public void onClick(View v) {
     ..Someting Pseudocode
   }
```
```
runOnUiThread는 다음과 같이 사용 가능
```
```
@Override
 public void onClick(View v) {
   ..Someting Pseudocode
    
    
   new Thread(new Runnable() {
  
	@Override
    public void run() {
        runOnUiThread(new Runnable() {
            public void run() {
				
                    // 이 안에서 다른 View의 속성을 변경 가능
                  
                  }
			 });    // runOnUiThread End
		}           // run() Method End
	}).start();     // new Thread End
}
```