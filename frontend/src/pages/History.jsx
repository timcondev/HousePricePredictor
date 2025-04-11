import React, { useEffect, useState } from "react";
import axios from "axios";

const History = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("/api/history/").then(res => {
      setData(res.data);
      initMap(res.data);
    });
  }, []);

  const initMap = (points) => {
    const map = new window.google.maps.Map(document.getElementById("map"), {
      zoom: 8,
      center: { lat: 43.5, lng: -79.7 },
    });

    points.forEach(p => {
      new window.google.maps.Marker({
        position: { lat: p.latitude, lng: p.longitude },
        map,
        title: `$${p.predicted_price}`
      });
    });
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-6">
      <h2 className="text-3xl font-bold text-center mb-4">Prediction History</h2>

      <table className="w-full text-left border-collapse">
        <thead>
          <tr className="border-b font-medium">
            <th>City</th>
            <th>Lat</th>
            <th>Lon</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {data.map((r, i) => (
            <tr key={i} className="border-t">
              <td>{r.city}</td>
              <td>{r.latitude.toFixed(2)}</td>
              <td>{r.longitude.toFixed(2)}</td>
              <td>{r.predicted_price.toLocaleString("en-CA", {
                style: "currency",
                currency: "CAD",
                maximumFractionDigits: 0,
              })}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default History;
