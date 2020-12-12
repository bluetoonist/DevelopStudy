# React Page Route

## INSTALL 
```
yarn add react-router-dom
```

## 페이지 분할
```
[client/Root.js]
import React from "react"
import  {BrowserRouter} from "react-router-dom" // 추가
import App from "../shared/App.js" 

export default function Root() {

    return (
        <BrowserRouter>
            <App/>
        </BrowserRouter>
    )

}

[pages/index.js]
# Home, About은 파일 생성후 적당히 내용 추가
export {default as Home} from "./Home";
export {default as About} from "./About";

[shared/App.js]
import React from "react";
import {Route} from "react-router-dom";
import {Home,About} from "../pages";

export default function App() {
    return (
        <>
            <div>
                # exact는 path에 적어진 경로랑 정확히  일치할 떄
                <Route exact path="/hello" component={Home} />     
                <Route exact path="/about" component={About} />
            </div>
        </>
    )
}
```
## Reference
```
https://velopert.com/3417
```
