__author__ = 'abb'

from unittest import TestCase
import confdown
import markdown
from bs4 import BeautifulSoup


class TestConfig(TestCase):

    def test_inherit_config(self):

        config = confdown.Config(
            'Custom Config',
            ('hostname', 'The domain name or the IP address of the server.', 'localhost'),
            ('port', 'The port of the server', '8080')
        )

        config_content = config.dump()

        print config_content

        self.assertIn('hostname', config_content)

        doc_content = markdown.markdown(config_content)

        self.assertIn('hostname', doc_content)

        print doc_content
        soup = BeautifulSoup(doc_content)

        headings = soup.find_all('h2')

        self.assertIn('hostname', headings[0].text)
        self.assertIn('port', headings[1].text)

        paragraphs = soup.find_all('p')

        self.assertIn('domain name', paragraphs[0].text)
        self.assertIn('port', paragraphs[1].text)

        new_config = confdown.Config.parse(config_content)
        assert isinstance(new_config, confdown.Config)