from setuptools import setup
import ella_series

setup(
    name='Ella-Series',
    version=ella_series.__versionstr__,
    description='Ella Series - add support for series of Publishable objects.',
    long_description='\n'.join((
        'Ella Series',
        '',
        'Add support for series of Publishable objects.',
        '',
    )),
    author='Ella Development Team',
    author_email='dev@ella-cms.com',
    maintainer='Vitek Pliska',
    maintainer_email='whit@jizak.cz',
    license='BSD',
    url='http://github.com/ella/ella-series/',

    packages=('ella_series',),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'ella>=2.0.4',
    ],
#    test_suite='test_ella.run_tests.run_all'

)
