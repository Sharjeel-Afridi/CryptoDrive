import { useState } from 'react';
import Plus from "./assets/icons8-plus-100.png"
import Home from "./components/Home";
import MyDrive from "./components/MyDrive";
import Recent from "./components/Recent";
import Input from './components/Input';


const componentMap = {
    "HOME": <Home />,
    "My Drive": <MyDrive />,
    "Recent": <Recent />
  };

const App = () => {
    const [buttonText, setButtonText] = useState('HOME');
    const [inputClick, setInputClick] = useState(false);

    const handleNavClick = (event) => {
        setButtonText(event.target.textContent.trim());
        
    }
    const handleUpload = () => {
        setInputClick(!inputClick)
    }

    return (
        <>
      <div className="flex">
        <nav className="flex flex-col gap-[20px] w-[25%] h-[100vh] border-r">
            <h1 className="flex justify-center items-center h-[20vh] font-bold text-3xl">CryptoDrive</h1>
            <div className="flex flex-col justify-center h-[70vh] font-bold  gap-[40px] ">
                <button className={`nav-btn mx-6 p-2 ${buttonText === 'HOME' ? 'text-black border-white rounded-full bg-blue-100' : ''}`} onClick={handleNavClick}>
                    HOME
                </button>
                <button className={`nav-btn mx-6 p-2 ${buttonText === 'My Drive' ? 'text-black border-white rounded-full bg-blue-100' : ''}`} onClick={handleNavClick}>
                    My Drive
                </button>
                <button className={`nav-btn mx-6 p-2 ${buttonText === 'Recent' ? 'text-black border-white rounded-full bg-blue-100' : ''}`} onClick={handleNavClick}>
                    Recent
                </button>
            </div>
        </nav>
        <div className="relative h-[100vh] w-[75%] " id="content">
            {componentMap[buttonText]}
            {/* {inputClick && <Input />} */}
            <img 
                src={Plus} 
                id="upload" 
                className="absolute h-20 bottom-20 right-20 rounded-full cursor-pointer" 
                onClick={handleUpload}
            />
        </div>
        
      </div>
      {inputClick && <Input />}
      </>
    );
};

export default App;
