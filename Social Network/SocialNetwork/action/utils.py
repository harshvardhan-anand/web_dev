from .models import Action

def create_action(user, verb=None, target=None):
    action = Action(user=user, verb=verb, target=target)
    action.save()