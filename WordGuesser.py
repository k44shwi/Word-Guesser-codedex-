import streamlit as st
import random

word_bank = [
    'smile', 'nice', 'sunshine', 'rainbows', 'rizz',
    'happy', 'laugh', 'friend', 'kind', 'brave',
    'dream', 'magic', 'sparkle', 'flower', 'ocean',
    'forest', 'cloud', 'storm', 'thunder', 'breeze',
    'summer', 'winter', 'autumn', 'spring', 'holiday',
    'music', 'dance', 'movie', 'pizza', 'chocolate',
    'cookie', 'panda', 'tiger', 'dolphin', 'penguin',
    'rocket', 'planet', 'galaxy', 'castle', 'dragon',
    'wizard', 'pirate', 'treasure', 'mystery', 'secret',
    'adventure', 'victory', 'legend', 'energy', 'vibes',
    'selfie', 'crush', 'savage', 'slay', 'goat'
]

if 'word' not in st.session_state:
    st.session_state.word = random.choice(word_bank)
    st.session_state.guessedWord = ['_'] * len(st.session_state.word)
    st.session_state.attempts = 10

#one of these words will be selected randomly
#the random.choice method is used to randomly select a word
#to not reveal the letters, we use underscores as placeholders for each letter


#gameloop:
st.write(
    'Current Word: ' + ' '.join(st.session_state.guessedWord)
)
st.write('\nCurrent Word: ' + ''.join(st.session_state.guessedWord))
    #the statement is printed on a new line via \n and joins the strings in guessedWord together with spaces

guess = st.text_input(
    'Guess a letter:',
    max_chars=1
).lower()

submit = st.button('Submit Guess')

if submit:
    if not guess:
        st.warning('Please enter a letter.')

    elif guess in st.session_state.word:
        for i in range(len(st.session_state.word)):
            if st.session_state.word[i] == guess:
                st.session_state.guessedWord[i] = guess

        st.success('Great guess!')

    else:
        st.session_state.attempts -= 1
        st.error(
            'Wrong guess! Attempts left: '
            + str(st.session_state.attempts)
        ) 

if '_' not in st.session_state.guessedWord:
    st.success(
        'Congratulations! You guessed the word: '
        + st.session_state.word
    )

elif st.session_state.attempts == 0:
    st.error(
        "You've run out of attempts! The word was: "
        + st.session_state.word
    )
