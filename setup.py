from setuptools import setup

setup(name='confdown',
      version='0.1',
      description='A Markdown-based self documenting configuration lib',
      url='http://github.com/abbgrade/confdown',
      author='Steffen Kampmann',
      author_email='confdown@abbgra.de',
      license='LGPL3',
      packages=['confdown'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)