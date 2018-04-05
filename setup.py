from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='mpu6050-raspberrypi',
      version='1.1.0.0',
      description='A Python module for accessing the MPU-6050 digital accelerometer and gyroscope on a Raspberry Pi.',
      keywords='mpu6050 raspberry',
      url='https://github.com/himay81/mpu6050',
      author='himay81',
      author_email='jamie.baxter@tutanota.com',
      license='MIT',
      packages=['mpu6050'],
      scripts=['bin/mpu6050-example'],
      zip_safe=False,
      install_requires=['smbus2'],
      long_description=readme())
