from setuptools import setup, find_packages

setup(
    name='bs-tool',
    version='1.0.0',
    packages=find_packages(),
    scripts=[],
    entry_points={
        'console_scripts': [
            'wechat_login=bs.wechat_login:main'
        ]
    },

    author='Bearsuny',
    author_email='sir_fengfan@163.com',
    description='bs-tool',
    license='GPL-3.0',
    url='https://github.com/Bearsuny'
)
