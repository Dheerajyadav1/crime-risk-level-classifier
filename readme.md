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
```

## Gender Values
```json
{
  "0": "Male",
  "1": "Female",
  "2": "Other"
}
```

## Valid Cities are
'Ahmedabad', 'Chennai', 'Ludhiana', 'Pune', 'Delhi', 'Mumbai',
       'Surat', 'Visakhapatnam', 'Bangalore', 'Kolkata', 'Ghaziabad',
       'Hyderabad', 'Jaipur', 'Lucknow', 'Bhopal', 'Patna', 'Kanpur',
       'Varanasi', 'Nagpur', 'Meerut', 'Thane', 'Indore', 'Rajkot',
       'Vasai', 'Agra', 'Kalyan', 'Nashik', 'Srinagar', 'Faridabad'
