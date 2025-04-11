import React, { useState } from "react";
import axios from "axios";

const Predict = () => {
  const [formData, setFormData] = useState({
    bed: "", bath: "", sqft: "", pricePerSf: "", lotArea: "",
    latitude: "", longitude: "", zipCode: "", city: "",
    lotAreaType: "", homeType: ""
  });
  const [price, setPrice] = useState(null);

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await axios.post("/api/predict/", formData);
      setPrice(res.data.predicted_price);
    } catch (err) {
      alert("Prediction failed.");
    }
  };

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Predict House Price</h2>
      <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">
        {Object.keys(formData).map(key => (
          <input
            key={key}
            name={key}
            value={formData[key]}
            onChange={handleChange}
            placeholder={key}
            className="border p-2 rounded"
          />
        ))}
        <button type="submit" className="col-span-2 bg-blue-500 text-white p-2 rounded">
          Predict
        </button>
      </form>
      {price !== null && (
        <div className="mt-4 text-xl font-semibold text-green-600">
          Predicted Price: {price.toLocaleString('en-CA', { style: 'currency', currency: 'CAD', maximumFractionDigits: 0 })}
        </div>
      )}
    </div>
  );
};

export default Predict;
