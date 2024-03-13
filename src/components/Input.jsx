import { useState } from "react";
import close from "../assets/close.png";


const InputField = ({ setFormSubmitted, inputClick, setInputClick }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();

    if (!selectedFile) {
      console.error("No file selected");
      return;
    }

    const formData = new FormData();
    formData.append("image", selectedFile);

    try {
      const response = await fetch("http://localhost:8080/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to upload image");
      }
      console.log("Image uploaded successfully");
    } catch (error) {
      console.error("Error:", error);
    }
    setFormSubmitted(true);
  };

  return (
    <div
      className="fixed top-0 h-[100%] w-[100%] z-10 backdrop-blur-[5px]"
      onClick={setInputClick(!inputClick)}
    >
      <form
        method="POST"
        onSubmit={handleFormSubmit}
        encType="multipart/form-data"
        action="/"
        className="absolute top-[30%] left-[25%] flex flex-col gap-[30px] justify-around items-center h-[40vh] w-[60vw] bg-gray-800"
      >
        <input
          type="file"
          onChange={handleFileChange}
          id="myFile"
          name="uploaded-file"
          className="rounded-md font-semibold cursor-pointer"
          accept="*"
        />
        <input
          type="submit"
          className="bg-green-600 border-0 px-4 py-2 rounded-md font-semibold cursor-pointer"
          value="Submit"
        />
      </form>
      <img src={close} className="absolute top-[30%] left-[81vw] cursor-pointer" onClick={() => setInputClick(false)}/>
    </div>
  );
};

export default InputField;
