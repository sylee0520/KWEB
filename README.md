# 2021 KWEB 준회원 과정 면제과제

2021 KWEB 준회원 스터디 과정 면제과제 어플리케이션의 구조에 관한 설명입니다.

## 소개
Full-stack Framework인 django를 이용하여 만들었습니다.

## 디렉토리 구조 설명
디렉토리 최상위에 django 프로젝트 폴더 KWEB이 있고, 그 아래에 어플리케이션 KWEB 폴더와 KWEB211 폴더가 위치하여 있습니다. KWEB 폴더에 위치한 settings.py에서는 프로젝트의 설정을 다룰 수 있으며, urls.py에서는 프로젝트의 라우팅이 올바르게 이뤄질 수 있도록 url들을 설정할 수 있습니다.

대부분의 작업은 KWEB211 폴더에서 진행되었습니다. 우선 admin.py에서는 관리자 페이지를 구성할 수 있으며, forms.py에서는 front-end에서 보이는 디자인을 모듈화 할 수 있습니다. models.py에서는 어플리케이션에 연동되는 데이터베이스 구조를 설계하고 적용할 수 있습니다. urls.py에서는 KWEB211 어플리케이션에서의 라우팅을 담당합니다. 마지막으로 views.py에서는 화면에 보이는 페이지를 구성할 수 있습니다.

## urls.py에 대해
이 파일에서는 라우팅 주소와 views.py내부에 작성된 page 화면을 구성하는 다양한 function들을 연결해줍니다. lecturewrite와 lectureread의 경우 주소 뒤에, 해당 강의의 고유 id값이 이어집니다.

## views.py에 대해

앞서 언급한 바와 같이 views.py에서는 화면에 보이는 페이지를 구성할 수 있습니다. 지금부터는 views.py에 작성된 페이지들을 소개하고자 합니다.

### index page
사이트에 접속하면 최초로 만나게 되는 화면입니다. 로그인이 되어있을 시, 다양한 기능을 사용할 수 있도록, 하이퍼링크를 표시하였고, 그렇지 않다면 로그인과 회원가입 하이퍼링크를 표시하여 다양한 기능을 이용하기 전에 사용자가 먼저 인증을 받도록 하였습니다.

### login & logout page
다양한 기능을 이용하기 위해 인증을 받도록 하는 login page 입니다. 회원가입 시 입력했던 아이디와 비밀번호를 입력하도록 하였고, 회원가입이 안되어 있거나, 아이디와 비밀번호가 틀렸을 경우에 에러메시지를 플래시 메세지를 이용하여 표시하도록 하였습니다. login에 성공한 경우에는 쿠키를 이용하여 사용자가 라우팅을 진행하더라도 로그인을 유지하도록 한 뒤, index page로 redirect를 수행시키도록 하였습니다. 아직 회원가입이 안된 사용자를 위해 회원가입 페이지로 가는 링크 또한 표시하였습니다.

이미 로그인 한 상태라면 화면에 로그인 대신 로그아웃이 표시되도록 하였고, 클릭할 시 로그아웃이 이뤄지면서 index page로 redirect를 진행합니다.

### signup page
회원가입을 수행하는 페이지 입니다. 명세조건에 따라, 아이디, 비밀번호, 비밀번호 확인, 이름, 학번 (혹은 교번), 학생/교수자 여부, 이메일을 회원가입 시 입력으로 받도록 하였습니다. 입력 받은 정보는 데이터베이스에 저장하여, 로그인 과정 시에 이용하도록 하였습니다. 이때, 비밀번호는 SHA256 방식을 통해 암호화 하여 저장하였습니다.

이미 데이터베이스에 입력받은 아이디가 존재하거나 비밀번호가 10자 미만으로 구성되었거나, 비밀번호와 비밀번호 확인이 서로 다를 경우에 에러메시지를 플래시 메시지로 표시하고, 회원가입 페이지로 redirect를 진행하도록 하였습니다.

최종적으로 모든 회원가입이 성공적으로 이뤄 진다면, index page로 redirect를 진행 합니다.

### lecturelist page
데이터베이스에 저장된 사용자 정보를 바탕으로 사용자가 현재 수강중이거나 이전에 수강했던 과목들을 표시하는 강의목록 페이지 입니다. 

학생 혹은 교수자가 강의를 수강하거나 수업하고 있는 정보를 담고있는 Takes 테이블에서 사용자의 id 값으로 지금까지 수강/교습 한 모든 강의들을 filtering 합니다. 그 후 datetime 모듈로 현재 시간을 가져오고 현재 시간이 강의가 진행되는 시간보다 이후라면 과거에 수강했던 강의로 판단하여 list에 저장하고 그렇지 않다면 현재 수강중인 강의 list에 저장합니다. 그 후, 화면에 이를 나누어 표시합니다. 강의마다 과목 이름, 교수자 이름, 수강 학기를 표시하도록 하였습니다.

### lectureread page
각 강의의 게시물을 표시하는 페이지 입니다. 데이터베이스에 들어있는 lecture의 고유 id값으로 라우팅을 진행하였습니다. (ex. /KWEB211/lectureread/1) 

우선 강의의 id값으로 강의의 게시물이 저장된 데이터베이스의 LecturePost 테이블에서 filtering을 진행합니다. 이후, 얻어진 게시물들을 시간을 기준으로 내림차순 하여, 가장 최신 게시물이 화면 가장 위로 배치되도록 하였습니다. 게시물에는 제목과 내용 그리고 작성 시간 정보가 담겨있습니다.

사용자의 신분이 교수자인 경우, 강의 게시물을 작성할 수 있는, lecturewrite page로 이동하는 링크를 표시되도록 하였습니다.

### lecturewrite page
사용자가 교수자인 경우, 강의의 게시물을 작성할 수 있는 페이지 입니다. 해당 페이지는 라우팅 될 때, 맨 뒤에 해당 과목의 고유 id값으로 라우팅 됩니다. (ex. /KWEB211/lecturewrite/1) 크게 title과 contents로 구성되어 있으며, contents를 입력하는 field는 ckeditor를 활용하여 rich text 형식으로 구성하였습니다. 모두 입력 받은 뒤, '작성하기' 버튼을 누르면, 데이터베이스의 LecturePost 테이블에 최초 생성 일자와 함께 담기게 되며 index page로 redirect하게 됩니다.

### update page
수강중인 강의의 최근 올라온 게시물을 확인할 수 있는 페이지 입니다. (블랙보드의 활동 스트림) 우선 사용자가 수강/교습 중인 모든 강의의 고유 id 값을 list 형태로 저장합니다. 이때 반복문을 돌면서 해당 id값에 해당하는 강의의 게시물의 고유 id값을 저장합니다. 시간 순서와 관계 없이 뒤섞인 강의 게시물 들을, 최초 생성 일자를 기준으로 내림차순하여, 가장 최근에 작성한 게시물이 화면 가장 위에 표시되도록 하였습니다.

### profile page
로그인 한 사용자가 본인의 프로필을 볼 수 있는 페이지 입니다. 로그인 한 상태라면, request.user 값에 사용자의 username (로그인 할 때 사용하는 아이디) 가 담기게 되고, 이를 이용해 Account 테이블에 존재하는 해당 사용자의 정보를 filtering 합니다. 그 후, 화면에 표시합니다. 필요 시 프로필 수정이 이뤄질 수 있도록 프로필을 수정하는 페이지인 profilechange page로 이동하는 링크를 표시했습니다.

### profilechange page
사용자가 본인의 프로필을 수정할 수 있는 페이지 입니다. 비밀번호를 제외한 사용자의 모든 정보를 바꿀 수 있도록 하였습니다. 이때 수정하고자 하는 아이디나 학번이 이미 데이터베이스 상에 존재한다면, 에러 메시지를 플래시 메시지로 표시하고 profilechange page로 redirect를 진행했습니다. 이러한 경우에 해당하지 않을 경우에는, 데이터베이스에 해당 사항을 변경하고 저장하도록 한 후 index page로 redirect 했습니다.

## static files & templates
정적파일을 모아두는 static 디렉토리에는 lecturepost를 작성하는데 사용되는 rich text 작성 editor, ckeditor 파일이 위치해 있고, KWEB211 디렉토리에는 application의 전체 디자인을 담당하는 style.css 가 있습니다.

templates 디렉토리의 하위 디렉토리 KWEB211에는 views.py에 작성한 page를 구성하는 function 과 연결되는 html 파일들이 위치해 있습니다.

## 데이터베이스 구조 설명
본 application의 데이터베이스는 총 5개의 테이블로 구성되어 있습니다. 인증과 관리자 여부를 담당하는 User 테이블, 회원 정보가 담긴 Account 테이블, 각 강의의 정보가 담긴 Lecture 테이블, 각 강의의 게시물 정보가 담긴 LecturePost 테이블, 마지막으로 어떤 강의를 수강/교습 하고 있는 지에 대한 정보가 담긴 Takes 테이블이 바로 그것입니다. 기본적으로 모든 테이블은 id 라고 하는 column이 자동적으로 추가되어 있으며, primary key로 지정되어 있습니다.

### User
Django 내에서 자체적으로 지원하는 테이블 입니다. 필수 column으로 username과 password가 있고 필요에 따라, 관리자 여부, 이메일 등을 추가할 수 있습니다.

관리자 1명, 학생 3명, 교수자 9명의 username, password 데이터가 담겨 있습니다. 

### Account
회원 정보가 담겨있는 테이블입니다. 아이디에 해당하는 username, 비밀번호에 해당하는 password, 이름에 해당하는 nickname, 학번/교번에 해당하는 studentId, 학생/교수자 여부에 해당하는 position, 이메일에 해당하는 email column들로 구성되어 있으며, email은 email field로, 나머지는 모두 charfield로 지정되어 있습니다. User 테이블의 username과 이 테이블의 username에 담긴 데이터는 완벽하게 일치합니다.

미리 담겨져 있는 데이터는 User 테이블과 같이 관리자 1명, 학생 3명, 교수자 9명의 회원정보 데이터가 담겨 있습니다. (ex. staryunleegh, 암호화된 비밀번호, 이성윤, 2020320001, student, staryunleegh@xxx.xxxx)

### Lecture
강의 정보가 담겨있는 테이블입니다. 강의 이름인 lecturename, 교수자의 이름인 professor, 해당 강의가 진행되는 연도 year, 진행되는 학기인 semester column들로 구성되어 있습니다. 모두 charfield로 이뤄져 있습니다.

미리 담겨져 있는 데이터로는, 제가 이번학기에 수강중인 모든 강의, 그리고 저번 학기에 수강했던 강의의 일부 데이터가 담겨있습니다. (ex. (논리설계, 이xx, 2021, 1), (글쓰기, 황xx, 2020, 2))

### LecturePost
강의의 게시물 정보가 담겨있는 테이블 입니다. lecture_id는 강의의 정보가 담긴 테이블인 Lecture와 foreignkey로 연결되어, Lecture 테이블의 id값이 할당되어 저장된다. title은 게시물 제목을 저장하며 charfield로 이뤄져있다. content는 richtext로 작성되어 upload되어야 하므로, richtextuploadfield로 지정됩니다. created_at은 최초 생성 일자를, updated_at에는 최근 업데이트 일자를 저장합니다. datetimefield로 지정되었으며, auto_now 조건을 True로 설정하여, 직접 입력하지 않고도 자동적으로 저장되도록 하였습니다.

현재 몇 가지 강의에 대한 게시물이 작성되어 있는 상태입니다. 

### Takes
사용자가 어떤 강의를 수강 또는 교습하고 있는 지에 대한 정보가 담긴 테이블 입니다. lecture_id는 Lecture 테이블과 foreignkey로 연결되어 있으며, Lecture 테이블의 primary key인 id 값이 할당됩니다.
마찬가지로 user_id는 user 테이블과 foreignkey로 연결되어 있으며, id 값이 할당됩니다. 각각 강의와 사용자의 정보가 담기게 됩니다.

현재 일부 학생과 일부 교수자들의 강의 수강/교습 여부가 담겨 있습니다.

## Data in Database
⚠️명시된 이름은 (들어본 이름일 수 있지만) 모두 허구의 인물입니다.

### User Table
|사용자이름|비밀번호|
|:---:|:---:|
murlocking|KF4b27**************************************
staryunlee|Jy+4m2**************************************
staryunleegh|scLZTK**************************************
student111|r/2aqt**************************************
teacher1|ZCnK5S**************************************
teacher2|2u9xEW**************************************
teacher3|GjWpxP**************************************
teacher4|Lh1F4m**************************************
teacher5|88SgiW**************************************
teacher6|3Vb4JD**************************************
teacher7|+IYiPL**************************************
teacher8|8V/0jL**************************************
teacher9|wSp2pZ**************************************

### Account Table
|아이디|비밀번호|이름|학번|교수자/학생|이메일|
|:---:|:---:|:---:|:---:|:---:|:---:|
staryunleegh|fb661f78e8531b31bfe46e62f9bed5d218d3a97366c38f3700ef8ca2bb74bd76|이성윤|2020320001|student|staryunleegh@naver.com
staryunlee|e0b64cf8175a0d229b481bba1533ca6113b92c3c622b13ed0dfdbae7a3a98a7a|이준서|2020320002|professor|staryunlee@naver.com
teacher1|8d72f2e19a06258861169683f843c913822011a8d2d463afbffdfed7b58b52c1|이숙윤|2020329001|professor|teacher1@naver.com
teacher2|ffd7126f3ff963fa074ad461060092204b835663895a4b8514705b7f892bd3a0|신은경|2020329002|professor|teacher2@naver.com
teacher3|4791da82d8cb1ff111e78cf7136a36ced7e142b7889c1cda1221557c67604142|이도길|2020329003|professor|teacher3@naver.com
teacher4|6b8fdf565cd2516497d767340d988db1f2cdf851d96fe7de496fd6ae423d9dc0|김정현|2020329004|professor|teacher4@naver.com
teacher5|9fc2328c0f353582f79a550290ee1edbc24cd66fa2adf4b6d35011a0323c5e90|김현우|2020329005|professor|teacher5@naver.com
teacher6|cc612e5922534d98cca5e5efb8e7e47ba60bc54998958f372b932e88d2632cf2|오형엽|2020329006|professor|teacher6@naver.com
teacher7|02cebc49fedd8a03a2f4bfa9842c2e5a6dff588f354ed4e020e307cd5385d35e|구건재|2020329007|professor|teacher7@naver.com
teacher8|998f04ad255d1dcc3109d576ffca45c452bc9e7ef5538ed11b29ec6e96d9825f|황정현|2020329008|professor|teacher8@naver.com
teacher9|4d98c431ff3978e5b38796151623435c436674952ef2e72e4b908da16ffe6eb4|김현철|2020329009|professor|teacher9@naver.com
student111|feb5edce5782328f1ea520f56943e0a24b9c2a49dfffbb0b9b53abbf8f6d15e9|minju|2020320083|student|student111@korea.ac.kr

### Lectures Table

강의이름|교수자|연도|학기
|:---:|:---:|:---:|:---:|
논리설계|이숙윤|2021|1
데이터과학과인공지능|신은경|2021|1
알고리즘|이도길|2021|1
이산수학|김정현|2021|1
인공지능|김현우|2021|1
한국의젊은시인들|오형엽|2021|1
1학년세미나2|구건재|2020|2
글쓰기|황정현|2020|2
데이터로표현하는세상|김현철|2020|2

### LecturePosts Table
강의 ID|제목|내용
|:---:|:---:|:---:|
1|중간고사 공지|중간고사는 4/28일에 봅니다. 온라인/오픈북 시험으로 진행됩니다.
2|중간고사 공지|중간고사는 4/21일에 봅니다. 오프라인 시험으로 진행됩니다.
3|중간고사 공지|중간고사는 4/23일에 봅니다. 어렵습니다 공부 제대로 하세요
3|과제3 공지|이번 과제는 convexhull을 divide-and-conquer 방식으로 풀어내는 과제 입니다 5/3일까지 제출하세요.
4|Quiz3 Announcement|Quiz3은 ch7,8에 해당하는 내용으로 봅니다. 공부 열심히 하세요. 저번 퀴즈 성적 조금 실망스럽습니다
1|과제2 공지|과제2는 실습 키트를 가지고 진행합니다. 자세한 사항은 다음주 수업 때, 공지하겠습니다.
1|과제3 키트 관련 공지|키트 받아 가세요
1|키트 사용법 공지|키트 사용법은 유튜브 검색하세요~
1|과제 4 공지|열심히 하세요~
2|파이썬 실습 공지|파이썬 실습을 다음주 부터 진행합니다.
3|과제 4 공지|대망의 마지막 과제!는 아닙니다. 이번 학기는 총 5개의 과제가 나갈 예정입니다. 참고하세요. 아 그냥 참고 하라고요.
1|마지막 과제 공지|알아서 하세요~
1|테스트 입니다|테스트 입니다! 테스트 입니다!테스트 입니다! 테스트 입니다!테스트 입니다!테스트 입니다!
1|테스트 2 입니다|**테스트 입니다.** **_테스트 입니다._** **_테스트 입니다,_** **_테스트 입니다,_**
1|테스트3입니다|테스트 3 입니다 _테스트 3입니다_
1|종강공지|방학입니당~

### Takes Table
강의 ID|사용자 ID
|:---:|:---:|
1|11
2|11
3|11
4|11
5|11
6|11
7|11
8|11
9|11
1|13
2|14
3|15
4|16
5|17
6|18
7|19
8|20
9|21

## Database Check
데이터 베이스에 있는 데이터를 확인해보고 싶으시다면 아래 계정으로 로그인 하세요.

학생 데이터
|아이디|비밀번호|
|:---:|:---:|
staryunleegh|5020leegh@

교수자 데이터
|아이디|비밀번호|
|:---:|:---:|
teacher1|teacher111
