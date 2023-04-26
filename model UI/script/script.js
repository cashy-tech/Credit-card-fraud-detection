const transactionForm = document.getElementById("transaction-form");
const transactionInput = document.getElementById("transaction-input");
const predictionOutput = document.getElementById("prediction-output");

transactionForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const response = await fetch("http://localhost:5000/predict", {
    method: "POST",
    body: transactionInput.value,
  });

  const data = await response.json();

  // Set the prediction output text and color based on the prediction result
  if (data.prediction == 0) {
    predictionOutput.value = "This was a legit transaction. Thank you";
    predictionOutput.style.color = "green";
    predictionOutput.style.fontSize = "20px";
  } else if (data.prediction == 1) {
    predictionOutput.value =
      "This was a fraud transaction. Please take necessary actions";
    predictionOutput.style.color = "red";
    predictionOutput.style.fontSize = "20px";
  }
  // else {
  //   predictionOutput.value = "You entered invalid transaction details";
  //   predictionOutput.style.color = "red";
  //   predictionOutput.style.fontSize = "20px";
  // }
});