# props ?

## Summary
```
# 하위 컴포넌트에 값을 전달하는 역할
# 여기서 값이란 html 문법으로 봤을 떄 태그네임 해당하는 부분을 지칭
# 컴포넌트의 기본적인 동작을 바꿀 때 쓰는 것

# defaultProps 로 기본값 설정
# 컴포넌트에 props를 지정하지 않았을 떄 기본적으로 사용할 값을 설정 가능
# Example>>
  Hello.defaultProps = { name : "이름없음" }

```


# Example
```
# App Component
function App() {
  return ( <Hello name="react" color='red'/>)
}

# Hello Component
function Hello{name,}{
    return <div name={{name}}></div>
}
```