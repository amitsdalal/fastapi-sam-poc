# fastapi-sam-poc

## Make sure to have sam cli installed && AWS cli configured. 

# Deploy FastAPI on Lambda/API Gateway using SAM

```sh
# setup locally
virtualenv venv
source venv/bin/activate

pip install -r tests/requirements.txt -r app/requirements.txt

# test
pytest -v

# deploy
sam build --use-container
sam deploy --guided

# destroy
aws cloudformation delete-stack --stack-name fastapi-sam-poc

# run
uvicorn app.app:app --reload
```