def sorter(invitation_list: str):
    arr = invitation_list.upper().split(';')
    split = []
    for name in arr:
        pair = name.split(':')
        name = pair[0]
        surname = pair[1]
        split.append(f'({surname}, {name})')
    split.sort()
    result = ''.join(split)
    return result