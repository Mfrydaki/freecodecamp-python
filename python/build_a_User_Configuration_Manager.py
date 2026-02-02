# User settings management functions

def add_setting(setting_dict, setting_pair):
    # Adds a new setting if it does not already exist
    key, value = setting_pair

    key = key.lower()
    value = value.lower()

    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    setting_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(sett_dict, sett_pair):
    # Updates the value of an existing setting
    key, value = sett_pair

    key = key.lower()
    value = value.lower()

    if key in sett_dict:
        sett_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(delset_dict, key):
    # Deletes a setting by key if it exists
    key = key.lower()

    if key in delset_dict:
        del delset_dict[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings_dict):
    # Returns formatted user settings or a message if no settings exist
    if not settings_dict:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in settings_dict.items():
        result += f"{key.capitalize()}: {value}\n"

    return result
