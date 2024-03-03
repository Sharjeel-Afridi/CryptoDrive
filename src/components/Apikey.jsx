import Key from "../../py/mykey.txt";
import { useEffect, useState } from "react";

const Apikey = () => {
    const [keyContent, setKeyContent] = useState('')
    useEffect(()=>{
        const fetchKeyContent = async () => {
            try {
            const response = await fetch('../../py/mykey.txt'); // Adjust the path as per your file location
            const text = await response.text();
            setKeyContent(text);
            } catch (error) {
            console.error('Error fetching key content:', error);
            }
        };
    
        fetchKeyContent();
        }, []);
  
    return (
        <div className="absolute top-0 h-[100%] w-[100%] z-10 backdrop-blur-[8px]">
            <h1>{keyContent}</h1>
        </div>
    )
    
        
    }
export default Apikey;