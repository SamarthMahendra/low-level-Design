





def process(url: str) -> str:
    url_parts = url.split("/")
    minor_parts = []
    for part in url_parts:
        temp = part.split(".")
        minor_parts.append(temp)
    res = []
    for part in minor_parts:
        temp = []
        for minor in part:
            minor = minor[0] + str(len(minor)-2) + minor[-1]
            temp.append(minor)
        res.append(temp)

    result = []
    for part in res:
        result.append('.'.join(part))

    return '/'.join(result)




def shorten_url(url: str, m: int = None, t: int = None) -> str:
    def compress(s: str) -> str:
        if len(s) <= 2:
            return s
        return f"{s[0]}{len(s)-2}{s[-1]}"

    # Step 1: split into major/minor (keep originals for now)
    majors = [part.split('.') for part in url.split('/')]

    # Step 2: enforce m (max per major)
    if m is not None:
        for i, part in enumerate(majors):
            if len(part) > m:
                head, tail = part[:m-1], ''.join(part[m-1:])
                majors[i] = head + [tail]

    # Step 3: enforce t (global total)
    if t is not None:
        flat = [minor for part in majors for minor in part]
        if len(flat) > t:
            keep, tail = flat[:t-1], ''.join(flat[t-1:])
            flat = keep + [tail]

            # rebuild majors from flat
            majors, idx = [], 0
            for part in url.split('/'):
                cnt = len(part.split('.'))
                new = flat[idx:idx+min(cnt, len(flat)-idx)]
                idx += len(new)
                if new:
                    majors.append(new)

    # Step 4: compress everything at the end
    majors = [[compress(minor) for minor in part if minor] for part in majors]

    return '/'.join('.'.join(part) for part in majors if part)





print(process("stripe.com/payments/checkout/customer.john.doe"))

print(shorten_url("stripe.com/payments/checkout/customer.john.doe", 2))








