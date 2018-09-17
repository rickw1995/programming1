def lang_genoeg(lengte):
    if lengte >= 120:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Je bent te klein!')

lengte = input('Hoelang ben jij in centimeters?')

(lang_genoeg(int(lengte)))
