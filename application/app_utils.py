import typing


class AppUtils:
    #TODO: how to mark that function returns function?
    @staticmethod
    def prefix_route(route_function: classmethod, prefix: str = '', mask: str = '{0}{1}') -> typing.Any:
        def newroute(route, *args, **kwargs):
            return route_function(mask.format(prefix, route), *args, **kwargs)

        return newroute
