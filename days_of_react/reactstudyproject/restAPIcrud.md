# axios crud usage

## CREATE
```
 const genData = () => {

    const result = axios.post("http://127.0.0.1:8000/data/?format=json",{
      headers : {
        'Content-Type' : 'application/json',
      },
      label : 'ThisIsTest',
    });
    console.log(result.data);  
  }

```

## READ
```
useEffect( () => {
    async function fetchData() {
      const result = await axios.get("http://127.0.0.1:8000/data/?format=json");
      console.log(result.data);
      setData((state) => result.data );
    }
    fetchData();
  },[setData])

```

## UPDATE
```
```

## DELEATE
```
  const DelData = () => {
    const deldata = axios.delete("http://127.0.0.1:8000/data/11/")
    console.log(deldata)
  }
```
