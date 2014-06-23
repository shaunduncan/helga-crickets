from setuptools import setup, find_packages

setup(
    name='helga-crickets',
    version='0.0.2',
    description=('Helga plugin that will respond with the word crickets'
                 'after a question has gone unacknowledged for a configurable amount of time.'),
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
