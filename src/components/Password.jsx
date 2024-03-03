import { useState } from "react";


const Password = ({filename, setPasswordChecked}) => {
    const[inputValue, setInputValue] = useState('');

    const handleInputChange = (event) => {
        setInputValue(event.target.value);
        
    };

    const handleFormSubmit = async (event) => {
        console.log(inputValue)
        event.preventDefault();
        const data = {
            "filename": filename,
            "input": inputValue
        }
        try {
            const response = await fetch('http://localhost:8080/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            setPasswordChecked(true)
            if (!response.ok) {
                throw new Error("Try Again");
            }
            console.log("Checked successfully");
        } catch (error) {
            console.error("Error:", error);
        }
    
  };


    return(
        <div className="absolute top-0 h-[100%] w-[100%] z-10 flex justify-center items-center backdrop-blur-[5px]">
            <form className="flex flex-col justify-center items-center gap-[10px] px-10 h-[30vh] bg-slate-400 rounded-md " onSubmit={handleFormSubmit}>
                <h1 className="font-bold text-2xl text-black">Secret Key</h1>
                <div className="flex gap-[10px]">
                    <input 
                        className=" flex items-center font-medium bg-white text-black rounded-sm h-[15vh] w-[35vw] px-4" 
                        placeholder="Enter your Secret Key"
                        value={inputValue}
                        onChange={handleInputChange}/>
                    <button type="submit" className="bg-green-700 p-4 rounded-sm font-semibold">Submit</button>
                </div>
            </form>
        </div>
    )
};

export default Password;
