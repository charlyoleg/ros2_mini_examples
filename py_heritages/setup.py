from setuptools import setup

package_name = 'py_heritages'

setup(
  name=package_name,
  version='0.1.0',
  py_modules=[
    'melting_pot',
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
  description='A py-module that imports stuff',
  license='Apache License, Version 2.0',
  tests_require=['pytest'],
  entry_points={
    'console_scripts': [
      'melting_pot = melting_pot:main',
    ],
  },
)

