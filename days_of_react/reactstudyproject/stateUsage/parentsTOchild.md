# 자식 컴포넌트에서 부모 컴포넌트로 state 값 넘기기

## App.js(Parents)
```
function App() {
    const [param, setParam] = useState([]);

    return(
        <>
        <Component setParam={setParam}/>
        </>
}
```

## Component
```

const Component = (props) => {
    const [data,setData] = useState();
    ...
    props.setParam(data);
    ...
}
```
## Summary
```
자식 컴포넌트에서 부모 컴포는에게 값을 전달할 때는 아래와 같은 순서에 따름
1. 부모 컴포넌트에서 불러온 자식 컴포넌트의 props를 설정
2. 자식 컴포넌트의 export 함수의 인자로 "props"를 줌
3. 자식 컴포넌트에서 "props" 키워드로 넘겨받은 부모 컴포넌트의 state에 접근 가능
```