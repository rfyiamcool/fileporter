from setuptools import setup

install_requires = [
    'tornado>=3.1.0',
]

setup(
    name='fileporter',
    version='1.0',
    description='support download/upload/browser,use tornado',
    author='fengyun',
    author_email='rfyiamcool@163.com',
    url='https://github.com/rfyiamcool/fileporter',
    license='BSD',
    py_modules=['fileporter'],
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Utilities',
    ]
)
