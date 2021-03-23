FROM python:3.6.7

WORKDIR /app

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
       #Dockerfile
# Now copy in our code, and run it
COPY . .
EXPOSE 8000
CMD ["cd", "videos_fetch"]
CMD [ "python", "manage.py" ,"process_tasks"]
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
