#!/usr/bin/env python3

from setuptools import setup


from fuo_bilibili import __version__


setup(
    name='fuo_bilibili',
    version=__version__,
    description='feeluown bilibili plugin',

    author='cosven',
    author_email='yinshaowen241@gmail.com',

    # packages=[
    #     'fuo_bilibili',
    # ],
    py_modules=['fuo_bilibili'],
    url='https://github.com/feeluown/feeluown-bilibili',
    keywords=['feeluown', 'plugin', 'bilibili'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'feeluown>=3.7.11',
    ],
    entry_points={
        'fuo.plugins_v1': [
            'bilibili = fuo_bilibili',
        ]
    },
)
