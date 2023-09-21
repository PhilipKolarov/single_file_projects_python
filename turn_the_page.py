def turn_the_page(total_pages, current_page, turn):
    if current_page + turn > total_pages:
        return f'No pages after {total_pages}!'
    elif current_page + turn < 1:
        return 'Cannot go back before first page!'
    else:
        new_page = current_page + turn
        return new_page


print(turn_the_page(277, 102, 50))
print(turn_the_page(230, 204, 100))
print(turn_the_page(439, 30, -55))
print(turn_the_page(561, 475, -392))
