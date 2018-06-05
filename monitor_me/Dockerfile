FROM python
# Run these commands

COPY . ~
WORKDIR ~
RUN pip install pipenv
RUN pipenv install
CMD pipenv run python3 app.py
