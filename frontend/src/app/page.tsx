"use client";
import React, { useState, useEffect } from 'react';

export default function ResiScrapeDashboard() {
  const [proxy, setProxy] = useState<any>(null);
  
  const fetchNextProxy = () => {
    fetch('http://localhost:8008/api/proxy/next')
      .then(res => res.json())
      .then(data => setProxy(data))
      .catch(() => {});
  };

  useEffect(() => {
    fetchNextProxy();
  }, []);

  return (
    <div className="min-h-screen bg-[#09090b] text-[#a1a1aa] p-8 font-mono">
      <div className="max-w-4xl mx-auto border border-[#27272a] rounded-lg p-6 bg-[#18181b] shadow-2xl">
        <h1 className="text-2xl font-bold mb-6 text-[#fafafa]">ResiScrape Master Node</h1>
        
        <div className="mb-8">
          <h2 className="text-xl font-semibold mb-4 text-[#22c55e]">Active Assigned Proxy</h2>
          <div className="bg-[#09090b] border border-[#27272a] rounded-md p-6 flex flex-col gap-2">
            {proxy ? (
              <>
                <p><span className="text-[#fafafa]">IP:</span> {proxy.ip}</p>
                <p><span className="text-[#fafafa]">Port:</span> {proxy.port}</p>
                <p><span className="text-[#fafafa]">Status:</span> <span className="text-[#22c55e]">{proxy.status}</span></p>
                <p><span className="text-[#fafafa]">Failures:</span> <span className="text-[#f97316]">{proxy.failure_count}</span></p>
              </>
            ) : <p>Loading proxy node...</p>}
          </div>
        </div>

        <div className="flex gap-4">
          <button 
            className="bg-[#22c55e] hover:bg-[#16a34a] text-[#09090b] font-bold py-2 px-6 rounded transition-colors"
            onClick={() => {
                alert("Simulated Scrape Success!");
                fetchNextProxy();
            }}>
            Report Success & Rotate
          </button>
          
          <button 
            className="bg-[#f97316] hover:bg-[#ea580c] text-[#09090b] font-bold py-2 px-6 rounded transition-colors"
            onClick={() => {
                alert("Simulated Blockade Hit! Blacklisting Node.");
                fetchNextProxy();
            }}>
            Report Blockade & Rotate
          </button>
        </div>
      </div>
    </div>
  );
}
