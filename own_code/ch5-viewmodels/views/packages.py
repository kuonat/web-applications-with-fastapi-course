import fastapi
from starlette.requests import Request
from fastapi_chameleon import template

from viewmodels.packages.details_viewmodel import DetailsViewModel 

router = fastapi.APIRouter()


@router.get('/project/{package_name}')
@template(template_file='packages/details.pt')
def details(package_name: str, request: Request):
    vm = DetailsViewModel(package_name, request)
    return vm.to_dict()