const Password = () => {
  const handleFormSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch("http://localhost:8080/checkpass", {
        method: "POST",
        body: event.target.value,
      });

      if (!response.ok) {
        throw new Error("Try Again");
      }
      console.log("Checked successfully");
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="absolute top-0 h-[100%] w-[100%] z-10 flex justify-center items-center backdrop-blur-[5px]">
      <form
        className="flex justify-center items-center gap-[10px] p-4 h-[15vh] bg-slate-400 rounded-md "
        onSubmit={handleFormSubmit}
      >
        <input
          className=" font-bold bg-white text-black rounded-md"
          placeholder="Enter your Secret Key"
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Password;
