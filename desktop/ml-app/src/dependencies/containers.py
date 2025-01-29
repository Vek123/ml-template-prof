from dependency_injector import containers, providers

from services.api import APIService, get_api_service
from settings import settings


class Gateways(containers.DeclarativeContainer):
    config = providers.Configuration()

    api_client = providers.Factory(
        APIService.get_session,
    )


class Services(containers.DeclarativeContainer):
    config = providers.Configuration()
    gateways = providers.DependenciesContainer()

    api_service = providers.Factory(
        get_api_service,
        session=gateways.api_client,
    )


class Application(containers.DeclarativeContainer):
    config = providers.Configuration()

    gateways = providers.Container(
        Gateways,
        config=config.gateways
    )
    services = providers.Container(
        Services,
        config=config.services,
        gateways=gateways,
    )
