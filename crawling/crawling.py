import re
#정규표현식 호출


class Node(object):
    """
    HTML태그 하나를 가지는 클래스
        내부에 다른 클래스를 가질수도 있음
        가장 큰 범위는 <html></html>
    """
    _pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'

    # .*?은 (.)은 문자 1개를 의미 (*)은 0회이상 최대 문자 ?다음에 오는 문자는 >이므로
    # {tag}다음에 오는 문자의수가 최대일때 ?> '>'전에 멈춰라라는 뜻
    # \s* : 공백문자 최대수 (그룹화) [.(1개의문자)\w(문자)\w(비문자) : 문자열]\s* : 공백문자최대

    _pattern_tag_content = r'<[^!]*?>([.\w\W]*)</.*?>'

    # [^!]은 느낌표를 제외한 문자모두를 의미 ?>은 '>'전까지 문자포함



    def __init__(self, source):
        #초기화 메서드
        self.source = source

    def __str__(self):
        #문자열 메서드
        return '{}\n{}'.format(
            super().__str__(),
            self.source
        )

    def find_tag(self, tag):
        """
        주어진 tag 문자열, 또는 문자열의 리스트 반환
        :param tag: 검색을 원하는 태그. ex)'div'
        :param source: 태그를 검색할 전체 문자열
        :return: 검색 결과가 1개일 경우에는 tag문자열로 만든 Node객체, 2개 이상 일 경우에는 tag문자열로 만든 Node의 리스트
        """
        pattern = re.compile(self._pattern_tag_base.format(tag=tag))
        #미리 컴파일 해놓음
        m_list = re.finditer(pattern, self.source)
        #ㅡlist변수를 만들고 finditer함수(반복자로 반환)로 전체 내용에서 패턴을 검사함
        if m_list:
            return_list = [Node(m.group()) for m in m_list]
            # 반환된 리스트가 m_list의 검사한 패턴이 있으면 node클래스에 써있는 정규표현식을 가져와라
            return return_list if len(return_list) > 1 else return_list[0]
            #만약 검색결과가 1개일 경우, tag문자열로 만든 node객체 2개 이상올경우에는 tag문자열로 만든 node의 리스트를 가져와라
        return None

    @property
    def content(self):
        """
        Node인스턴스의 내용을 리턴
        :return: Node(태그)내부의 내용 문자열을 리턴
        """
        pattern = re.compile(self._pattern_tag_content)
        m = re.search(pattern, self.source.strip())
        if m:
            return m.group(1).strip()
            # group(1)을 가져오고 양쪽의 공백을 없애라
        return None

    @property
    def class_(self):
        """
        해당 Node가 가진 class속성의 value를 리턴 (문자열)
        :return: 
        """
        pass


with open('example.html') as f:
    # with 표현식 as 변수 : 파일을 사용한후 구문이 종료되면, 파일을 닫아준다
    html = Node(f.read())

node_div = html.find_tag('div')
#div요소를 포함하고 있는 문자열을 찾고
node_p_list = node_div.find_tag('p')
#p요소를 포함하고 있는 문자열을 찾아라

for node_p in node_p_list:
    print(node_p.content)
    # p요소를 포함하고 있는 node클래스의 객체에서 node_p를 발견하면 출력하라


# pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'
#
#
# def find_tag(tag, source):
#     """
#     주어진 tag 문자열, 또는 문자열의 리스트 반환
#     :param tag: 검색을 원하는 태그. ex)'div'
#     :param source: 태그를 검색할 전체 문자열
#     :return: 검색 결과가 1개일 경우에는 tag문자열, 2개 이상 일 경우에는 tag문자열의 리스트
#     """
#     pattern = re.compile(pattern_tag_base.format(tag=tag))
#     m_list = re.finditer(pattern, source)
#     if m_list:
#         return_list = [m.group() for m in m_list]
#         return return_list if len(return_list) > 1 else return_list[0]
#     return None
#
#
# # pattern_tag_content = r'^<.*?>([.\w\W]*?)</.*?>$'
# pattern_tag_content = r'<.*?>([.\w\W]*)</.*?>'
#
#
# def get_tag_content(tag_string):
#     """
#     tag 문자열이 주어졌을 때, 해당 tag의 내용을 리턴
#     :param tag_string: <tag>내용</tag>형태의 문자열
#     :return: 위 형태에서 '내용'부분
#     """
#     pattern = re.compile(pattern_tag_content)
#     m = re.search(pattern, tag_string.strip())
#     if m:
#         return m.group(1)
#     return None
#
#
# # html문자열 변수에서 'div'태그의 내용을 찾아 반환하는 함수 실행
# div = find_tag('div', html)
# p_list = find_tag('p', div)
# print(p_list)
# for p in p_list:
#     print(get_tag_content(p))
#
#
# # 원리
# pattern_div = re.compile(r'<div.*?>([.\w\W]*?)</div>')
# m = re.search(pattern_div, html)
# div = m.group(1)
#
# pattern_p = re.compile(r'<p.*?>([.\w\W]*?)</p>')
# m_list = re.finditer(pattern_p, div)