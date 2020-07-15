from setuptools import setup, find_packages
setup(
    name='wpe',   #app name
    sdk_version='1.0.1',    #which sdk version that app runing
    version='0.0.1',    #app version
    author='TonyStark',   
    author_email='info@wongpaiboon.com',
    description='Water Level',
    license='PRIVATE',  #app license, you can use GPL, MIT, BSD...
    packages = find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    install_requires=[
    ],
    #your app entrty points, you just implement it like "appnamne = Application:main" 
    entry_points = """
		[console_scripts]
		wpe = Application:main
		"""
)