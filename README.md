# fetch_youtube_feed

# To run

```
cd videos_fetch
python manage.py process_tasks
python manage.py runserver 
```
These two python commands must be run in different windows
## added dockerfile too
To build docker

```
docker build . -t videos_fetch_final
```
Keep your API Keys in "videos_fetch/youtube/api_keys.py"

It feteches every 5min from youtube
I fyou want to change time we can edit in views.py repeat variable

