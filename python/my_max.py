
def binrep(n):
    return bin(n)[2:]


def pad_binreps(a,b):
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        diff = len_b - len_a
        a = ''.join(['0']*diff) + a
    elif len_a > len_b:
        diff = len_a - len_b
        b = ''.join(['0']*diff) + b
    return a,b


def my_max_worker_recursive(a, b):
    print(f"Working on A = {a}, B = {b}")
    # Assume:
    # - a and b are equal-length binary strings
    # Correct, but recursion depth too high
    a_msb = None
    b_msb = None
    for i in range(len(a)):
        if a[i] == '1':
            a_msb = i
            print(f"found A MSB at {i}")
        if b[i] == '1':
            b_msb = i
            print(f"found B MSB at {i}")
        if a_msb is not None and b_msb is None:
            print("A is max")
            return a
        elif a_msb is None and b_msb is not None:
            print("B is max")
            return b
        elif a_msb is not None and b_msb is not None:
            a_substr = a[i:]
            b_substr = b[i:]
            print(f"Recursing on substrings: A = {a_substr}, B = {b_substr}")
            return my_max_worker(a_substr, b_substr)
    return a


def my_max_worker_iterative(a, b):
    a_msb = None
    b_msb = None
    n_bits = len(a)
    i = -1
    while i < n_bits-1:
        i += 1
        if a[i] != b[i]:
            if a[i] == '1':
                #print("A max")
                return a
            else:
                #print("B max")
                return b
    #print("Equal")        
    return a


def my_max(a, b):
    # Preconditions
    assert isinstance(a, int)
    assert isinstance(b, int)
    # Preprocess:
    # - Get binary string representations of input integers
    # - Left zero pad shorter representation
    bin_a = binrep(a)
    bin_b = binrep(b)
    bin_a, bin_b = pad_binreps(bin_a, bin_b)
    #print(f"Padded representations: A = {bin_a}, B = {bin_b}")
    # Algorithm:
    # - Iterate from MSB to LSB:
    #   - Case 1: a has higher MSB than b -> a is max
    #   - Case 2: b has higher MSB than a -> b is max
    #   - Case 3: MSBs occur at same position. Recurse on substring. 
    result = my_max_worker_iterative(bin_a, bin_b)
    if result == bin_a:
        return a
    else:
        return b



if __name__ == "__main__":
    a, b = pad_binreps(binrep(17), binrep(5))
    assert len(a) == len(b)

    assert my_max(1, 0) == 1
    assert my_max(0, 0) == 0
    assert my_max(1, 1) == 1
    assert my_max(2, 3) == 3
    assert my_max(17,36) == 36
