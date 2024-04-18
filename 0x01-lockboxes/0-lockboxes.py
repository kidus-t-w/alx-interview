#!/usr/bin/python3
"""0-lockboxes """


def look_next_opened_box(opened_boxes):
    """
    Returns:
        list: List with the keys contained in the box
    Args:
        opened_boxes (dict): Dictionary which contains boxes opened
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(box):
    """
    Returns:
        bool: True if all boxes can be opened, otherwise False
    Args:
        boxes (list): List which contain all the boxes with keys
    """
    if len(box) <= 1 or box == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': box[0],
            }
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and aux.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    aux[key] = {
                        'status': 'opened',
                        'keys': box[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(box):
            break
        else:
            return False

    return len(aux) == len(box)


def main():
    """Entry """
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
