# Token Count Microservice (counttokens-microservice)

This project is a microservice that counts tokens for OpenAI models. It exposes a RESTful API endpoint that receives a JSON payload containing a list of messages and a model identifier. It returns a JSON response containing the token count for each message.

## Running the Microservice

To run the microservice, follow these steps:

1. Clone the repository
2. Install [Docker](https://www.docker.com/)
3. Run the following command from the root directory of the project:

```
docker-compose up -d
```

This will build and start the Docker containers needed to run the microservice.

## Using the API

The API endpoint is located at `http://localhost:5000/tokens/count`.

To call the API, send a POST request to the endpoint with the following parameters:

- `Content-Type: application/json`
- `Accept: application/json`
- `messages`: a list of messages, each containing a `role` and `content` fields.
- `model`: a string identifier of the model to use for token counting.

Here's an example `curl` command:

```
curl -X POST \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -i http://localhost:5000/tokens/count \
  --data '{
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English."
        },
        {
            "role": "system",
            "name": "example_user",
            "content": "New synergies will help drive top-line growth."
        },
        {
            "role": "system",
            "name": "example_assistant",
            "content": "Things working well together will increase revenue."
        },
        {
            "role": "system",
            "name": "example_user",
            "content": "Let'\''s circle back when we have more bandwidth to touch base on opportunities for increased leverage."
        },
        {
            "role": "system",
            "name": "example_assistant",
            "content": "Let'\''s talk later when we'\''re less busy about how to do better."
        },
        {
            "role": "user",
            "content": "This late pivot means we don'\''t have time to boil the ocean for the client deliverable."
        }
    ],
    "model": "gpt-3.5-turbo-0301"
}'
```

The API will return a JSON response with the token count for each message.

## License

This project is licensed under the [MIT License](LICENSE.md).


