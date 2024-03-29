import { useEffect, useState } from "react";
import CopyImg from "../assets/icons8-copy-64.png";

const Apikey = ({ setKeyCopied }) => {
  const [keyContent, setKeyContent] = useState("");

  useEffect(() => {
    const fetchKeyContent = async () => {
      try {
        const response = await fetch("../../mykey.txt"); // Adjust the path as per your file location
        const text = await response.text();
        setKeyContent(text);
      } catch (error) {
        console.error("Error fetching key content:", error);
      }
    };

    fetchKeyContent();
  }, []);

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(keyContent);
      setKeyCopied(true);
    } catch (error) {
      console.error("Failed to copy:", error);
    }
  };

  return (
    <div className="absolute top-0 h-[100%] w-[100%] z-10 flex justify-center items-center backdrop-blur-[5px]">
      <div className="flex justify-center items-center gap-[10px] px-10 h-[25vh] bg-gray-800 rounded-md ">
        <h1 className="flex items-center font-medium bg-white text-black rounded-sm h-[15vh] px-4">
          {keyContent}
        </h1>
        <img
          src={CopyImg}
          className="w-[25px] cursor-pointer"
          onClick={copyToClipboard}
        />
      </div>
    </div>
  );
};
export default Apikey;
