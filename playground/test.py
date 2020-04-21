import urllib.request
url = "http://agile.egloos.com/archives/"
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
#print(f.read().decode('utf-8'))

links = ['<a href="/5931859">혹독한 조언이 나를 살릴까?</a>',
'<a href="/archives/2020/02/page/1" title="전체보기">"2020년02월" 의 글 내용 전체 보기</a>',
'<a href="/5925195">퍼실리테이터로 살아보기</a>',
'<a href="/archives/2019/09/page/1" title="전체보기">"2019년09월" 의 글 내용 전체 보기</a>']

for link in links:
    print(link.find('title'))
"""
<a href="/5914591">함께 자라기 : 제가 쓴 첫 책이 나왔습니다!</a>
<a href="/archives/2018/12/page/1" title="전체보기">"2018년12월" 의 글 내용 전체 보기</a>
<a href="/5906079">방법론 도입이 실패하는 이유</a>
<a href="/archives/2018/04/page/1" title="전체보기">"2018년04월" 의 글 내용 전체 보기</a>
<a href="/5905451">프로그래밍 어떻게 배우고 어떻게 가르칠까</a>
<a href="/archives/2018/03/page/1" title="전체보기">"2018년03월" 의 글 내용 전체 보기</a>
<a href="/5904205">애자일을 키워드로 배워보자 : 애자일 키워드 팟캐스트</a>
<a href="/5904102">협업의 미신 5가지</a>
<a href="/archives/2018/02/page/1" title="전체보기">"2018년02월" 의 글 내용 전체 보기</a>
<a href="/5892581">하기 싫지만 누군가 해야하는 일</a>
<a href="/archives/2017/07/page/1" title="전체보기">"2017년07월" 의 글 내용 전체 보기</a>
<a href="/5890768">문재인 대통령의 회의 방침</a>
<a href="/archives/2017/05/page/1" title="전체보기">"2017년05월" 의 글 내용 전체 보기</a>
<a href="/5888372">AC2 과정이 어떤 느낌인지 궁금하신가요?</a>
<a href="/archives/2017/04/page/1" title="전체보기">"2017년04월" 의 글 내용 전체 보기</a>
<a href="/5885773">당신이 뻔하다고 생각하는 것</a>
<a href="/archives/2017/03/page/1" title="전체보기">"2017년03월" 의 글 내용 전체 보기</a>
<a href="/5882445">AC2 내년 첫 과정 모집</a>
<a href="/5881049">외적 동기가 내적 동기를 갉아먹는다</a>
<a href="/archives/2016/12/page/1" title="전체보기">"2016년12월" 의 글 내용 전체 보기</a>
<a href="/5880685">Agile과 agile</a>
<a href="/5879231">퍼포먼스 공식</a>
<a href="/archives/2016/11/page/1" title="전체보기">"2016년11월" 의 글 내용 전체 보기</a>]
"""
