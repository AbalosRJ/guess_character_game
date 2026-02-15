import streamlit as st

st.set_page_config(page_title="Guess The Character!", page_icon="🎭", layout="centered")

# =====================================================
# GAME DATA (25 CHARACTERS TOTAL)
# =====================================================

game_data = {

    "Easy": [

        {
            "name": "Harry Potter",
            "image": "images/harry_potter.png",
            "clues": [
                "I have a lightning-shaped scar.",
                "I can speak Parseltongue.",
                "I studied at Hogwarts.",
                "My best friends are Ron and Hermione.",
                "I am known as 'The Boy Who Lived.'"
            ]
        },

        {
            "name": "Spider-Man",
            "image": "images/spiderman.png",
            "clues": [
                "I gained powers after being bitten.",
                "I can stick to walls.",
                "I use webs to travel.",
                "My real name is Peter Parker.",
                "I live in New York."
            ]
        },

        {
            "name": "Batman",
            "image": "images/batman.png",
            "clues": [
                "I fight crime at night.",
                "I don't have superpowers.",
                "My city is Gotham.",
                "My butler is Alfred.",
                "My real name is Bruce Wayne."
            ]
        },

        {
            "name": "Elsa",
            "image": "images/elsa.png",
            "clues": [
                "I have ice powers.",
                "I built an ice palace.",
                "My sister is Anna.",
                "I am a queen.",
                "I sang 'Let It Go.'"
            ]
        },

        {
            "name": "Pikachu",
            "image": "images/pikachu.png",
            "clues": [
                "I am small and yellow.",
                "I produce electricity.",
                "I say my own name.",
                "My trainer is Ash.",
                "I am a Pokémon."
            ]
        },

        {
            "name": "Superman",
            "image": "images/superman.png",
            "clues": [
                "I wear a red cape.",
                "I can fly.",
                "I am weak to Kryptonite.",
                "I work as a reporter.",
                "My real name is Clark Kent."
            ]
        },

        {
            "name": "Simba",
            "image": "images/simba.png",
            "clues": [
                "I am a lion.",
                "My father was a king.",
                "I was raised by Timon and Pumbaa.",
                "My uncle is Scar.",
                "I became king of the Pride Lands."
            ]
        },

        {
            "name": "SpongeBob SquarePants",
            "image": "images/spongebob.png",
            "clues": [
                "I live in a pineapple.",
                "I work at the Krusty Krab.",
                "My best friend is Patrick.",
                "I live in Bikini Bottom.",
                "I am a yellow sea sponge."
            ]
        },

        {
            "name": "Wonder Woman",
            "image": "images/wonder_woman.png",
            "clues": [
                "I am an Amazon warrior.",
                "I use a lasso.",
                "I come from Themyscira.",
                "My real name is Diana.",
                "I am part of the Justice League."
            ]
        },

        {
            "name": "Mickey Mouse",
            "image": "images/mickey.png",
            "clues": [
                "I wear red shorts.",
                "I have big round ears.",
                "My girlfriend is Minnie.",
                "I am Disney's mascot.",
                "I am a famous cartoon mouse."
            ]
        },
    ],

    "Medium": [

        {
            "name": "Katniss Everdeen",
            "image": "images/katniss.png",
            "clues": [
                "I volunteer as tribute.",
                "I am skilled with a bow.",
                "I come from District 12.",
                "I fought in a televised competition.",
                "I am called the Girl on Fire."
            ]
        },

        {
            "name": "Tony Stark",
            "image": "images/tony_stark.png",
            "clues": [
                "I am a billionaire genius.",
                "I build advanced technology.",
                "I wear a powerful suit.",
                "I love witty one-liners.",
                "I am Iron Man."
            ]
        },

        {
            "name": "Loki",
            "image": "images/loki.png",
            "clues": [
                "I love chaos.",
                "I can shape-shift.",
                "I am adopted.",
                "I am Thor's brother.",
                "I am the God of Mischief."
            ]
        },

        {
            "name": "The Flash",
            "image": "images/flash.png",
            "clues": [
                "I move extremely fast.",
                "I was struck by lightning.",
                "I can time travel.",
                "My name is Barry Allen.",
                "I am the fastest man alive."
            ]
        },

        {
            "name": "Neo",
            "image": "images/neo.png",
            "clues": [
                "My world is a simulation.",
                "I can dodge bullets.",
                "I wear black trench coats.",
                "Morpheus believes in me.",
                "I am 'The One.'"
            ]
        },

        {
            "name": "Deadpool",
            "image": "images/deadpool.png",
            "clues": [
                "I break the fourth wall.",
                "I heal very fast.",
                "I wear red and black.",
                "I am very sarcastic.",
                "My real name is Wade Wilson."
            ]
        },

        {
            "name": "Wednesday Addams",
            "image": "images/wednesday.png",
            "clues": [
                "I rarely smile.",
                "I love dark humor.",
                "My best friend is Thing.",
                "I attend Nevermore Academy.",
                "I am part of the Addams Family."
            ]
        },

        {
            "name": "Legolas",
            "image": "images/legolas.png",
            "clues": [
                "I am an elf.",
                "I am skilled with a bow.",
                "I have incredible eyesight.",
                "I am friends with Gimli.",
                "I fight in the War of the Ring."
            ]
        },

        {
            "name": "Dracula",
            "image": "images/dracula.png",
            "clues": [
                "I sleep during the day.",
                "I drink blood.",
                "I can turn into a bat.",
                "I live in a castle.",
                "I am a famous vampire."
            ]
        },

        {
            "name": "Daenerys Targaryen",
            "image": "images/daenerys.png",
            "clues": [
                "I am linked to dragons.",
                "I was exiled.",
                "I am called Mother of Dragons.",
                "I seek the Iron Throne.",
                "I am from House Targaryen."
            ]
        },
    ],

    "Hard": [

        {
            "name": "Geralt of Rivia",
            "image": "images/geralt.png",
            "clues": [
                "I hunt monsters.",
                "My hair is white.",
                "I carry two swords.",
                "I am a Witcher.",
                "Hmm..."
            ]
        },

        {
            "name": "Severus Snape",
            "image": "images/snape.png",
            "clues": [
                "I teach Potions.",
                "I have black hair.",
                "I say 'Always.'",
                "I once served Voldemort.",
                "I loved Lily."
            ]
        },

        {
            "name": "Eleven",
            "image": "images/eleven.png",
            "clues": [
                "I have psychic powers.",
                "I escaped from a lab.",
                "I love Eggo waffles.",
                "My nose bleeds when I use powers.",
                "I am from Stranger Things."
            ]
        },

        {
            "name": "Thranduil",
            "image": "images/thranduil.png",
            "clues": [
                "I am an elven king.",
                "I rule the Woodland Realm.",
                "I am Legolas' father.",
                "I appear in The Hobbit.",
                "I value my kingdom deeply."
            ]
        },

        {
            "name": "Buzz Lightyear",
            "image": "images/buzz.png",
            "clues": [
                "I believe I am a space ranger.",
                "I say 'To infinity and beyond!'",
                "I wear white and green.",
                "I am a toy.",
                "I am from Toy Story."
            ]
        }
    ]
}

# =====================================================
# SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "title"

if "level" not in st.session_state:
    st.session_state.level = None

if "character_index" not in st.session_state:
    st.session_state.character_index = 0

if "clue_index" not in st.session_state:
    st.session_state.clue_index = 0

# =====================================================
# TITLE PAGE
# =====================================================

if st.session_state.page == "title":
    st.title("🎭 GUESS THE CHARACTER!")
    st.subheader("Interactive Team Challenge")
    if st.button("Start Game"):
        st.session_state.page = "mechanics"
        st.rerun()

# =====================================================
# MECHANICS
# =====================================================

elif st.session_state.page == "mechanics":
    st.title("📜 Mechanics")
    st.markdown("""
    - Each character has 5 clues.
    - Press 🔴 if wrong.
    - Press 🟢 if correct.
    - Game continues until all characters are guessed.
    """)
    if st.button("Select Level"):
        st.session_state.page = "level"
        st.rerun()

# =====================================================
# LEVEL
# =====================================================

elif st.session_state.page == "level":
    st.title("🎯 Choose Difficulty")

    if st.button("🟢 Easy"):
        st.session_state.level = "Easy"
        st.session_state.page = "game"
        st.session_state.character_index = 0
        st.session_state.clue_index = 0
        st.rerun()

    if st.button("🟡 Medium"):
        st.session_state.level = "Medium"
        st.session_state.page = "game"
        st.session_state.character_index = 0
        st.session_state.clue_index = 0
        st.rerun()

    if st.button("🔴 Hard"):
        st.session_state.level = "Hard"
        st.session_state.page = "game"
        st.session_state.character_index = 0
        st.session_state.clue_index = 0
        st.rerun()

# =====================================================
# GAME LOOP
# =====================================================

elif st.session_state.page == "game":

    level = st.session_state.level
    characters = game_data[level]

    if st.session_state.character_index >= len(characters):
        st.session_state.page = "end"
        st.rerun()

    character = characters[st.session_state.character_index]
    clue = character["clues"][st.session_state.clue_index]

    st.title(f"🎮 Level: {level}")
    st.subheader("🔍 Clue:")
    st.write(clue)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔴 Wrong"):
            if st.session_state.clue_index < 4:
                st.session_state.clue_index += 1
            else:
                st.session_state.page = "reveal"
            st.rerun()

    with col2:
        if st.button("🟢 Correct"):
            st.session_state.page = "reveal"
            st.rerun()

# =====================================================
# REVEAL
# =====================================================

elif st.session_state.page == "reveal":

    character = game_data[st.session_state.level][st.session_state.character_index]

    st.balloons()
    st.success("🎉 CORRECT! 🎉")
    st.header(character["name"])

    st.image(character["image"])  # Put your image files in /images folder

    if st.button("Next Character ➡"):
        st.session_state.character_index += 1
        st.session_state.clue_index = 0
        st.session_state.page = "game"
        st.rerun()

# =====================================================
# END
# =====================================================

elif st.session_state.page == "end":
    st.title("🏆 Congratulations!")
    st.balloons()
    st.markdown("## 🎉 Amazing job Team Cabia! 🎉")
    st.markdown("Thank you for participating in Guess The Character!")

    if st.button("Play Again"):
        st.session_state.page = "title"
        st.session_state.character_index = 0
        st.session_state.clue_index = 0
        st.rerun()
