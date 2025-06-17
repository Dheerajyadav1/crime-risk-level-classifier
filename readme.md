# 🛡️ Crime Risk Level Prediction API

This API predicts the level of crime risk based on:
- City
- Age
- Gender
- Current Time

## 🚀 API Endpoints

- `GET /` — Health check
- `POST /predict/` — Returns predicted risk level (Low, Medium, High)

## 🔧 Input Example

```json
{
  "city": "Mumbai",
  "age": 25,
  "gender": 1
}


## Gender Values
```json
{
  "0": "Male",
  "1": "Female",
  "2": "Other"
}
