KASKO_HAVAL = 130_000
KASKO_DEFAULT = 170_000


def get_loyal_tooltip(model):
    if model == "001":
        return "Geely, Belgee, Knewstar, Changan, Haval, Tank, Great Wall, Chery, GAC, Omoda, Exeed, Jetour, Jaecoo, Kaiyi, Baic, Jac, Faw, Ora, Jetta, Wey, Livan, Lifan, Hongqi, Soueast, Lixiang, Skywell, Voyah, Lynk & Co, Zeekr, Aito, Avatr, BYD, Dongfeng, Oting, SWM, VGV, TENET, Nio, Denta, Foton"

    elif model == "EX5 EM-i":
        return "Volkswagen, Skoda, Toyota, Nissan, Renault, Hyundai, Kia, Mazda, Lexus, Volvo, Geely, Belgee, Knewstar"

    else:
        return "Volkswagen, Skoda, Toyota, Nissan, Renault, BMW, Mercedes-Benz, Audi, Land Rover, Volvo, Geely, Belgee, Knewstar"
