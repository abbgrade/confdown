__author__ = 'abb'


class Config(object):

    class Parser(object):

        def __init__(self):
            self.state = 0

            self.config_name = None
            self.definition = []
            self.key = None
            self.description = []
            self.value = []

        def parse(self, line):

            if self.state == 3 and not line.startswith('\t'):
                self.definition.append((self.key, '\n'.join(self.description), '\n'.join(self.value)))
                self.key = None
                self.description = []
                self.value = []

            if self.state == 0 and line.startswith('# '):
                self.config_name = line[2:]
                self.state = 1

            elif self.state == 1 and line.startswith('## '):
                self.key = line[3:]
                self.state = 2

            elif self.state == 2 and not line.startswith('\t'):
                self.description.append(line)
                self.state = 2

            elif self.state in [2, 3] and line.startswith('\t'):
                self.value.append(line[1:])
                self.state = 3

        def get_config(self):
            self.definition.append((self.key, '\n'.join(self.description), '\n'.join(self.value)))
            return Config(self.config_name, self.definition)

    @classmethod
    def parse(cls, content):
        parser = Config.Parser()
        for line in content.split('\n'):
            parser.parse(line)

        return parser.get_config()

    def __init__(self, config_name, *definition):
        assert isinstance(config_name, basestring)
        self.config_name = config_name

        assert definition
        self.definition = definition


    def dump(self):
        return '''# %s

''' % self.config_name + '\n'.join(
            ['''## %(key)s

%(description)s

    %(value)s
''' % {'key': definition[0], 'description': definition[1], 'value': definition[2]} for definition in self.definition])