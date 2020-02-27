from setuptools import setup, find_packages

setup(
	name='project0',
	version='1.0',
	author='Nithivarn Reddy Shanigaram',
	authour_email='nithivarn.reddy.shanigaram-1@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['pandas==1.0.1',
                      'PyPDF2==1.26.0'
					  ],
	setup_requires=['pytest-runner'],
	tests_require=['pytest']
)