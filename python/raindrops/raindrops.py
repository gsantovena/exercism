def convert(number):

    raindrops = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }

    result = ''.join(
        [raindrops[n] for n in raindrops.keys() if number % n == 0]
    )

    return str(number) if result == '' else result
