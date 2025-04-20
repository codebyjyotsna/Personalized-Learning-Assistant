import React, { useState, useEffect } from "react";
import axios from "../../services/api";

const RecommendationList = () => {
  const [resources, setResources] = useState([]);

  useEffect(() => {
    axios.post("/recommend", { learning_style: "visual" })
      .then(response => setResources(response.data.resources))
      .catch(error => console.error(error));
  }, []);

  return (
    <ul>
      {resources.map((res, index) => (
        <li key={index}>{res}</li>
      ))}
    </ul>
  );
};

export default RecommendationList;
