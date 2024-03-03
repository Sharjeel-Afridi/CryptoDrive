import { useEffect, useState } from "react";

const Home = () => {
  const [data, setData] = useState({ name: [] });
  useEffect(() => {
    fetchData();
  }, []);
  const fetchData = async () => {
    try {
      const response = await fetch("http://localhost:8080/api/data");

      const jsonData = await response.json();
      console.log(jsonData);
      setData(jsonData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  const sendFileName = async (filename) => {
    try {
      const response = await fetch("http://localhost:8080/send", {
        method: "POST",
        body: filename,
      });
      if (!response.ok) {
        throw new Error("Failed to send response");
      }
      console.log("responce sent successfully");
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <>
      <h1 className="font-bold text-2xl mt-[80px] ml-[50px]">HOME</h1>
      <div className="flex gap-[50px]">
        {data.name.map((item, index) => (
          <div
            key={index}
            className="flex flex-col w-[100px] cursor-pointer"
            onClick={() => sendFileName(item)}
          >
            <img src="../../static/icons8-file-100.png" className="w-[100px]" />
            <h2 className="overflow-hidden">{item}</h2>
          </div>
        ))}
      </div>
    </>
  );
};
export default Home;
