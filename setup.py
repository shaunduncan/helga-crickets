from setuptools import setup, find_packages

setup(
    name='helga-crickets',
    version='0.0.1',
    author="Shaun Duncan",
    author_email="shaun.duncan@gmail.com",
    url="https://github.com/shaunduncan/helga-crickets",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    entry_points=dict(
        helga_plugins=[
            'crickets = helga_crickets:crickets',
        ],
    ),
)
