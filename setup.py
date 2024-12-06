from setuptools import setup, find_packages

setup(
    name="OSS_PNG_Transfer",  # 패키지 이름 (PyPI에 업로드될 이름)
    version="0.1.0",  # 초기 버전
    author="sijbwer77, gitleejm, yong8947, Nhh05, lovedosoon",  # 작성자 이름
    author_email="leejm8422@hanyang.ac.kr",  # 작성자 이메일
    description="A Python library for data processing",  # 패키지 설명
    long_description=open("README.md").read(),  # README 내용을 상세 설명으로 사용
    long_description_content_type="text/markdown",  # README 형식 지정
    url="https://github.com/Nhh05/oss_data_library",  # 프로젝트 GitHub URL
    packages=find_packages(),  # 패키지 자동 탐색
    classifiers=[  # PyPI에 표시될 메타데이터
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # 최소 Python 버전
    install_requires=[],  # 의존성 패키지 (예: ['numpy', 'pandas'])
)
