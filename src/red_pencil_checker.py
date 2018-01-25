def is_promo_active(original, new):
    highActivationPrice = original * .95
    lowActivationPrice = original * .7

    if(new <= highActivationPrice and new >= lowActivationPrice):
        return True
    else:
        return False

