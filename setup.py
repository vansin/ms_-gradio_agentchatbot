from setuptools import setup, find_packages

setup(
    name='msgradio',
    version='0.1.1',
    packages=find_packages(
        include=[
            'frontend*',
        ]
    ),
    package_data={
        '': ['*.html', '*.css', '*.js'],
    },
    install_requires=[
        # 'gradio',
        # 'openai',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts here
        ],
    },
    author='vanisn',
    author_email='msnode@163.com',
    description='A chatbot using Gradio',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ms_gradio_agentchatbot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)