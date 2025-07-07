# **ASSIGNMENT: 3**
# **Python Assignment: Smart Home Automation System**


## **1. Device Management (Lists & Tuples)**
### Task 1.1: Create and Manage a List of Smart Devices**

import streamlit as st

if "smart_devices" not in st.session_state:
    st.session_state.smart_devices = [
        "smart plug", "smart speaker", "smart vaccum", "automatic smart feeder", "smart wifi"
    ]

st.title("Smart Devices Manager")


option = st.selectbox("What do you want to do?", ["Nothing", "Add", "Remove", "Sort"])

if option == "Add":
    quantity = st.number_input("How many devices do you want to add?", min_value=1, step=1, key="qty")
    
    for i in range(quantity):
        new_device = st.text_input(f"Enter device {i+1} name:", key=f"device_{i}")
        if new_device:
            if new_device not in st.session_state.smart_devices:
                st.session_state.smart_devices.append(new_device)
    
    st.write("✅ Updated Smart Devices List:")
    st.write(st.session_state.smart_devices)

elif option == "Remove":
    device_to_remove = st.selectbox("Select device to remove", st.session_state.smart_devices)
    if st.button("Remove Device"):
        st.session_state.smart_devices.remove(device_to_remove)
        st.success(f"{device_to_remove} removed!")

elif option == "Sort":
    if st.button("Sort Devices Alphabetically"):
        st.session_state.smart_devices.sort()
        st.success("Devices sorted!")

elif option == "Nothing":
    st.write("Okay, goodbye! Thank you for visiting.")

# Final view of smart devices list

st.subheader("Current Smart Devices:")
st.write(st.session_state.smart_devices)



### Task 1.2: Store Device Settings Using Tuples**


import streamlit as st

# --- Device Data using Tuples (name, status, watts) ---
devices = (
    ("Smart Plug", "ON", 10),
    ("Smart Speaker", "OFF", 5),
    ("Smart Vacuum", "ON", 50),
    ("Automatic Smart Feeder", "OFF", 3),
    ("Smart WiFi", "ON", 15)
)


st.title("Smart Device Settings Viewer")


option = st.selectbox("What do you want to do?", ["Select an option", "View", "Quit"])

if option == "View":
    st.subheader("Device Settings:")
    for name, status, power in devices:
        st.write(f"📱 **{name}** - Status: `{status}`, Power: `{power}W`")
elif option == "Quit":
    st.success("✅ Thank you for coming. Bye!")


import streamlit as st

# Title
st.title("🔌 Energy Consumption Tracker")

# --- Initialize energy usage dictionary in session ---
if "energy_usage" not in st.session_state:
    st.session_state.energy_usage = {
        "smart light": "20Kwh",
        "smart bell": "10Kwh",
        "smart wifi": "50Kwh"
    }

# --- Main Option Menu ---
option = st.selectbox(
    "What do you want to do?",
    ["Select an option", "Add or Update", "Remove", "Display Total Usage", "Nothing"]
)

# --- Add or Update ---
if option == "Add or Update":
    num_devices = st.number_input("How many devices' energy usage do you want to add/update?", min_value=1, step=1)
    
    for i in range(num_devices):
        key = st.text_input(f"Enter name for device #{i+1}", key=f"device_{i}")
        value = st.text_input(f"Enter energy usage for {key} (number only)", key=f"value_{i}")
        
        if key and value:
            if value.replace('.', '').isdigit():
                st.session_state.energy_usage[key] = value + "Kwh"
            else:
                st.warning(f"⚠️ Value for {key} must be a number!")

    st.write("✅ Updated Energy Usage Data:")
    st.write(st.session_state.energy_usage)

# --- Remove a device ---
elif option == "Remove":
    if st.session_state.energy_usage:
        to_remove = st.selectbox("Select a device to remove:", list(st.session_state.energy_usage.keys()))
        if st.button("Remove Device"):
            del st.session_state.energy_usage[to_remove]
            st.success(f"✅ Removed '{to_remove}' successfully.")
    else:
        st.info("No devices to remove.")

# --- Display Total Usage ---
elif option == "Display Total Usage":
    total = 0
    for v in st.session_state.energy_usage.values():
        try:
            total += float(v.replace("Kwh", "").strip())
        except ValueError:
            st.warning(f"Could not process value: {v}")
    st.metric("🔋 Total Energy Usage", f"{total} Kwh")

# --- Exit ---
elif option == "Nothing":
    st.success("👋 Thank you for coming! Bye!")



import streamlit as st

# --- Initialize modes set ---
if "modes" not in st.session_state:
    st.session_state.modes = {"Night mode", "Day mode", "Sleepy mode"}

st.header("🌙 Power-Saving Modes Manager")

mode_action = st.selectbox("What do you want to do with modes?", ["Select an option", "Add", "Check", "View", "Nothing"])

if mode_action == "Add":
    new_mode = st.text_input("Enter mode to add:", key="add_mode")
    if new_mode:
        st.session_state.modes.add(new_mode.capitalize())
        st.success("✅ Mode added successfully.")

elif mode_action == "Check":
    check_mode = st.text_input("Enter mode to check:", key="check_mode")
    if check_mode:
        if check_mode.capitalize() in st.session_state.modes:
            st.success("✅ Yes, mode exists.")
        else:
            st.warning("❌ No, mode not found.")

elif mode_action == "View":
    st.write("🔎 Current Modes:", st.session_state.modes)

elif mode_action == "Nothing":
    st.success("✅ Thank you for using the system.")

# Task 3.1
st.header("💸 Monthly Energy Cost Calculator")

energy_used = st.number_input("Enter total energy usage (kWh):", min_value=0)
rate = st.number_input("Enter electricity rate per kWh:", min_value=0)

if st.button("Calculate Cost"):
    cost = energy_used * rate
    st.write(f"Total Monthly Energy Cost: **{cost} PKR**")

# Task3.2
st.header("🏠 Common Devices in Two Homes")

home_1 = ["smart fan", "smart bell", "smart clock", "smart bulb", "smart plug"]
home_2 = ["smart lights", "smart fan", "smart feeder", "smart car", "smart clock"]

set_1 = set(home_1)
set_2 = set(home_2)
common = set_1.intersection(set_2)

st.write("Home 1 Devices:", home_1)
st.write("Home 2 Devices:", home_2)
st.success(f"🔁 Common Devices: {list(common)}")

# Task4.1
st.header("⚙️ Create Automation Rule")

device = st.text_input("Enter device name:")
time = st.text_input("Enter time (e.g., 3:00 PM):")
action = st.selectbox("Select action:", ["On", "Off"])

if st.button("Create Rule"):
    st.success(f"✅ {device} will be turned **{action}** at **{time}**.")



# Task4.2
st.header("🔋 Optimize Power Consumption")

devices = [("fan", 1200), ("lights", 50), ("plug", 400)]

threshold = st.number_input("Enter max power threshold (Watts):", min_value=0, value=1000)

active_devices = [device for device, power in devices if power <= threshold]

st.write("Original Devices:", devices)
st.success(f"✅ Active Devices under {threshold}W: {active_devices}")



