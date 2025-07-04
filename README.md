
<img width="1064" alt="정보보안깃허브사진" src="https://github.com/user-attachments/assets/66527bd5-12d7-4758-9382-4fd60c0cb42b" />

# 💬 Python 소켓 채팅 프로그램

Python의 socket 라이브러리를 활용하여 서버-클라이언트 간 실시간 채팅이 가능한 네트워크 프로그램을 구현하였습니다.
GUI는 tkinter 라이브러리를 활용해 사용자 친화적인 인터페이스를 구성하였으며, 메시지 송수신은 멀티스레딩을 적용하여 실시간으로 처리하였습니다.
또한, 클라이언트와 서버 간 통신은 TCP 기반으로 안정적으로 설계하는 데 중점을 두었습니다.

# 🎯 프로젝트 목표
- **소켓 통신을 활용한 실시간 네트워크 프로그래밍 학습:** Python의 socket 모듈을 활용하여 TCP 기반의 안정적인 서버-클라이언트 구조를 직접 구현함으로써, 실시간 메시지 송수신 구조와 네트워크 통신의 기본 원리를 이해하고 실습하는 것을 목표로 하였습니다.

- **GUI 기반 사용자 인터페이스 구성:** tkinter 라이브러리를 사용하여 채팅 인터페이스를 구성하고, 사용자가 직관적으로 채팅에 참여할 수 있는 환경을 구축하였습니다. 이를 통해 텍스트 기반이 아닌 시각적인 사용자 경험(UX) 을 고려한 프로그램 개발을 실습합니다.

- **멀티스레딩을 통한 비동기 처리 구현**
클라이언트 프로그램에서는 멀티스레딩을 통해 메시지 수신과 GUI 동작을 병렬로 처리함으로써, 사용자 인터페이스가 중단되지 않도록 설계하였습니다. 이를 통해 동시성 제어의 개념과 스레드 활용 방법을 학습합니다.

- **사용자 목록 실시간 공유 및 귓속말 기능 구현**
서버에서 연결된 사용자 목록을 모든 클라이언트에 실시간으로 전송하며, 특정 사용자를 선택해 1:1 메시지를 전송할 수 있는 귓속말 기능(/w)을 추가하였습니다. 이를 통해 간단한 사용자 상태 관리와 메시지 라우팅 로직을 구현해보는 경험을 쌓습니다.

# 💻 기술 스택
* OS: macOS
* 개발 도구: VSCode
* 주요 기술: Python

👥 프로젝트 작업인원: 개인 프로젝트

🗓️ 프로젝트 완료일: 2025-05-15

# 🛠️ 주요 기능 및 특징

- **서버-클라이언트 간 실시간 채팅 기능 구현:** socket 모듈을 이용해 TCP 기반의 안정적인 통신 구조를 구축하고, 서버와 다수의 클라이언트 간 메시지를 실시간으로 주고받을 수 있도록 구현했습니다.

- **멀티스레딩을 활용한 비동기 수신 처리:** 클라이언트 측에서 메시지 수신을 별도의 스레드로 처리함으로써 GUI 응답이 멈추지 않고 자연스럽게 작동하며, 네트워크 병목 없이 실시간 소통이 가능하도록 설계했습니다.

- **귓속말(1:1 메시지) 기능 구현:** `/w` 유저명 메시지 형식의 명령을 통해 특정 사용자에게만 비공개 메시지를 보낼 수 있는 귓속말 기능을 구현하여, 단순한 브로드캐스트 외의 커뮤니케이션 방식도 지원합니다.

- **tkinter 기반 GUI 채팅 인터페이스 구성:** `tkinter`를 활용해 채팅 목록, 입력창, 전송 버튼, 사용자 선택 콤보박스를 갖춘 사용자 인터페이스를 구성해 편리함을 제공합니다.

# 🔍 문제 해결 및 사례
- **멀티스레딩 적용 시 GUI 멈춤 현상**: 초기에는 메시지 수신과 GUI 처리를 단일 스레드에서 수행하여, 수신 대기 중 사용자 인터페이스가 멈추는 현상이 발생했습니다. 이를 해결하기 위해 `threading.Thread`를 활용해 메시지 수신을 별도 스레드로 처리하여, 사용자 입력과 화면 출력이 동시에 자연스럽게 작동되도록 개선했습니다.

- **서버에서 접속 사용자 목록 동기화 문제 해결:** 클라이언트 접속과 퇴장 시 사용자 목록을 서버에서 동기화하여 클라이언트 측에 전달하는 로직 구현에서, 타이밍 이슈로 인해 목록이 반영되지 않는 문제가 발생했습니다. `USERLIST:` 접두어를 붙여 사용자 목록을 구분하고, 클라이언트는 이를 받아 `Combobox`에 실시간 반영하도록 처리하여 문제를 해결했습니다.

- **사용자 이름 중복 처리 로직 누락 문제 해결:** 처음에는 여러 사용자가 동일한 이름으로 접속할 수 있었고, 이로 인해 귓속말 기능이나 사용자 식별이 혼란스러워졌습니다. `addUser()` 메서드에 중복 이름 체크 조건을 추가하고, 이미 등록된 이름일 경우 안내 메시지를 전송하여 문제를 사전에 방지할 수 있도록 처리했습니다.

# 📚 성과 및 배운 점

- **소켓 통신의 동작 원리 및 TCP 기반 네트워크 구조에 대한 이해:** 클라이언트와 서버 간의 데이터 송수신 과정을 직접 구현하면서, TCP 소켓 통신의 구조와 흐름, `bind` `listen` `accept` `connect` 등의 함수 동작 원리를 실습을 통해 명확히 이해할 수 있었습니다.

- **멀티스레딩을 활용한 비동기 처리 경험:** GUI와 수신 로직을 분리하기 위해 멀티스레딩을 적용하면서, Python에서의 스레드 개념과 동시성 처리 방법을 배웠습니다. 특히, GUI 이벤트 루프와 네트워크 수신이 동시에 동작하도록 설계한 경험은 추후 병렬 처리나 비동기 프로그래밍에 대한 기초 역량을 쌓는 데 도움이 되었습니다.
