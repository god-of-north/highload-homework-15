docker run -it --rm logstash:7.16.1 logstash -e "input { stdin { } } output { stdout { } }"
