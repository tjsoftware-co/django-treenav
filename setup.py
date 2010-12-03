from setuptools import setup, find_packages

setup(
    name='django-treenav',
    version=__import__('treenav').__version__,
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(exclude=['sample_project']),
    include_package_data=True,
    url='http://github.com/caktus/django-treenav',
    license='LICENSE.txt',
    description='Extensible, hierarchical, and pluggable navigation system '
                'for Django sites',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.rst').read(),
)
