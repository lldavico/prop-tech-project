from src.system.feed import Feed



class System:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._current_ads = None
        self.feed = Feed()

    def _show_feed_ads(self):
        self._current_ads = self.feed._show_and_get_ads()

    def _display_menu(self):
        option = input("""
            Elige alguna opción: 
            (1) Selecciona una propiedad para ver
            (2) Cerrar sesión
                       
            """)
        if option == '1':
            ad_option = input('Elige una propiedad para ver: ')
            if ad_option not in self._current_ads:
                print('Opción no válida')
                return self._display_menu()
            print(self._current_ads[ad_option])
        elif option == '2':
            print('Cerrando sesión...')
            return
        else:
            print('Opción no válida')
        
        self._display_menu()
        

    def run(self):
        print('Welcome to my startup!')
        self._show_feed_ads()
        self._display_menu()

