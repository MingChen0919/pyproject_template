import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="project_name",
	version="0.0.1",
	author="Ming Chen",
	author_email="mingchen@example.com",
	description="A small example package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/pypa/project_name",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	install_requires=[
		'pytest>=4.3.1',
		'pytest-runner>=4.4',
	],
	setup_requires=['pytest-runner'],
	tests_require=['pytest'],
)