from distutils.core import setup

setup(
  name='RPi.GPIO-def',
  packages=['RPi.GPIO', 'RPi.GPIO.definitions', 'RPi.GPIO.definitions.PWM', 'RPi.GPIO.definitions.functions'],
  version='0.1.1-alpha',
  description='Definition library for RPi.GPIO(used for IntelliSense)',
  author='Lyubomir Rumenov',
  author_email='lubeto_9@mail.bg',
  url='https://github.com/Def4l71diot/RPi.GPIO-def',
  download_url='https://github.com/Def4l71diot/RPi.GPIO-def/tarball/0.1.1-alpha',
  keywords=['raspberry', 'gpio', 'RPi.GPIO', 'definition', 'windows', 'linux', 'RPi', 'GPIO'],
  classifiers=[],
)
