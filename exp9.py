import math


def first_fit(items, capacity=1.0):
    bins = []
    bin_contents = []
    for item in items:
        placed = False
        for i, space in enumerate(bins):
            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break
        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])
    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)
    bins = []
    bin_contents = []
    for item in sorted_items:
        best_idx = -1
        best_space = float('inf')
        for i, space in enumerate(bins):
            if space >= item and (space - item) < best_space:
                best_space = space - item
                best_idx = i
        if best_idx >= 0:
            bins[best_idx] -= item
            bin_contents[best_idx].append(item)
        else:
            bins.append(capacity - item)
            bin_contents.append([item])
    return bin_contents


def html_bins(label, bins):
    rows = []
    for i, b in enumerate(bins, 1):
        used = sum(b)
        bar = '#' * int(used * 20)
        rows.append(
            f'<tr>'
            f'<td>{i}</td>'
            f'<td>{", ".join(str(round(x, 1)) for x in b)}</td>'
            f'<td>{used:.1f}</td>'
            f'<td><code>{bar}</code></td>'
            f'</tr>'
        )
    return (
        f'<h2>{label}: {len(bins)} bins</h2>\n'
        f'<table border="1" cellspacing="0" cellpadding="4">\n'
        f'<tr><th>Bin</th><th>Items</th><th>Used</th><th>Bar</th></tr>\n'
        + "\n".join(rows)
        + '\n</table>\n'
    )


def build_html(items, capacity, ff_bins, ffd_bins, bfd_bins):
    total = sum(items)
    lower_bound = math.ceil(total / capacity) if capacity else 0