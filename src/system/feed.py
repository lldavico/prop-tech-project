from typing import List
from src.db.ads import get_ads


# Singleton
class Feed:

    def _show_and_get_ads(self):
        ads = get_ads()
        enumerated_ads = {}
        for i, ad in enumerate(ads, start=1):

            print('****************************************')
            print(f'({i}) {ad}')
            print('****************************************')
            enumerated_ads[str(i)] = ad

        return enumerated_ads


    