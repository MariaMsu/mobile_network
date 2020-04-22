from setuptools import setup, find_packages


setup(
    name="mobile_network",
    version="0.0.22",
    author="m.cherepnina",
    description="utility for determining the number of unavailable users",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            "call_counter=mobile_network.counter:call_counter",
            "run_server=mobile_network.server:run_server"
        ]
    },
)
