from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='boomak-clipy',
    version='0.0.1',
    description='Boomak — Command-Line Based Application',
    long_description=readme(),
    url='https://github.com/resurtm/boomak-clipy',
    download_url='https://github.com/resurtm/boomak-clipy/archive/v0.0.1.tar.gz',
    author='resurtm',
    author_email='resurtm@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['boomak_clipy'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
    ],
)
