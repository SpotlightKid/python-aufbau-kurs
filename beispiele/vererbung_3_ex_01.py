  class JsonSerializableMixin:
      def to_json(self):
          import json
          return json.dumps(self.__dict__)

  class PrintableMixin:
      def print(self):
          print(self)

  class DataObject(JsonSerializableMixin, PrintableMixin):
      def __init__(self, value):
          self.value = value
  