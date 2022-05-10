from setuptools import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='input_manager',
    version='0.0.1',
    description='Make use of mouse and keyboard inputs through your whole application.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['input_manager'],
    package_dir={'': 'src'},
    setup_requires=['wheel'],
    extra_require={
        "dev": [
            'pytest>=3.7',
            'flake8>=3.9.2',
            'tox>=3.24.3',
            'pytest>=6.2.5',
            'pytest-cov>=2.12.1',
            'mypy>=0.910'
        ]
    },
    install_requires=['pysdl2 >= 0.9.7'],
    url="github",
    author="Sven Firmbach",
    author_email="sven.firmbach@gmx.de",
)
