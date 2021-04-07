# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import *

from ....api import Request, Response, set_timeout, set_tenant_key, set_user_access_token, set_path_params, \
    set_query_params, set_response_stream, set_is_response_stream, FormData, FormDataFile
from ....config import Config
from ....consts import ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER, ACCESS_TOKEN_TYPE_APP
from .model import *


class Service(object):
    def __init__(self, conf):
        # type: (Config) -> None
        self.conf = conf
        self.authens = AuthenService(self)
        



class AuthenService(object):
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def access_token(self, body, timeout=None):
        # type: (AuthenAccessTokenReqBody, int) -> AuthenAccessTokenReqCall

        request_opts = []   # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        return AuthenAccessTokenReqCall(self, body, request_opts=request_opts)

    def refresh_access_token(self, body, timeout=None):
        # type: (AuthenRefreshAccessTokenReqBody, int) -> AuthenRefreshAccessTokenReqCall

        request_opts = []   # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        return AuthenRefreshAccessTokenReqCall(self, body, request_opts=request_opts)

    def user_info(self, user_access_token=None, timeout=None):
        # type: (str, int) -> AuthenUserInfoReqCall

        request_opts = []   # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return AuthenUserInfoReqCall(self, request_opts=request_opts)



class AuthenAccessTokenReqCall(object):
    def __init__(self, service, body, request_opts=None):
        # type: (AuthenService, AuthenAccessTokenReqBody, List[Any]) -> None

        self.service = service
        self.body = body

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> Response[UserAccessTokenInfo]
        root_service = self.service.service

        conf = root_service.conf
        req = Request('authen/v1/access_token', 'POST', [ACCESS_TOKEN_TYPE_APP],
                      self.body, output_class=UserAccessTokenInfo, request_opts=self.request_opts)
        resp = req.do(conf)
        return resp


class AuthenRefreshAccessTokenReqCall(object):
    def __init__(self, service, body, request_opts=None):
        # type: (AuthenService, AuthenRefreshAccessTokenReqBody, List[Any]) -> None

        self.service = service
        self.body = body

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> Response[UserAccessTokenInfo]
        root_service = self.service.service

        conf = root_service.conf
        req = Request('authen/v1/refresh_access_token', 'POST', [ACCESS_TOKEN_TYPE_APP],
                      self.body, output_class=UserAccessTokenInfo, request_opts=self.request_opts)
        resp = req.do(conf)
        return resp


class AuthenUserInfoReqCall(object):
    def __init__(self, service, request_opts=None):
        # type: (AuthenService, List[Any]) -> None

        self.service = service
        

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> Response[UserInfo]
        root_service = self.service.service

        conf = root_service.conf
        req = Request('authen/v1/user_info', 'GET', [ACCESS_TOKEN_TYPE_USER],
                      None, request_opts=self.request_opts)
        resp = req.do(conf)
        return resp

