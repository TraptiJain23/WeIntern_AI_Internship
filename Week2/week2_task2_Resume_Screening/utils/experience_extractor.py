import re

def extract_experience(text):

    experience_entries = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Resume formats like:
        # Social Media Executive | Company
        # Team Head & Member | Club

        if "|" in line:
            experience_entries.append(line)

        # Resume formats like:
        # Personal Trainer
        # Travel Agent
        # Account Manager

        elif re.search(
            r'(manager|executive|trainer|agent|developer|engineer|analyst|intern|coordinator|specialist|consultant|assistant|head|lead)',
            line.lower()
        ):
            experience_entries.append(line)

    if experience_entries:
        return "\n".join(dict.fromkeys(experience_entries))

    return "Experience not found"