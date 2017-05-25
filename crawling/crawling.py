import re
#정규표현식 호출


class Node(object):
    """
    HTML태그 하나를 가지는 클래스
        내부에 다른 클래스를 가질수도 있음
        가장 큰 범위는 <html></html>
    """


    _pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'
    # 태그안에 있는 내용을 가져오기
    # 이것만 쓰게되면 <p>요소안내용</p>이렇게 되기에, _pattern_tag_content을 통해 p태그안에 있는 내용을 가져와야한다.

    # (.*)/(?>) : (.*)은 문자최대, (?>)은 괄호앞까지 출력
    # [.\w\W]* 은 문자\문자\비문자 다양하게 올 수있는 문자열 형태최대이고, ?\s는 공백문자 앞까지 출력, \s*은 공백문자 최대

    _pattern_tag_content = r'<[^!]*?>([.\w\W]*?)</.*?>'
    # 태그안에 있는 문자열을 가져오기

    # [^!]*은 느낌표를 제외한 문자모두최대(<!doctype html>때문에) ?>은 >앞까지 출력


    _pattern_class_content = r'^\s*<.*?class=([\'"](.*?)[\'"])>'

    #[\'"] : (")이다. : ^\s* 공백문자 시작이며, 최대 <.* : 문자최대,  ?class : class앞까지 출력, [\'"]은 "이고,(.* : 문자최대 ?['"] : ['"]앞까지 출력




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
        
        :return : 검색 결과가 1개일 경우에는 tag문자열로 만든 Node객체, 2개 이상 일 경우에는 tag문자열로 만든 Node의 리스트
        (메모리효율성을 위해서)
        """
        pattern = re.compile(self._pattern_tag_base.format(tag=tag))
        #컴파일 된 패턴객체를 문자열 대신 첫번째 인자로 사용 가능

        m_list = re.finditer(pattern, self.source)

        # m_list변수를 만들고, finditer함수(반복자로 반환)로 전체 내용에서 패턴을 검사함

        if m_list:

            return_list = [Node(m.group()) for m in m_list]

            # 반환된 리스트가 m_list의 검사한 패턴이 있으면 node클래스에 써있는 정규표현식을 가져와라
            # m_list에서 내용과 일치하는 패턴을 m에 일시저장해주고, Node클래스의 속성으로(m.group)을 대입하여 정규표현식을 가져온다.
            # 검사한 패턴들을 그룹화하고 [ 내용 ]으로 리스트화해준다.

            return return_list if len(return_list) > 1 else return_list[0]

            #만약 검색결과가 1개일 경우, tag문자열로 만든 node객체 2개 이상올경우에는 tag문자열로 만든 node의 리스트를 가져와라
            # 반환된 리스트의 길이가 1개라면 tag문자열, 반환된 리스트의 길이가 2개라면, tag문자열로 만든 리스트를 가져와라.

        return None

    @property
    def content(self):
        """
        
        Node인스턴스의 내용을 리턴
        :return : Node(태그)내부의 내용 문자열을 리턴
        
        """

        pattern = re.compile(self._pattern_tag_content)
        #컴파일된 문자열을 인자로 사용가능

        m = re.search(pattern, self.source.strip())
        # 전체내용내에 패턴을 검색
        if m:
            return m.group(1).strip()
            # group(1)을 가져오고 양쪽의 공백을 없애라
        return None

    @property
    def class_(self):
        # 해당 Node가 가진 class 속성의 value 리턴(문자열)
        # : return:


        pattern = re.compile(self._pattern_class_content)
        # 컴파일된 문자열을 인자로 사용가능

        m = re.search(pattern,self.source.strip())
        # 패턴을 검색

        if m:
            return m.group(1).strip()




with open('example.html') as f:

    # with 표현식 as 변수 : 파일을 사용한후 구문이 종료되면, 파일을 닫아준다

    html = Node(f.read())
    #html이라는 변수는 Node클래스의 속성으로 f.read 즉 example.html을 읽겠다.

node_div = html.find_tag('div')

#div요소를 포함하고 있는 문자열을 찾고 node_div라는 변수에 할당

node_p_list = node_div.find_tag('p')
#p요소를 포함하고 있는 문자열을 찾아라




# print(node_p_list)
# for node_p in node_p_list:
#     print(node_p)
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