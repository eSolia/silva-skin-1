from setuptools import setup, find_packages
import os

version = '1.0dev'

setup(name='silvatheme.esolia',
      version=version,
      description="eSolia themes for Silva",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='silvatheme',
      author='Infrae',
      author_email='info@infrae.com',
      url='http://infrae.com/products/silva',
      license='BSD and Creative Commons',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['silvatheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'silva.export.html',
          ],

      )
