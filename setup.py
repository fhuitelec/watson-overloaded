from setuptools import setup, find_packages

setup(
    name='watson-overloaded',
    version='0.0.1',
    description='Overload time-tracking tool "watson"',
    url='https://github.com/fhuitelec/watson-overloaded',
    author='Evaneos',
    author_email='fabien@huitelec.fr',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Scheduling',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='watson time tracking',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['watson-overloaded=fhuitelec_watson_overloaded.watson:__main__'],
    },
    python_requires='>=3.8',
    install_requires=[
        'prompt-toolkit~=3.0'
    ],
)
