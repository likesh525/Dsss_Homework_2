from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    author='Likesh Gopalanayaka',
    author_email='bewithlikesh@gmail.com',
    description='A math quiz game to test your math skills.',
    long_description_content_type='text/markdown',
    url='https://github.com/likesh525/Dsss_Homework_2/tree/main/math_quiz',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',
        ],
    },
    python_requires='>=3.6',
)
