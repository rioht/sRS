from setuptools import setup

setup(name='srs',
      version='0.8',
      description='srs',
      author='Dave Cha',
      author_email='dev.rioht@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask==0.10.1', 'Flask_Mail==0.9.1', 'Flask_Wtf==0.11', 'WTForms==1.0.5', 'praw==2.1.21', 'requests==2.7'],
     )
