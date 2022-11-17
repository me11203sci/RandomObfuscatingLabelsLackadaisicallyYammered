#!/bin/bash
URL="https://api.random.org/json-rpc/4/invoke"
KEY=$(sed -n 's/RANDOM_KEY=//p' .env)
REQUEST='
{ 
	"jsonrpc": "2.0",
	"method": "generateStrings",
	"params": 
	{
		"apiKey": "'"$KEY"'",
		"n": 1, 
		"length": 8, 
		"characters": "abcdefghijklmnopqrstuvwxyz0123456789",
		"replacement": false 
	},
	"id": 128
}'
RESPONSE=$(
	curl -s -X POST \
	-H "Content-Type: application/json" \
	-d "$REQUEST" \
	"$URL"
)
FILENAME=$(echo "$RESPONSE"| grep -P -o -i '(?<=\[")[a-z0-9]*?(?="\])' - )
DIRECTORY="/home/melesioalbavera/Documents/NOTEBOOK 2022/4 - Files/"
EXTENSION="jpg"
mv $1 "$DIRECTORY""$FILENAME"."$EXTENSION"
echo "File ""$FILENAME"".""$EXTENSION"" created."
