import os

import requests
from bs4 import BeautifulSoup


class NaverWebtoonCrawler:

    #초기화메서드에 넣지 않는 것은 바뀌지 않을 값이다.
    _url_detail_base = 'http://comic.naver.com/webtoon/detail.nhn?' \
                        #네이버 웹툰 메인 페이지
                       'titleId={webtoon_id}&' \
                        #어떤 웹툰 전체 페이지
                       'no={episode_num}&' \
                        # no = 58은 58화의 넘버
                       'weekday=wed'
                        #수요일웹툰

    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        #webtoon_id : webtoon_id매개변수에 실행인자를 넣은것을 받아 self자기자신.webtoon_id에 넣어준다
        # 즉 자기자신 초기화 메서드를 통해 webtoon_id가 어떤값이 올수 있도록 초기화해준다.
        #초기화메서드에 넣는 매개변수들은 계속 바뀌는 값이기에
        # self.매개변수 = 매개변수로, 어떤매개변수가 올때마다 self자신의 값이 바뀌도록
        # self.인스턴스이름 = 매개변수로 설정해준다

    def crawl_page(self, page_num):
        return '해당 페이지의 에피소드 리스트'

    def crawl_episode(self, episode_num=None):
        """
        webtoon_id에 해당하는 웹툰의 episode_num화 내부의 이미지를 저장
        :param episode_num: 
        :return: 
        """
        dir_path = '{}/{}'.format(self.webtoon_id, episode_num)
        # 폴더경로는 webtoon_id는 어떤웹툰의 타이틀넘버 , episode_num은 각 화수의 넘버

        def make_episode_dir():
            # 이미지를 저장하기 위한 폴더 생성
            print(dir_path)
            # exists로 이미 생성하려는 폴더가 있는지 검사
            if not os.path.exists(dir_path):
                # os는 지금 돌고있는 클래스의 서버환경 path:환경의 경로 exists는 즉 os.path.exists는 정형화된 패턴
                os.makedirs(dir_path)
                # os.makedirs도 정형화된 패턴
                print('dir created')
            print('dir exist')

            # try~except구문으로 이미 폴더가 존재할경우 예외처리
            # exists로 이미 생성하려는 폴더가 있는지 검사
            try:
                os.makedirs(dir_path)
            except FileExistsError as e:
                print('dir exist, error:', e)

            # exists로 이미 생성하려는 폴더가 있는지 검사
            # exist_ok매개변수 추가
            os.makedirs(dir_path, exist_ok=True)

        def  get_img_tag_list():
            """
            디테일페이지에서 img Tag(bs4)의 리스트를 반환
            :return: 
            """
            # 디테일 페이지의 html을 가져와 img의 href를 출력
            # print(url_detail)
            # requests를 이용해서 url_detail에 get요청을 보냄
            response = requests.get(url_detail)
            # with open('test.html', 'wt') as f:
            #     f.write(response.text)
            # 응답(Response)에서 .text를 이용해 내용을 가져옴
            # 가져온 응답내용을 이용해 BeautifulSoup인스턴스를 생성 (soup)

            soup = BeautifulSoup(response.text, 'lxml')
            # soup인스턴스에서 select_one 메서드를 사용해 웹툰뷰어 태그를 리턴

            div_wt_viewer = soup.select_one('div.wt_viewer')
            # 웹튠뷰어 태그에서 img태그들을 전부 찾아 리스트로 반환
            img_list = div_wt_viewer.find_all('img')
            return img_list

        if not episode_num:
            url_detail = self._url_detail_base.format(
                # self._url_detail_base는 초기화메서드 밖에 있는 것으로 네이버웹툰메인은 바뀔필요가 없다. 그래서
                # 초기화메서드 밖에 써주는것이다. 쓸때는 자신이 자신의 값을 가지므로 self.url_detail_base이다
                self.webtoon_id,
                #format은 문자열을 처리해주는 방식으로 base(인스턴스).format함수안에 self.webtoon_id라는 타이틀명
                #에 해당하는 것을 넣어 실행한다. 즉 url_detail은 기본메인페이지에서 어떤웹툰의 메인페이지까지 불러오는것이다
                '마지막 에피소드 넘버 가져오기'
            )
        else:
            url_detail = self._url_detail_base.format(

            #     _url_detail_base='http://comic.naver.com/webtoon/detail.nhn?' \
            #         # 네이버 웹툰 메인 페이지
            #                      'titleId={webtoon_id}&' \
            #         # 어떤 웹툰 전체 페이지
            #                      'no={episode_num}&' \
            #         # no = 58은 58화의 넘버
            #                      'weekday=wed'
            # 에 중괄호 되어있는 {wetoon_id}하고 {episode_num}이있기에 webtoon_id = self.webtoon_id, episode_num

                webtoon_id=self.webtoon_id,
                episode_num=episode_num
                #어떤 웹툰페이지는 바뀌지만 아직까지는 num은 바꾸지 않았다.
            )

        # 이미지를 다운받을 폴더 생성
        make_episode_dir()

        # 이미지 태그 목록 가져오기
        img_list = get_img_tag_list()

        # 리스트를 순회하며 각 img태그의 src속성을 출력 및 다운로드
        for index, img in enumerate(img_list):
            # 이미지 주소에 get요청
            print(img['src'])
            #tag['속성']이면 속성에 해당하는 내용을 가져와라


            headers = {'Referer': url_detail}
            #네이버에서 관련된 url로 들어오게 만드는것

            response = requests.get(img['src'], headers=headers)
            # requests를


            # 요청 결과 (이미지파일)의 binary데이터를 파일에 쓴다
            img_path = '{}/{:02}.jpg'.format(
                dir_path,
                index
            )
            with open(img_path, 'wb') as f:
                #wb는 이전데이터타입
                f.write(response.content)

        # 해당 에피소드를 볼 수 있는 HTML파일을 생성
        html_path = '{}/{:02}.html'.format(self.webtoon_id,episode_num)

        # 위 경로로 파일을 쓰기모드로 받고 '<html>'을 기록 후 닫기


        with open(html_path,'wt') as f:
            f.write('<html>')
        """
        <html>
            <img src="651673/1/00.jpg">
            <img src="651673/1/01.jpg">
            <img src="651673/1/02.jpg">
            <img src="651673/1/03.jpg">
        </html>
        """
        print('Crawling complete')

    def crawl_all_episodes(self):
        return ''


class NaverWebtoon:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = []

    def get_info(self):
        return '정보 리턴'

    def view_last_episode(self):
        return ''

    def view_episode_list(self, num=1):
        return ''

    def save_webtoon(self, create_html=False):
        if create_html:
            return '다운받은 웹툰을 볼 수 있는 html까지 생성해서 저장'
        return '특정 경로에 웹툰 전체를 다운받아서 저장'


class NaverWebtoonEpisode:
    # url_thumbnail, title, rating, date는 property로 구현 (전부 읽기전용, private으로 선언하지 말 것)
    def __init__(self, url_thumbnail, title, rating, date):
        self._url_thumbnail = url_thumbnail
        self._title = title
        self._rating = rating
        self._date = date

    @property
    def url_thumbnail(self):
        return self._url_thumbnail

    @property
    def title(self):
        return self._title

    @property
    def rating(self):
        return self._rating

    @property
    def date(self):
        return self._date