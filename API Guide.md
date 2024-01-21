# Fizz Buzz REST Server API Documentation

## Base URL
The base URL for the API is `http://localhost:8000`.

## 1. Get Fizz-Buzz List

### Endpoint
- **URL:** `/fizzbuzz`
- **Method:** GET

### Query Parameters
- `int1` (optional, default: 3): Integer to replace multiples of.
- `int2` (optional, default: 5): Another integer to replace multiples of.
- `limit` (optional, default: 100): Upper limit for the list.
- `str1` (optional, default: "fizz"): String to replace multiples of `int1`.
- `str2` (optional, default: "buzz"): String to replace multiples of `int2`.

### Example Request
```http
GET http://localhost:5000/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz
```

### Example Response
```http
1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz
```

## 2. Get Requests Statistics

### Endpoint
- **URL:** `/statistics`
- **Method:** GET

### Example Request
```http
GET http://localhost:5000/statistics
```

### Example Response
```http
{
    "most_used_request": "GET /fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz",
    "hits": 10
}

```

This documentation provides information about the available endpoints, their parameters, example requests, and expected responses. 
