# Find The Plain // Writeup

## Problem

*== KR == 알파팀의 내부고발자가 팀 내부 기밀자료를 ftp를 이용하여 외부로 내부의 정보를 유출시키는 패킷을 캡쳐하였다.*

*패킷을 분석하여 ftp접속에 사용된 비밀번호와 획득한 정보를 플래그로 제출하라!*

*플래그 형식 : KorNewbie{비밀번호_발견한정보}*

*※ 혹시라도 해시값이 있다면 그것은 md5이다.*

*== EN == Alpha team's whistleblower captured a packet that leaked internal information to the outside using ftp internal confidential data.*

*Analyze the packet and flag the password and information obtained for the ftp connection!*

*flag format : KorNewbie{password_yougetinformation}*

*※ If there is a hash value, it will be md5.*

## Solution

Let's check the file type

Open [vithim.pcapng](https://nctf.vulnerable.kr/files/e9f451a2239ca6d6a4555ae7a3a0c64c/vithim.pcapng?token=eyJ0ZWFtX2lkIjoyMTYsInVzZXJfaWQiOjU1NSwiZmlsZV9pZCI6MTl9.XcNOHg.-o6zY1_kncoKP70PG_KWHBQ91Jw) ( dumped network traffic ) with Wireshark and use filter `ftp`.
