import { useNavigate } from "react-router-dom";
import GoogleIMG from "../assets/google.png";

const Auth = () => {
  const navigate = useNavigate();

  const handleLoginClick = async () => {
    const login = await fetch("http://localhost:8080/login", {
      method: "GET",
    });
    navigate("/home");
  };

  return (
    <>
      <div className="flex justify-around items-center h-[100vh] w-[100%] ">
        <div className="flex flex-col items-center justify-center h-[80vh] w-[40vw]">
          <h1 className="font-['Whisper'] text-[3.5rem]">Welcome to</h1>
          <h1 className="font-bold text-[4rem]">CryptoDrive</h1>
        </div>
        <div className="flex flex-col items-center justify-around  h-[20vh] w-[20vw]">
          <h1 className="font-bold text-[2rem]">Login with </h1>
          <img src={GoogleIMG} alt="google-png" />
          <button
            className="bg-[#1e84c4] px-6 py-3 rounded-md text-white font-bold"
            onClick={handleLoginClick}
          >
            Login
          </button>
        </div>
      </div>
    </>
  );
};

export default Auth;
