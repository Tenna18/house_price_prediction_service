1. **What approach would you use to version and track different models in production?**
My experience with model versioning and tracking is primarily in the context of large language models (LLMs), where I have used Langfuse to manage and monitor different model and prompt versions in production. In Langfuse, I track each model or prompt version using the built-in version parameter, along with relevant metadata and custom evaluation metrics. This allows me to analyze the impact of changes, compare performance across versions, and ensure robust traceability for every prediction or generation. I have also recently explored model lifecycle management in Databricks, where models are registered, versioned, and promoted through different stages using tools like MLflow and Unity Catalog. This approach supports structured deployment workflows and makes it easy to roll back or update models as needed.

    For this particular project, I would adopt a simple but effective model versioning strategy: each trained model artifact would be saved with a unique version identifier (such as a timestamp or semantic version number) and accompanied by metadata describing the training data, parameters, and evaluation results. The API would expose the current model version in its responses or through a dedicated endpoint, ensuring easy traceability and auditability.


2. **What key metrics would you monitor for this API service and the prediction model?**
<u>For this API service:</u>
- *Response Time:* Measures how long the API takes to process and return a response to each request. Monitoring response time helps identify slowdowns and performance bottlenecks that could impact user experience.

- *Latency:* Tracks the delay between when a client sends a request and when the first byte of the response is received. High latency can indicate network issues or backend delays, even if overall response times seem acceptable.

- *Error Rate:* The percentage of requests that fail (typically returning 4xx or 5xx status codes). Monitoring error rate is critical for detecting outages, misconfigurations, or unexpected failures in the service.

- *Uptime:* Measures the percentage of time the API is operational and accessible. High uptime is essential for user trust and business continuity, and it is often tied to service-level objectives or agreements.

- *Utilization:* Refers to the resource usage of the API servers, such as CPU and memory consumption. Monitoring utilization helps ensure the infrastructure can handle current and future loads and can reveal when scaling or optimization is needed.


    <u>For the prediction model: </u>

- *Mean Squared Error (MSE):* Measures the average squared difference between the predicted and actual values in regression tasks. Lower MSE indicates more accurate predictions.

- *Root Mean Squared Error (RMSE):* The square root of MSE, providing error in the same units as the target variable. RMSE is widely used for interpreting model performance in regression.

- *Mean Absolute Error (MAE):* Calculates the average absolute difference between predicted and actual values. MAE is less sensitive to outliers than MSE and RMSE.

- *R² (R-Squared):* Represents the proportion of variance in the target variable explained by the model. Higher R² values indicate better model fit for regression problems.

- *Accuracy:* The ratio of correct predictions to the total number of predictions, commonly used for classification tasks with balanced datasets.

- *Precision:* The proportion of true positive predictions among all positive predictions. High precision means fewer false positives, important in scenarios like fraud detection.

- *Recall:* The proportion of true positive predictions among all actual positives. High recall is critical when missing a positive case is costly, such as in medical diagnosis.

- *F1 Score:* The harmonic mean of precision and recall, providing a balanced metric for classification tasks, especially with imbalanced data.

- *Area Under the ROC Curve (AUC-ROC):* Evaluates a classification model’s ability to distinguish between classes across all thresholds. Higher AUC indicates better overall model performance.