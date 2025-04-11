import React, { useState } from "react";
import axios from "axios";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSubmit = async e => {
    e.preventDefault();
    setResults([]);
    setError("");
    setSuccess("");

    if (!file) {
      setError("Please select a CSV file before uploading.");
      return;
    }

    const formData = new FormData();
    formData.append("csv_file", file);
    try {
      const res = await axios.post("/api/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" }
      });
      setResults(res.data);
      setSuccess(`Predicted ${res.data.length} entries.`);
    } catch {
      setError("Upload failed. Check CSV format.");
    }
  };

  const downloadSample = () => {
    const headers = "bed,bath,sqft,pricePerSf,lotArea,latitude,longitude,zipCode,city,lotAreaType,homeType\n";
    const sample = "3,2,1800,400,5000,43.6,-79.5,L6H,Oakville,sqft,Detached\n";
    const blob = new Blob([headers + sample], { type: "text/csv" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "sample.csv";
    a.click();
  };

  const exportResults = () => {
    if (results.length === 0) return;
    const headers = "City,Lat,Lon,Price\n";
    const rows = results.map(r =>
      `${r.city},${r.latitude},${r.longitude},${r.predicted_price}`
    ).join("\n");
    const blob = new Blob([headers + rows], { type: "text/csv" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "predictions.csv";
    a.click();
  };

  return (
    <div className="p-4 max-w-3xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Upload CSV for Batch Prediction</h2>
      <form onSubmit={handleSubmit} className="flex items-center gap-4 mb-4">
        <input type="file" onChange={e => setFile(e.target.files[0])} />
        <button type="submit" className="bg-blue-600 text-white p-2 rounded">Upload</button>
        <button type="button" onClick={downloadSample} className="bg-gray-600 text-white p-2 rounded">Download Sample</button>
      </form>
      {error && <div className="text-red-600 mb-2">{error}</div>}
      {success && <div className="text-green-600 mb-2">{success}</div>}
      {results.length > 0 && (
        <div className="mt-4">
          <button onClick={exportResults} className="mb-2 bg-green-700 text-white p-2 rounded">Export to CSV</button>
          <table className="w-full border">
            <thead>
              <tr>
                <th className="text-center">City</th>
                <th className="text-center">Lat</th>
                <th className="text-center">Lon</th>
                <th className="text-center">Predicted Price</th>
              </tr>
            </thead>
            <tbody>
              {results.map((r, i) => (
                <tr key={i} className="border-t">
                  <td className="text-center">{r.city}</td>
                  <td className="text-center">{r.latitude}</td>
                  <td className="text-center">{r.longitude}</td>
                  <td className="text-center">{(r.predicted_price).toLocaleString('en-CA', 
                    {
                      style: 'currency',
                      currency: 'CAD',
                      maximumFractionDigits: 0
                    })}

                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}