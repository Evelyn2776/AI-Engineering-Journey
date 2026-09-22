hay = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

def needle (hay):
    try:

        target = "needle"
        position = hay.index(target)

        if target in hay:
            print(f"found the {target} at position {position}")
        return hay

    except ValueError:
        print(f"'{target}' is not in the list")

print(needle(hay))