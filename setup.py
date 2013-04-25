from setuptools import setup, find_packages

setup(
    name='blimp-cli',
    version='0.5.4',
    author='Yamil Asusta',
    author_email='yamil.asusta@upr.edu',
    scripts=['blimp'],
    url='https://github.com/elbuo8/blimp-cli/',
    download_url='https://github.com/elbuo8/blimp-cli/tarball/master',
    license='MIT License',
    description='CLI interface for Blimp Tasks API',
    long_description='CLI interface for Blimp Tasks API',
    install_requires=[
        'blimp'
    ],
)
