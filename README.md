#Kafka Demo using Twitter Streaming API

This is a simple demo for streaming tweets in real time from twitter and storing into a single node
[Kafka](https://kafka.apache.org/) cluster. We also demonstrate the use of [Kafka](https://kafka.apache.org/) consumer module to subscribe to the **twitter channel** and consume the tweets uploaded to that channel by the [Kafka](https://kafka.apache.org/) Producer.

###Requirements
  1. [Apache Kafka Framework](https://kafka.apache.org/quickstart)
  2. Python modules mentioned in [requirements.txt](requirements.txt)

###Install Dependencies
  1. `pip install -r requirements.txt`
  2. Download and unzip/untar the [Apache Kafka Framwork](https://kafka.apache.org/quickstart)

###Run the twitter-kafka demo
  1. `cd path/to/apachekafka`
  2. Start zookeeper server: `bin/zookeeper-server-start.sh config/zookeeper.properties`
  3. Start kafka sever: `bin/kafka-server-start.sh config/server.properties`
  4. Create a **key.json** file and add your [Twitter Access Keys](https://dev.twitter.com/oauth/overview/application-owner-access-tokens) in the following json format:
```
     {
          "twitter": {
                "CONSUMER_KEY": "KEY_VALUE",
                "CONSUMER_SECRET": "SECRET_VALUE",
                "ACCESS_TOKEN": "TOKEN_VALUE",
                "ACCESS_TOKEN_SECRET": "SECRET_VALUE"
          }
      }
```
  5. Send to twitter channel: `python tweets-producer.py`
  6. Consume from twitter channel: `python tweets-consumer.py`
