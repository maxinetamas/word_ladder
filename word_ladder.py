#!/bin/python3
from collections import deque

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    stack = []
    stack.push(start_word)
    queue = deque([])
    queue = deque([stack])

    while len(queue) != 0:
        while queue:
            curr_stack = queue.popleft()
            curr_word = curr_stack[-1]
            for i in range(len(curr_word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    new_word = curr_word[:i] + j + curr_word[i + 1:]
                    if new_word == end_word:
                        return curr_stack + [new_word]
                    stack_copy = curr_stack + [new_word]
                    queue.append(stack_copy)

    if start_word == end_word:
        return [start_word]

    return []


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    for i in enumerate(ladder):
        if adjacent(enumerate[i], enumerate[i + 1]) == False:
            return False
    return True 


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    count = 0
    if len(word1) == len(word2):
        for i in enumerate(word1):
            if word1[i] != word2[i]:
                count += 1
    if count == 1:
        return False
    return True
