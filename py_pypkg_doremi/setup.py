from setuptools import setup

package_name = 'py_pypkg_doremi'

setup(
  name=package_name,
  version='0.1.0',
  packages=[
    'doremi',
  ],
  data_files=[
    ('share/' + package_name, ['package.xml']),
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
  description='a stupid python-package',
  license='Apache License, Version 2.0',
  tests_require=['pytest'],
  entry_points={
    'console_scripts': [
      'simplet_x = doremi.simplet_x:main',
      'simplet_y = doremi.simplet_y:main',
    ],
  },
)

