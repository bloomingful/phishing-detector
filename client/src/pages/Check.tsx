import React, { useState } from "react";
import Modal from 'react-modal';

const CheckPhishPage = () => {
  const [inputText, setInputText] = useState("");
  const [showResult, setShowResult] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  
  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const handleCheckClick = async () => {
    try {
        setIsLoading(true);
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
          setIsLoading(false);
          setIsOpen(true);
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
                placeholder="Enter URL (https://... or http://...)"
                className="w-96 h-16 px-4 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                value={inputText}
                onChange={handleInputChange}
                />
                <button
                className="h-16 px-6 bg-blue-500 text-white font-bold rounded-r-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 "
                onClick={handleCheckClick}
                >
                {isLoading ? (
                  <svg
                    className="w-6 h-6 mx-auto animate-spin"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      className="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      strokeWidth="4"
                    ></circle>
                    <path
                      className="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm12 0a8 8 0 100-16 8 8 0 000 16z"
                    ></path>
                  </svg>
                ) : (
                  "Check"
                )}
                </button>
            </div>
            {isOpen ? (
                <>
                <div
                  className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none"
                >
                  <div className="relative w-auto my-6 mx-auto max-w-3xl">
                    {/*content*/}
                    <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-base-100 outline-none focus:outline-none">

                      {/*header*/}
                      <div className="flex items-start justify-between p-5 border-b border-dashed border-gray-600 rounded-t">
                        <h3 className="text-3xl">
                          Result
                        </h3>
                      </div>

                      {/*body*/}
                      <div className="relative p-6 flex-auto">
                        <p className="my-4 text-lg leading-relaxed">
                          {showResult}
                        </p>
                      </div>

                      {/*footer*/}
                      <div className="flex items-center justify-end p-6 border-t border-dashed border-gray-600 rounded-b">
                        <button
                          className="bg-error text-white font-bold rounded-r-md uppercase text-sm px-6 py-3 rounded mr-1 mb-1 hover:bg-error focus:outline-none focus:ring-2 focus:ring-red-500 ease-linear transition-all duration-150"
                          type="button"
                          onClick={() => setIsOpen(false)}
                        >
                          Close
                        </button>
                      </div>

                    </div>
                  </div>
                </div>
                <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
              </>
            ) : null}
        </div>
      </div>
    </section>
  );
};

export default CheckPhishPage;