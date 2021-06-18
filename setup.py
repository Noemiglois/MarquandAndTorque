from setuptools import setup, find_packages

REQUIRED_PACKAGES = ["pandas==0.25.1","scipy==1.6.3", "nibabel==3.2.1", "sklearn==0.0", 
                     "torch==1.8.1", "numpy==1.20.3", "scikit-learn==0.24.2", "asn1crypto==0.24.0",
                     "certifi==2019.3.9", "cffi==1.12.2", "chardet==3.0.4", "cryptography==2.6.1",
                     "idna==2.8", "joblib==1.0.1", "packaging==20.9", "pycosat==0.6.3", 
                     "pycparser==2.19", "pyOpenSSL==19.0.0", "pyparsing==2.4.7", "PySocks==1.6.8",
                    "python-dateutil==2.8.1", "pytz==2021.1", "requests==2.21.0", "six==1.12.0",
                    "ruamel-yaml==0.15.46", , "threadpoolctl==2.1.0", "typing-extensions==3.10.0.0",
                     "urllib3==1.24.1"]

setup(name='nispat',
      version='0.2',
      install_requires=REQUIRED_PACKAGES,
      description='Spatial methods for neuroimaging data Pedro M. Gordaliza docker',
      url='http://github.com/amarquand/nispat',
      author='Pedro M. Gordaliza modified from Andre Marquand',
      author_email='pmacias@ing.uc3m.es',
      license='GNU GPLv3',
      packages=find_packages(),
      zip_safe=False)
