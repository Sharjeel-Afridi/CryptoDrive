const InputField = () => {

    return(
        <form method="POST" encType="multipart/form-data" action="/" className="flex flex-col gap-[30px] justify-around items-center h-[40vh] w-[60vw] bg-gray-800">
            <input type="file" id="myFile" name="uploaded-file" className="rounded-md font-semibold" accept=".jpg" />
            <input type="submit" className="bg-green-600 border-0 px-4 py-2 rounded-md font-semibold" value="Submit" />
        </form>
    )
};

export default InputField;