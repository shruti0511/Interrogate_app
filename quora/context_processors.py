from quora.models import quoraTopic
from quora.forms import addAnswer
from authentication.forms import UserProfile


def add_variable_to_context(request):
    allTopics = quoraTopic.objects.all()
    return{'allTopics':allTopics , 'form':addAnswer}