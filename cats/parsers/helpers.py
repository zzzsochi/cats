def _strip_lines(lines):
    lines = list(lines)

    for line in lines.copy():
        if not line.strip():
            del lines[0]
        else:
            break

    for line in reversed(lines.copy()):
        if not line.strip():
            del lines[-1]
        else:
            break

    for line in lines:
        yield line.rstrip()


def prepare_cat(cat):
    cat = '\n'.join(_strip_lines(cat.split('\n')))

    cat = (cat
           .replace('&gt;', '>')
           .replace('&lt;', '<')
           .replace('&amp;', '&')
           )

    return cat
