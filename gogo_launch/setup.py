import os
from glob import glob
from setuptools import setup

package_name = 'gogo_launch'

setup(
  name=package_name,
  version='0.1.0',
  py_modules=[
    'simplet_z',
  ],
  data_files=[
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name), glob('launch/*.launch.py'))
  ],
  install_requires=['setuptools'],
  zip_safe=True,
  author='charlyoleg',
  author_email='charlyoleg@fabfolk.com',
  maintainer='charlyoleg',
  maintainer_email='charlyoleg@fabfolk.com',
  keywords=['ROS2'],
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development',
  ],
  description='just for a launch script',
  license='Apache License, Version 2.0',
  tests_require=['pytest'],
  entry_points={
    'console_scripts': [
      'simplet_z = simplet_z:main',
    ],
  },
)

