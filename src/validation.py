from flask import Flask, request, Response

def validate_query(expected_key_types : list[tuple[str, object]]):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for rule in expected_key_types:
                name, type = rule
                if not isinstance(request.args.get(name), type):
                    return Response(status=400)
            return func(args, kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator
def validate_form( expected_key_types : list[tuple[str, object]]):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for rule in expected_key_types:
                name, type = rule
                if not isinstance(request.form.get(name), type):
                    return Response(status=400)
            return func(args, kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator