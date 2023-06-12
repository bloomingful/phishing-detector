import React from 'react';
import { FaGithub } from 'react-icons/fa';

export default function Footer() {
    const favoriteIcon = (
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
          />
        </svg>
      )

  return (
    <footer className='bg-base-200 text-base-content '>
      <div className='container '>
        <div className='flex flex-col sm:flex-row items-center border-t border-base-300 py-4 gap-2'>
          <div className="flex-grow text-center sm:text-start">
            <p>© 2023.</p>
          </div>
          <div className="grid grid-flow-col gap-4">
            <a href="https://github.com/bluemberg/phishing-detector-backend" className="btn btn-sm btn-github">
                <FaGithub className="inline-block mr-2" />
                Github
            </a>
          </div>
        </div>
      </div>
    </footer>
  )
}