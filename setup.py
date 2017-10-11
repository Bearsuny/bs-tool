from setuptools import setup, find_packages

setup(
    name='bear_tool',
    version='1.0.1',
    packages=find_packages(),
    scripts=[],
    entry_points={
        'console_scripts': [
            'wechat_login=bear_tool.wechat_login:main'
        ]
    },

    author='bearsuny',
    author_email='sir_fengfan@163.com',
    description='bear_tool',
    license='LGPL',
    url='https://www.python.org/'
)
