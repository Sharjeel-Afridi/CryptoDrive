import { useState } from "react";


const Password = ({filename}) => {
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
            <form className="flex justify-center items-center gap-[10px] p-4 h-[15vh] bg-slate-400 rounded-md " onSubmit={handleFormSubmit}>
                <input 
                    className=" font-bold bg-white text-black rounded-md" 
                    placeholder="Enter your Secret Key"
                    value={inputValue}
                    onChange={handleInputChange}/>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
};

export default Password;
