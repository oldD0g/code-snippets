# See https://developer.atlassian.com/cloud/confluence/rest-api-examples/
# for these examples

# So easy to commit an API key to github, ouch!
apiKey="$(< ivand-APIkey.txt)"
#file1="$(< answer.txt)"
curl -u ivanskyd@gmail.com:${apiKey} -X GET "https://ivand.atlassian.net/wiki/rest/api/content" | python -mjson.tool