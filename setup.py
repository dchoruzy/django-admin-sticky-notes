import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-admin-sticky-notes",
    version="1.0.0",
    author="Dariusz Choruzy",
    author_email="dariusz.choruzy@gmail.com",
    description="Django admin sticky notes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dchoruzy/django_admin_sticky_notes",
    project_urls={
        "Bug Tracker": "https://github.com/dchoruzy/django_admin_sticky_notes/issues",
    },
    license='MIT License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
)