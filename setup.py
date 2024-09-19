import setuptools

setuptools.setup(
        name = 'cropall',
        version = '0.1.0',
        scripts = [ 'cropall' ],
        author = 'Venkataram Edavamadathil Sivaram',
        author_email = 'vesion4690@gmail.com',
        description = 'Batch crop tool',
        long_description = 'Batch crop tool',
        long_description_content_type = 'text/markdown',
        # url = 'https://github.com/vedavamadathil/smake',
        packages = setuptools.find_packages(),
        # install_requires = ['pyyaml', 'colorama'],
        classifiers = [
                'Programming Language :: Python :: 3',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
        ],
)
