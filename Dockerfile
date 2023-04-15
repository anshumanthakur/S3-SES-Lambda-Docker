FROM public.ecr.aws/lambda/python:3.8

# Copy the requirements for pip + catboost
COPY requirements.txt ./

# Install the python requirements from requirements.txt
RUN python3.8 -m pip install -r requirements.txt

COPY app.py ./

COPY / .

# Set the CMD to your handler
CMD ["app.lambda_handler"]