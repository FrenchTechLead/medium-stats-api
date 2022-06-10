### MEDIUM-STATS-API

Due to the lack of functionalities in the [official medium REST API](https://github.com/Medium/medium-api-docs),
We created this API that makes it possible to retrieve stats of a specefic medium story.  

# USAGE
REQUEST :

```GET: http://localhost:8080/api/stats?story_url=THE_URL_OF_THE_MEDIUM_STORY```

RESPONSE :
``` JSON 
{
   "claps": 78,
   "comments": 1
}
```
