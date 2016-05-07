from setuptools import setup, find_packages


setup(
    name='pi',
    version='1.0',
    author='Samar Agrawal',
    author_email='samar@enstino.com',
    packages = find_packages(),
    package_dir = {'': '.'},
    install_requires=['flask'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=True,
)


