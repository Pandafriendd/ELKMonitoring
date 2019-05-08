# Introduction and Set-ups for the Capstone Project
## requirements
* Install Logstash, Elasticsearch, and Kibana. We are using version 6.6 for all these components.
## Prepare threat data feed
* **malicious.yaml**. Download it from our repo.
* Prepare threat data feed: Blueliv
⋅⋅⋅Indexing the threat data into Elasticsearch by Logstash. Run the following command:
```
bin/logstash -f test9.conf
```
This command will index crimeserver threat data into Elasticsearch. Mention that you should use your own api key to access the data. To create your api key, visit [here](https://community.blueliv.com/#!/get-started/).
