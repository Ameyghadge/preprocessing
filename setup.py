import setuptools


with open('Readme.md','r') as file:
	long_description=file.read()

setuptools.setup(
	name='preprocess',
	version='0.0.1',
	author='amey',
	long_description=long_description,
	packages=setuptools.find_packages(),
	classifiers=[
	'programming Language::python::3',
	'License::OSI Approved::MIT License',
	'Operating System:: OS Independent'],
	python_requries='>3.5'




	)