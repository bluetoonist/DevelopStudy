# axios Usage Snippet Code
```
import React, {useState, useEffect} from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState('');

  const printData = () => {
    console.log(...data);
  }

  useEffect( () => {
    async function fetchData() {
      const result = await axios.get("http://127.0.0.1:8000/data/?format=json");  
      setData([data, result.data])
    }
    fetchData();
  },[setData])

  return (
    <>
      <button onClick={printData}>ClickMe</button>
    </>
    )
}

export default App; 
```
