from setuptools import setup


setup(
    name='Py-Authorize',
    version='1.2.2.1',
    author='Vincent Catalano',
    author_email='vincent@vincentcatlano.com',
    url='https://github.com/vcatalano/py-authorize',
    download_url='',
    description="A full-featured Python API for Authorize.net's AIM, CIM, ARB and Reporting APIs.",
    long_description=__doc__,
    license='MIT',
    install_requires=[
        'colander',
    ],
    packages=[
        'authorize',
        'authorize.apis',
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
