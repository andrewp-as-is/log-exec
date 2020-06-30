import setuptools

setuptools.setup(
    name='log-exec',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/log-exec']
)
