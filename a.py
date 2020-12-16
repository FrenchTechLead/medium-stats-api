import requests

story_url = "https://mecheri-akram.medium.com/this-story-has-n-views-53484fac8131"
c = requests.get(story_url).content.decode("utf-8")
c = c.split("clapCount\":")[1]
endIndex = c.index(",")
claps = int(c[0:endIndex])
c = c.split("responsesCount\":")[1]
endIndex = c.index(",")
comments = int(c[0:endIndex])
print(claps)
print(comments)
