from config import main_url
from pages.locators import MainPageLocators
from pages.locators import RecoveryPageLocators


links_locators = [(MainPageLocators.NEW_SUGGEST_BUTTON, 'Создать новое предложение'),
                  (MainPageLocators.NEW_PRODUCT_BUTTON, 'Создать новый продукт'),
                  (MainPageLocators.TYPES_OFFERS_LINK, 'Виды предложений'),
                  (MainPageLocators.OFFERS_LINK, 'Предложения'),
                  (MainPageLocators.TYPES_PRODUCTS_LINK, 'Виды продуктов'),
                  (MainPageLocators.PRODUCTS_LINK, 'Продукты'),
                  (MainPageLocators.PRODUCTS_PARAMS_LINK, 'Виды параметров продуктовых предложений'),
                  (MainPageLocators.CLIENT_SEGMENTS, 'Клиентские сегменты'),
                  (MainPageLocators.OFFERS_RELATIONSHIPS_LINK, 'Зависимости предложений'),
                  (MainPageLocators.OFFERED_PRODUCTS_LINK, 'Предлагаемые продукты'),
                  (MainPageLocators.OFFERS_PARAMS_LINK, 'Параметры предлагаемых продуктов'),
                  (MainPageLocators.OFFERS_SEGMENTS_LINK, 'Предложения для клиентских сегментов'),
                  (MainPageLocators.PHONES_SEGMENTS, 'Телефоны клиентского сегмента'),
                  (MainPageLocators.SALES_LINK, 'Дополнительные продажи за год'),
                  # (MainPageLocators.USERS_LINK, 'Пользователи'),
                  (MainPageLocators.CACHING_LINK, 'Управление кэшированием'),
                  (MainPageLocators.SUPPORT_LINK, 'Поддержка'),
                  (MainPageLocators.HELP_LINK, 'Справка')
                  ]

links_names = ['Create new offer', 'Create new product', 'Types offers',
               'Offers', 'Types products', 'Products', 'Poducts params', 'Client segments', 'Offers relationship',
               'Offered products', 'Offers params', 'Offers segments', 'Phone segments', 'Sales',
               'Caching', 'Support', 'Help']

invalid_emails = ['ff', 'Йцукен', '1мf', '@', '@mail.ru', '.ru']

info_boxes = ['ДЕЙСТВУЮЩИЕ ПРЕДЛОЖЕНИЯ', 'ПРЕДЛАГАЕМЫЕ ПРОДУКТЫ', 'ВСЕГО ПРОДУКТОВ', 'БАННЕРОВ АКТИВНО']

test_data_recovery = [
    (main_url + '/user/forgot', RecoveryPageLocators.EMAIL_FIELD_PASSWORD),
    (main_url + '/user/resend', RecoveryPageLocators.EMAIL_FIELD_RESEND),
]

results_codes = {
    'passed': 1,
    'blocked': 2,
    'retest': 4,
    'failed': 5
}
