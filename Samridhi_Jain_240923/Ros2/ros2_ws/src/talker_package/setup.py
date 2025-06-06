from setuptools import find_packages, setup

package_name = 'talker_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Samridhi',
    maintainer_email='samridhi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker_node = talker_package.talker_node:main',
            'publisher_node = talker_package.publisher_node:main',
            'launcher_node = talker_package.launcher_node:main',
        ],
    },
)
