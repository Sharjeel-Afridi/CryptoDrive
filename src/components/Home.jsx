import { useEffect, useState } from "react";
import Password from "./Password";

const Home = () => {
    const [data, setData] = useState({"name": []})
    const [showPassword, setShowPassword] = useState(false)
    const[filename, setFilename] = useState('');


    useEffect(()=>{
          fetchData()
    },[])

    const fetchData = async () => {
        try {
          const response = await fetch('http://localhost:8080/api/data'); 
          
          const jsonData = await response.json();
          console.log(jsonData)
          setData(jsonData);
          
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };

      const fileClick = (item) => {
        setFilename(item)
        setShowPassword(true)        
      }
      const handleRefresh = () => {
        console.log('refresh')
        fetchData()
      }
    
    return (
        <>
        <div className="flex justify-between items-center h-[100px] px-10">
            <h1 className="font-bold text-2xl">
                HOME
            </h1>
            <button onClick={handleRefresh}>Refresh</button>
        </div>
        <div className="flex gap-[50px] flex-wrap ml-[20px]">
            {data.name.map((item,index) => (
                <div key={index} className="flex flex-col w-[100px] cursor-pointer" onClick={() => fileClick(item)}>
                    <img src="../../static/icons8-file-100.png" className="w-[100px]"/>
                    <h2 className="w-[100px] overflow-hidden">{item}</h2>
                </div>
            ))}
        </div>
        {showPassword && <Password filename={filename}/>}
        </>
    )
};
export default Home;
