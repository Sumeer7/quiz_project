import os
import json
import common


class Topic():
    def __init__(self, name):
        self.name = name


def read_topics():
    if not os.path.isfile("topics.json"):
        return []

    fp = open('topics.json', 'r')
    content = fp.read()
    fp.close()
    if content is None or content == "":
        return []
    dict_content = json.loads(content)
    return list(dict_content)


def write_topics(topics):
    fp = open('topics.json', 'w+')
    dump_data = json.dumps(topics, default=common.obj_dict, indent=1)
    fp.write(dump_data)
    fp.close()


def print_topics(topics):
    for i in range(len(topics)):
        print(str(i + 1) + " - " + topics[i]['name'])


def edit_topic():
    topics = read_topics()
    print_topics(topics)
    topic_number = int(input("Enter topic number to be edited"))
    new_name = input("Enter new topic name")
    topics[topic_number - 1]['name'] = new_name
    write_topics(topics)


def delete_topic():
    topics = read_topics()
    print_topics(topics)
    topic_number = int(input("Enter topic number you want to deleted"))
    topics.remove(topics[topic_number - 1])
    write_topics(topics)


def enter_topic_name():
    topic = Topic(input("enter topic name"))
    topics = read_topics()
    topics.append(topic)
    write_topics(topics)
