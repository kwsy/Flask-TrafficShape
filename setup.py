import setuptools

setuptools.setup(
    name='Flask-Trafficshape',
    version='1.0.0',
    url='https://github.com/kwsy/Flask-TrafficShape',
    license='MIT',
    author='kwsy',
    author_email='xigongda200608@163.com',
    description='shape the traffic by tokenbucket and leakbucket method',
    long_description='Full documentation can be found on the Flask-Trafficshape "Home Page".',
    py_modules=['hibiscus_traffic'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)