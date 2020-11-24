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
<hr>
```
위와 같이
```