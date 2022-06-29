from sys import stdin

def get_button_input_count(word, dictionary):
    word_len = len(word)
    next_ch_dict = dictionary[word[0]]
    cur_idx = 1
    button_input = 1
    
    while cur_idx < word_len:
        if len(next_ch_dict) > 1:
            button_input += 1
        next_ch_dict = next_ch_dict[word[cur_idx]]
        cur_idx += 1
        
    return button_input

while True:
    dictionary = {}
    words = []
    try:
        n = int(stdin.readline())
    except:
        break
    for _ in range(n):
        word = stdin.readline().rstrip()
        words.append(word)
        next_ch_dict = dictionary
        for ch in word:
            if ch not in next_ch_dict:
                next_ch_dict[ch] = {}
            next_ch_dict = next_ch_dict[ch]
        next_ch_dict['end_of_word'] = True
    button_input = 0
    for word in words:
        button_input += get_button_input_count(word, dictionary)
    print('{:.2f}'.format(button_input/n))