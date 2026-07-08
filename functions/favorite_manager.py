def favorite_limit(device, device_names, hw_states, sw_states, rb01_labels=(), rb02_labels=(), rb03_labels=()):
    limit = len(hw_states) + len(sw_states)
    if device == device_names[2]:
        limit += len(rb01_labels) + len(rb02_labels) + len(rb03_labels)
    return limit


def favorite_label(fav_index, device, device_names, hw_labels, sw_labels, rb01_labels=(), rb02_labels=(), rb03_labels=()):
    hw_count = len(hw_labels)
    sw_count = len(sw_labels)

    if fav_index < hw_count:
        return hw_labels[fav_index]

    sw_index = fav_index - hw_count
    if sw_index < sw_count:
        return sw_labels[sw_index]

    if device != device_names[2]:
        return f"FAV {fav_index + 1}"

    relay_index = fav_index - hw_count - sw_count
    if relay_index < len(rb01_labels):
        return rb01_labels[relay_index]
    relay_index -= len(rb01_labels)
    if relay_index < len(rb02_labels):
        return rb02_labels[relay_index]
    relay_index -= len(rb02_labels)
    if relay_index < len(rb03_labels):
        return rb03_labels[relay_index]
    return f"FAV {fav_index + 1}"


def favorite_status(
    fav_index,
    device,
    device_names,
    state_texts,
    hw_states,
    sw_states,
    sw_on_texts,
    sw_off_texts,
    relay_states_1to8=(),
    relay_states_9to16=(),
):
    hw_count = len(hw_states)
    sw_count = len(sw_states)

    if fav_index < hw_count:
        return state_texts[1] if hw_states[fav_index] else state_texts[0]

    sw_index = fav_index - hw_count
    if sw_index < sw_count:
        return sw_on_texts[sw_index] if sw_states[sw_index] else sw_off_texts[sw_index]

    if device != device_names[2]:
        return state_texts[0]

    relay_num = fav_index - hw_count - sw_count
    board = relay_num // 16
    bit = relay_num % 16
    if board < 0 or board >= len(relay_states_1to8) or board >= len(relay_states_9to16):
        return state_texts[0]

    if bit < 8:
        active = not (relay_states_1to8[board] & (1 << bit))
    else:
        active = not (relay_states_9to16[board] & (1 << (bit - 8)))
    return state_texts[1] if active else state_texts[0]


def favorite_target(fav_index, device, device_names, hw_states, sw_states):
    hw_count = len(hw_states)
    sw_count = len(sw_states)

    if fav_index < hw_count:
        return "HW", fav_index

    sw_index = fav_index - hw_count
    if sw_index < sw_count:
        return "SW", sw_index

    if device == device_names[2]:
        return "RELAY", fav_index - hw_count - sw_count
    return "UNKNOWN", fav_index


def build_qopt_favorites(fav_states, limit, label_for_index, max_slots=20):
    favorites = []
    for fav_index, enabled in enumerate(fav_states[:limit]):
        if not enabled:
            continue
        favorites.append({
            "fav_index": fav_index,
            "label": label_for_index(fav_index),
        })
        if len(favorites) >= max_slots:
            break
    return favorites
