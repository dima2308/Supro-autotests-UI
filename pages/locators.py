from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGIN_FIELD = (By.ID, "login-form-login")
    PASSWORD_FIELD = (By.ID, "login-form-password")
    LOGIN_ERROR = (By.XPATH, "//*[@id='login-form']/div[1]/div")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "div.form-group:nth-child(3) > div:nth-child(3)")
    CHECKBOX_REMEMBER = (By.ID, "login-form-rememberme")
    NOT_RECEIVED_LETTER_BUTTON = (By.LINK_TEXT, "Не пришло письмо?")
    FORGET_PASSWORD_BUTTON = (By.LINK_TEXT, "Забыли пароль?")


class RecoveryPageLocators:
    EMAIL_FIELD_PASSWORD = (By.ID, "recovery-form-email")
    EMAIL_FIELD_RESEND = (By.ID, "resend-form-email")
    SUBMIT_BUTTON = (By.TAG_NAME, "button")
    ERROR = (By.CLASS_NAME, "help-block")
    SUCCESS_TEXT = (By.ID, "w0")
    SUCCESS_BUTTON = (By.CLASS_NAME, "close")


class MainPageLocators:
    LOGO_LINK = (By.CLASS_NAME, "logo")
    SIDEBAR_TOGGLE = (By.CLASS_NAME, "sidebar-toggle")
    INFO_BOXES = (By.CLASS_NAME, "info-box-text")
    PRODUCTS_TABLE = (By.ID, "w0")
    DROPDOWN_TOGGLE = (By.CLASS_NAME, "dropdown-toggle")
    LOG_OUT_BUTTON = (By.LINK_TEXT, "Выйти")
    PROFILE_BUTTON = (By.LINK_TEXT, "Профиль")
    USER_INFO_MAIN = (By.CLASS_NAME, "pull-left.info")
    USER_INFO_ADD = (By.CLASS_NAME, "hidden-xs")
    # быстрые действия
    NEW_SUGGEST_BUTTON = (By.LINK_TEXT, "Создать новое предложение")
    NEW_PRODUCT_BUTTON = (By.LINK_TEXT, "Создать новый продукт")
    # справочники
    TYPES_OFFERS_LINK = (By.LINK_TEXT, "Виды предложений")
    OFFERS_LINK = (By.LINK_TEXT, "Предложения")
    TYPES_PRODUCTS_LINK = (By.LINK_TEXT, "Виды продуктов")
    PRODUCTS_LINK = (By.LINK_TEXT, "Продукты")
    PRODUCTS_PARAMS_LINK = (By.LINK_TEXT, "Параметры продуктов")
    CLIENT_SEGMENTS = (By.LINK_TEXT, "Клиентские сегменты")
    # связи
    OFFERS_RELATIONSHIPS_LINK = (By.LINK_TEXT, "Зависимости предложений")
    OFFERED_PRODUCTS_LINK = (By.LINK_TEXT, "Предлагаемые продукты")
    OFFERS_PARAMS_LINK = (By.LINK_TEXT, "Параметры предложений")
    OFFERS_SEGMENTS_LINK = (By.LINK_TEXT, "Сегменты предложений")
    PHONES_SEGMENTS = (By.LINK_TEXT, "Телефоны сегментов")
    # метрики
    SALES_LINK = (By.LINK_TEXT, "Продажи")
    # система
    USERS_LINK = (By.LINK_TEXT, "Пользователи")
    CACHING_LINK = (By.LINK_TEXT, "Кэширование")
    SUPPORT_LINK = (By.LINK_TEXT, "Поддержка")
    HELP_LINK = (By.LINK_TEXT, "Справка")


class TypeOfferPageLocators:
    OFFER_TYPE_NAME = (By.ID, "offertype-name")
    OFFER_TYPE_COMMENT = (By.ID, "offertype-comment")
    OFFER_TYPE_SUBMIT_BUTTON = (By.TAG_NAME, "button")
    NAME_ERROR = (By.CSS_SELECTOR, "div.form-group:nth-child(2) > div:nth-child(3)")
    OFFER_TYPE_EDITED_FROM_TABLE = (By.CSS_SELECTOR, "tbody tr:last-child td:nth-child(5)")


class ContactPageLocators:
    CONTACT_NAME = (By.ID, "contactform-name")
    CONTACT_EMAIL = (By.ID, "contactform-email")
    CONTACT_SUBJECT = (By.ID, "contactform-subject")
    CONTACT_TEXT = (By.ID, "contactform-body")
    CONTACT_CAPTCHA = (By.ID, "contactform-verifycode")
    CONTACT_SUBMIT_BUTTON = (By.NAME, "contact-button")


class AboutPageLocators:
    BOX_BODY_LINKS = (By.CSS_SELECTOR, ".box-body a")


class OfferPageLocators:
    OFFER_SUBMIT_BUTTON = (By.TAG_NAME, "button")
    OFFER_NAME = (By.ID, "offer-name")
    OFFER_COMMENT = (By.ID, "offer-comment")
    OFFER_TYPE = (By.ID, "0")
    OFFER_START_DATE = (By.ID, "offer-begins")
    OFFER_REMOVE_START_DATE_BUTTON = (By.CSS_SELECTOR, "#offer-begins-datetime > span:nth-child(2)")
    OFFER_FINISH_DATE = (By.ID, "offer-ends")
    OFFER_REMOVE_FINISHT_DATE_BUTTON = (By.CSS_SELECTOR, "#offer-ends-datetime > span:nth-child(2)")


class TaskPageLocators:
    THEAD = (By.CSS_SELECTOR, "thead tr th")
    TABLE_EMPTY_BODY = (By.CLASS_NAME, "empty")
    TABLE_TR = (By.CSS_SELECTOR, "tbody tr:last-child td")
    REMOVE_FLAG = (By.CSS_SELECTOR, "tbody tr:last-child td:nth-last-child(2)")
    LOOK_BUTTON_FROM_TABLE = (By.CSS_SELECTOR, "tbody tr:last-child td:last-child a[aria-label='Просмотр']")
    EDIT_BUTTON_FROM_TABLE = (By.CSS_SELECTOR, "tbody tr:last-child td:last-child a[aria-label='Редактировать']")
    REMOVE_BUTTON_FROM_TABLE = (By.CSS_SELECTOR, "tbody tr:last-child td:last-child a[aria-label='Удалить']")
    BUTTON = (By.CLASS_NAME, "btn-success")
    NAME_FROM_TABLE = (By.CSS_SELECTOR, "tbody tr:last-child td:nth-child(3)")
    CREATE_PARAM_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")


class ParamsPageLocators:
    PARAM_TYPE = (By.NAME, "OfferProductParam[type_id]")
    PARAM_VALUE = (By.NAME, "OfferProductParam[value]")
    OFFER_NAME = (By.CSS_SELECTOR, "div.form-group:nth-child(3) > h3:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.form-group:nth-child(4) > h3:nth-child(1)")


class CachePageLocators:
    CACHE_KEY = (By.CSS_SELECTOR, "tbody tr:last-child td:nth-child(2)")
    CASHE_TTL = (By.CSS_SELECTOR, "tbody tr:last-child td:nth-child(4)")
    CACHE_BOX_TITLE = (By.CLASS_NAME, "box-title")
    CACHE_STRINGS = (By.CSS_SELECTOR, "tbody tr td:last-child a[aria-label='Удалить']")