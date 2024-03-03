// import Key from "../../py/mykey.txt";
import { useEffect, useState } from "react";

const Apikey = () => {
    const [keyContent, setKeyContent] = useState('')
    useEffect(()=>{
        const fetchKeyContent = async () => {
            try {
            const response = await fetch('../../mykey.txt'); // Adjust the path as per your file location
            const text = await response.text();
            setKeyContent(text);
            } catch (error) {
            console.error('Error fetching key content:', error);
            }
        };
    
        fetchKeyContent();
        }, []);
        
    
    return (
        <div className="absolute top-0 h-[100%] w-[100%] z-10 flex justify-center items-center">
            <div className="flex justify-center items-center p-4 h-[15vh] bg-slate-400 rounded-md ">
            <h1 className=" font-bold bg-white text-black rounded-md">{keyContent}</h1>
            </div>
        </div>
    )
    
        
    }
export default Apikey;