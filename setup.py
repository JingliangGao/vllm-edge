from setuptools import setup, find_packages

setup(
    name="vllm-edge",
    version="0.1.0",
    description="Efficient LLM inference for edge devices",
    author="JingliangGao",
    author_email="1174003943@qq.com",  # 可以添加您的邮箱
    url="https://github.com/JingliangGao/vllm-edge",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
)