# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> MongoDB components for Python Changelog

## <a name="3.2.5"></a> 3.2.5 (2022-06-07)

### Bug fixes
* Made GrpcService IReferenceable

## <a name="3.2.4"></a> 3.2.4 (2021-11-21)

### Bug fixes
* Updated imports

## <a name="3.2.3"></a> 3.2.3 (2021-09-01)

# Features
* Update GrpcClient:
    * add client_service param
    * add tracer
    * update _instrument method
    * update _call method

## <a name="3.2.0-3.2.2"></a> 3.2.0-3.2.2 (2021-08-28)

### Bug fixes
* Update tests
* Fixed type hints
* Fixed getting correlation id in call_command
* Fixed json serialization for CommandableGrpcService

### Features
* CommandableGrpcService added _apply_commands
* GrpcEndpoint add supports ssl_ca_file
* GrpcEndpoint removed _register_method and _register_interceptor
* GrpcService add:
    - register_commadable_method
    - _apply_validation
    - _apply_interceptors
    - _register_method
    - _register_method_with_auth
    - _register_interceptor
* Added **test** module


## <a name="3.1.0"></a> 3.1.0 (2021-05-26)

### Bug fixes
* fixed method names
* added docstrings and examples

### Features
* Added type hints


## <a name="3.0.1"></a> 3.0.1 (2021-04-14)
* Update references

## <a name="3.0.0"></a> 3.0.0 (2020-12-24)

Initial public release

### Features
* **Build** - factories for creating gRPC services
* **Clients** -  basic client components for grpc
* **Services** - basic service implementations for grpc