#!/usr/bin/python3


def add_complex(x, y):
    a = x['r']
    b = x['i']
    c = y['r']
    d = y['i']
    c_real = a + b
    c_imag = c + d

    return {'r': c_real, 'i': c_imag}


def main():
    complex_dict = {}
    complex_dict['c1'] = {'r': 5, 'i': 3}
    complex_dict['c2'] = {'r': 3, 'i': -7}
    complex_dict['c3'] = add_complex(complex_dict['c1'], complex_dict['c2'])

    # complex_dict['add'] = add_complex
    complex_dict['add'] = lambda x, y: {'r': x['r'] + y['r'], 'i': x['i'] + y['i']}
    # with this lambda function, I could delete all the code above def main() and it
    # would still work the same way

    complex_dict['c4'] = complex_dict['add'](complex_dict['c1'], complex_dict['c2'])

    print(complex_dict)


if __name__ == '__main__':
    main()
