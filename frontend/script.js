const form = document.getElementById("carForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        model: document.getElementById("model").value,
        year: parseInt(document.getElementById("year").value),
        km_driven: parseInt(document.getElementById("km_driven").value),
        fuel_type: document.getElementById("fuel_type").value,
        transmission: document.getElementById("transmission").value,
        city: document.getElementById("city").value,
        owners: parseInt(document.getElementById("owners").value),
        condition: document.getElementById("condition").value
    };

    resultDiv.innerHTML = "Predicting...";

    try {

        const response = await fetch("http://127.0.0.1:8000/predict-price/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        resultDiv.innerHTML = `
            <h3>Prediction Result</h3>
            <p>${result.price_estimate}</p>
        `;

    } catch (error) {

        resultDiv.innerHTML = "Error connecting to backend.";
        console.error(error);
    }
});