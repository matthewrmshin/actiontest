from setuptools import find_packages, setup
import os.path


HERE = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as handle:
    long_description = handle.read()


setup(
    name='actiontest',
    version='0.1',
    description='Testing Action using Conda and Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/matthewrmshin/actiontest',
    author='Matt Shin',
    author_email='matthew.shin@metoffice.gov.uk',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Software Distribution',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # keywords='post-processing',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=[
    ],
    # extra_requires={
    #     'test': ['flake8', 'pytest', 'pytest-cov'],
    # },
    # package_data={},
    # entry_points={'console_scripts': ['...', ...]},
    # project_urls={},
)
