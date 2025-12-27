# 📈 Rising Stock Recommender

**Rising Stock Recommender**는 다양한 산업 섹터별 유망 주식을 한눈에 파악하고, 실시간에 가까운 주가 데이터와 트렌드 차트를 제공하는 Streamlit 기반 웹 어플리케이션입니다.

프로젝트 개요 (Project Overview)
사용자가 관심 있는 산업 분야(AI, 반도체, 바이오 등)를 선택하면, 해당 분야의 주요 기업 리스트와 함께 최신 주가 정보, 전일 대비 등락률, 그리고 지난 1년간의 주가 흐름 차트를 시각화하여 제공합니다. 
투자 결정을 돕기 위해 직관적인 UI/UX를 제공하는 데 초점을 맞추었습니다.

사용된 기술 및 라이브러리 (Tech Stack)
프로젝트 구현을 위해 다음과 같은 파이썬 라이브러리가 사용되었습니다:

Framework : Streamlit (웹 인터페이스 구현)
Data Analysis : Pandas, Numpy (데이터 처리 및 연산)
Stock Data: yfinance (Yahoo Finance API를 통한 실시간 주가 데이터 수집)
Visualization: Matplotlib, Seaborn (주가 트렌드 차트 시각화)
Networking: Requests (데이터 통신)

코드 구성 (Project Structure)
코드는 단일 파일 app.py로 구성되어 있으며 주요 로직은 다음과 같습니다.

1. 각 섹터(SECTOR_MAP)와 기업 설명(COMPANY_INFO)을 딕셔너리 형태로 관리합니다.
2. fetch_stock() 함수를 통해 특정 종목의 1년치 이력을 가져옵니다.
3. CSS를 활용하여 핑크색 배경과 검은색 텍스트 등 가독성 높은 테마를 적용했습니다.
4. st.session_state를 사용하여 시작 화면 -> 섹터 선택 -> 결과 화면으로 이어지는 페이지 전환을 관리합니다.
5. st.metric을 사용하여 현재가와 변동폭을 강조하고, matplotlib 차트를 통해 주가 흐름을 시각적으로 보여줍니다.

실행 방법 (How to Run)
로컬 환경에서 실행하려면 아래 명령어를 입력하세요:

pip install streamlit pandas numpy matplotlib seaborn yfinance
streamlit run app.py
