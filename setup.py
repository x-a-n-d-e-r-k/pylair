from distutils.core import setup

setup(
    name="pylair",
    version="1.0.2",
    author='Dan Kottmann, XanderK',
    author_email='djkottmann@gmail.com, xanderk@notbo.red',
    packages=['pylair'],
    url='https://github.com/x-a-n-d-e-r-k/pylair',
    license='LICENSE',
    description='Python library for interacting with Lair 2.0 API.',
    install_requires=[
        "requests >= 3.4.0"
    ],
)
