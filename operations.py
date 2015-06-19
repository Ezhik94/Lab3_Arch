
import redis


class Base(object):
    def __init__(self):
        self.base = redis.StrictRedis(host='localhost', port=6379, db=0)

    def create(self, key, data):
        if self.base.set(key, data):
                return 'Document has been added.'
        return 'Document has not been added.'

    def read(self, key):
        result = self.base.get(key)
        if result is None:
            return 'Document has not been read.'
        if len(result) > 0:
            return result

    def update(self, key, data):
        result = self.base.get(key)
        if result is None:
            return "Document doesn't exist."
        self.base.set(key, data)
        return 'Document has been updated.'

    def delete(self, key):
        result = self.base.get(key)
        if result is None:
            return "Document doesn't exist."
        self.base.delete(key)
        return 'Document has been deleted.'
