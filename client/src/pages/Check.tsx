import React, { useState } from "react";

const CheckPhishPage = () => {
  const [inputText, setInputText] = useState("");
  const [showResult, setShowResult] = useState(false);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const handleCheckClick = async () => {
    try {
        const response = await fetch('/reverse', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: inputText }),
        });
  
        if (response.ok) {
          const data = await response.json();
          setShowResult(data.result);
        }
      } catch (error) {
        console.error('Error:', error);
      }
  };

  return (
    <section>
      <div className="container">
        <div className="h-96 md:h-[568px] flex flex-col items-center justify-center">
            <h1 className="text-4xl font-bold mb-8">Real-Time URL Checker</h1>
            <div className="flex items-center mb-8">
                <input
                type="text"
                placeholder="Enter URL or IP address"
                className="w-96 h-12 px-4 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                value={inputText}
                onChange={handleInputChange}
                />
                <button
                className="h-12 px-6 bg-blue-500 text-white font-bold rounded-r-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 "
                onClick={handleCheckClick}
                >
                Check
                </button>
            </div>
            {showResult && (
                <div className="md:h-[200px]">
                  <div className="border border-2 border-gray-300 rounded-md p-4 mb-40">
                      <p className="text-xl">{showResult}</p>
                  </div>
                </div>
            )}
        </div>
      </div>
    </section>
  );
};

export default CheckPhishPage;