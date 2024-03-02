import { useState } from 'react';
import Plus from "./assets/icons8-plus-100.png"

const App = () => {
    
    return (
      <div className="flex">
        <nav className="flex flex-col gap-[20px] w-[25%] h-[100vh] border-r">
            <h1 className="flex justify-center items-center h-[20vh] font-bold text-3xl">CryptoDrive</h1>
            <div className="flex flex-col justify-center h-[70vh] font-bold  gap-[40px] ">
                <button className="nav-btn mx-6 p-2 " >
                    HOME
                </button>
                <button className="nav-btn mx-6 p-2 " >
                    My Drive
                </button>
                <button className="nav-btn mx-6 p-2" >
                    Recent
                </button>
            </div>
        </nav>
        <div className="relative h-[100vh] w-[75%] " id="content">
            <img src={Plus} id="upload" className="absolute h-20 bottom-20 right-20 rounded-full cursor-pointer" />
        </div>
            
      </div>
    );
};

export default App;
