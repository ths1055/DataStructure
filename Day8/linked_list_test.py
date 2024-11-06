from enum import Enum
from linked_list import LinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제','꼬리노드삭제','주목노드출력','주목노드이동','주목노드삭제','모든노드삭제','검색','멤버십판단','모든노드출력','스캔','종료'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = LinkedList()

while True:
    menu = select_Menu()

    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))
    
    elif menu == Menu.머리노드삭제:
        lst.remove_first()
    
    elif menu == Menu.꼬리노드삭제:
        lst.remove_last()
    
    elif menu == Menu.주목노드출력:
        lst.print_current_node()

    elif menu == Menu.주목노드이동:
        lst.next()
    
    elif menu == Menu.주목노드삭제:
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:
        lst.clear()

    elif menu == Menu.검색:
        pos = lst.search(int(input('검색할 갑승ㄹ 입력하세요ㅕ.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당하는 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:
        print('그 값의 데이터는 포함되어' + (' 있습니다.'if int(input('판단할 값을 입력하세요.: ')) in lst else '있지 않습니다.'))

    elif menu == Menu.모든노드출력:
        lst.print()

    elif menu == menu.스캔:
        for e in list:
            print(e)
    

    else:
        break