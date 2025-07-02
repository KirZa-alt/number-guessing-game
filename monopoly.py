import streamlit as st
import random


tiles = [
    "Start", "Urdu Bazar", "Chance", "Hall Road", "Jamshaid Road",
    "Clock Tower", "Bahria Town", "Jail Road",
    "Satellite Town", "Clifton", "Zoo", "Light House"
]

# --- Property Prices ---
property_prices = {
    "Urdu Bazar": 2000, "Hall Road": 1000, "Jamshaid Road": 1500,
    "Clock Tower": 1000, "Bahria Town": 5000, "Jail Road": 800,
    "Satellite Town": 2500, "Clifton": 3000, "Zoo": 700, "Light House": 900
}

# --- Game Setup ---
if "player_names" not in st.session_state:
    name1 = st.text_input("🎮 Enter name for Player 1", "Player 1")
    name2 = st.text_input("🎮 Enter name for Player 2", "Player 2")
    if st.button("🚀 Start Game"):
        st.session_state.player_names = [name1, name2]
        st.session_state.players = {
            name1: {"pos": 0, "money": 10000, "props": []},
            name2: {"pos": 0, "money": 10000, "props": []}
        }
        st.session_state.turn = name1
        st.session_state.just_rolled = False
        st.rerun()
    st.stop()

# --- Access Session Data ---
names = st.session_state.player_names
players = st.session_state.players
turn = st.session_state.turn
player = players[turn]

# --- Title ---
st.markdown("<h1 style='color:#0099ff;'>🎲 Easy Monopoly Game</h1>", unsafe_allow_html=True)

# --- Function: Tile Display with Color ---
def tile_html(name, players_here):
    bg = "#f9f9f9"  # default

    if name == "Chance":
        bg = "#fff7c0"
    elif name in property_prices:
        bg = "#e0f7fa"
    elif name == "Start":
        bg = "#d4edda"

    player_text = "👤 " + " ".join(players_here) if players_here else "⬜"
    return f"<div style='background:{bg}; padding:10px; border-radius:10px; text-align:center;'>\
            <b>{name}</b><br>{player_text}</div>"

# --- Top Row (0-3) ---
top = st.columns(4)
for i in range(4):
    with top[i]:
        players_here = [n for n, p in players.items() if p["pos"] == i]
        st.markdown(tile_html(tiles[i], players_here), unsafe_allow_html=True)

# --- Middle (Left 11,10 | Center | Right 4,5) ---
mid = st.columns([1, 2, 1])
with mid[0]:
    for i in [11, 10]:
        players_here = [n for n, p in players.items() if p["pos"] == i]
        st.markdown(tile_html(tiles[i], players_here), unsafe_allow_html=True)
with mid[1]:
    st.markdown("<div style='text-align:center; background:#eeeeee; border-radius:10px; padding:20px;'>\
                <h4>🎯 Game Center</h4></div>", unsafe_allow_html=True)
with mid[2]:
    for i in [4, 5]:
        players_here = [n for n, p in players.items() if p["pos"] == i]
        st.markdown(tile_html(tiles[i], players_here), unsafe_allow_html=True)

# --- Bottom Row (9-6) ---
bottom = st.columns(4)
for idx, i in enumerate([9, 8, 7, 6]):
    with bottom[idx]:
        players_here = [n for n, p in players.items() if p["pos"] == i]
        st.markdown(tile_html(tiles[i], players_here), unsafe_allow_html=True)

# --- Player Status ---
tile = tiles[player["pos"]]
st.markdown(f"### 🎮 <span style='color:#0099ff'>{turn}'s Turn</span>", unsafe_allow_html=True)
st.markdown(f"📍 Tile: <b>{tile}</b>", unsafe_allow_html=True)
st.markdown(f"💰 Balance: <span style='color:green'><b>${player['money']}</b></span>", unsafe_allow_html=True)

# --- Dice Roll Logic ---
if "just_rolled" not in st.session_state:
    st.session_state.just_rolled = False

if not st.session_state.just_rolled:
    if st.button("🎲 Roll Dice"):
        roll = random.randint(1, 6)
        st.session_state.last_roll = roll
        st.session_state.just_rolled = True
        st.rerun()
else:
    roll = st.session_state.last_roll
    player["pos"] = (player["pos"] + roll) % len(tiles)
    tile = tiles[player["pos"]]
    st.success(f"🎲 {turn} rolled a {roll} and moved to **{tile}**")

    # --- Chance Card ---
    if tile == "Chance":
        msg, value = random.choice([
            ("🎉 You found money! +$500", +500),
            ("😢 You paid a fine! -$300", -300),
            ("💼 Bonus from job! +$700", +700),
            ("🚗 You lost a bet! -$200", -200)
        ])
        st.info(f"🃏 Chance Card: {msg}")
        player["money"] += value

    # --- Rent Logic ---
    elif tile in property_prices:
        for name, other in players.items():
            if name != turn and tile in other["props"]:
                rent = property_prices[tile] // 2
                player["money"] -= rent
                other["money"] += rent
                st.warning(f"💸 You paid ${rent} rent to {name}!")
                break

    # --- Buy Property ---
    if tile in property_prices and tile not in player["props"]:
        st.info(f"This property costs 💰 ${property_prices[tile]}")
        if st.button("🏠 Buy Property"):
            if player["money"] >= property_prices[tile]:
                player["money"] -= property_prices[tile]
                player["props"].append(tile)
                st.success(f"{turn} bought {tile}!")
                st.rerun()
            else:
                st.error("Not enough money!")

    elif tile in player["props"]:
        st.warning("🏠 You already own this property.")

    # --- End Turn Button ---
    if st.button("✅ End Turn"):
        st.session_state.just_rolled = False
        st.session_state.turn = names[1] if turn == names[0] else names[0]
        st.rerun()

# --- Player Summary ---
st.markdown("### 📋 Player Summary")
for name, p in players.items():
    st.markdown(f"<div style='background:#f4f4f4;padding:8px;border-radius:8px;margin-bottom:5px;'>\
        <b>{name}</b> → 💰 ${p['money']} | 📍 {tiles[p['pos']]} | 🏠 {', '.join(p['props']) if p['props'] else 'None'}</div>",
        unsafe_allow_html=True)

# --- Win/Lose Conditions ---
for name, p in players.items():
    if p["money"] <= 0:
        st.error(f"💀 {name} is bankrupt! Game Over.")
        st.stop()

total_props = len(property_prices)
for name, p in players.items():
    if len(p["props"]) == total_props:
        st.success(f"🏆 {name} owns all properties and wins!")
        st.stop()

# --- Restart ---
if st.button("🔄 Restart Game"):
    for key in ["player_names", "players", "turn", "just_rolled", "last_roll"]:
        if key in st.session_state:
            del st.session_state[key]
    st.success("Game reset! Enter names again to play.")
    st.rerun()
