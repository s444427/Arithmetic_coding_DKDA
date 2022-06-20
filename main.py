def AC_code(alphabet, code, p, intervals):
    print('### Arithmetic Coding Coder ###')

    # STEP 1

    for k in range(len(code) - 1):
        size = intervals[code[k]][1] - intervals[code[k]][0]

        intervals[0][0] = intervals[code[k]][0]
        intervals[len(intervals) - 1][1] = intervals[code[k]][1]

        for i in range(len(alphabet) - 1):
            intervals[i][1] = intervals[i][0] + size * p[i]
            intervals[i + 1][0] = intervals[i][1]

        print(intervals)

    print('RESULT: ', intervals[code[-1]][0])
    return intervals[code[-1]][0]


def AC_intervals(alphabet, p):
    intervals = {}

    # STEP 0
    x = 0
    for i in alphabet:
        intervals[i] = [sum(p[:x]), sum(p[:x + 1])]
        x += 1

    print(intervals)
    return intervals


def AC_decoder(alphabet, coded, p, intervals):
    print('### Arithmetic Coding Decoder ###')

    code = []
    is_end = False
    count = 0

    while not is_end or count >= 10:
        # Check end
        count += 1
        for c in intervals:
            for j in [0, 1]:
                if intervals[c][j] == coded:
                    is_end = True

        # Get ID of fiting place
        for i in range(len(intervals)):
            if intervals[i][0] <= coded < intervals[i][1]:
                coder = i
                code.append(i)
                print(code)

        # Reshape
        size = intervals[coder][1] - intervals[coder][0]

        intervals[0][0] = intervals[coder][0]
        intervals[len(intervals) - 1][1] = intervals[coder][1]

        for i in range(len(alphabet) - 1):
            intervals[i][1] = intervals[i][0] + size * p[i]
            intervals[i + 1][0] = intervals[i][1]

        print(intervals)
        print(code)
    return code


if __name__ == '__main__':
    alphabet = [0, 1, 2, 3]
    p = [0.6, 0.2, 0.1, 0.1]

    # code = [0, 2, 3]
    intervals = AC_intervals(alphabet, p)

    # coded = AC_code(alphabet, code, p, intervals)
    coded = 0.534

    code = AC_decoder(alphabet, coded, p, intervals)
