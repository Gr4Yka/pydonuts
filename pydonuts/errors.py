# https://vkdonuts.ru/api

class UnknownMethod(Exception):    pass # 1000
class RequiredParameters(Exception):   pass # 1001
class IncorrectValues(Exception):   pass # 1002
class AuthorisationException(Exception):    pass # 1004
class VersionDeprecated(Exception):   pass # 1005
class ServiceUnavailable(Exception):    pass # 1006
class CallLimitExceeded(Exception):    pass # 2000
class NoActiveCampaign(Exception):    pass # 3000
