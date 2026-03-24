from django.http import HttpResponse
from issues.models import Reporter, Issue
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view



def index(request):
    return HttpResponse("Issues app is ready.")

#In your POST /api/issues/ view, instantiate the correct subclass based on priority and include describe() in the response. For medium and high priority, use the base Issue class.

@api_view(['GET', 'POST'])
def issues_handler(request):
    if request.method == 'GET':
        id = request.query_params.get('id')
        status = request.query_params.get('status')
        print(id)
        if id:  
            issue = Issue.get_issue_by_id(Issue,id)
            if issue:
                return Response(issue)
            else:
                return Response({"error": "Issue not found"}, status=404)
        elif status:
            issues = Issue.get_issues_by_status(Issue,status)
            return Response(issues)
        else:
            issues = Issue.get_all_issues(Issue)
            return Response(issues)
    elif request.method == 'POST':
        data = request.data
        priority = data['priority']
        if priority == 'high':
            issue = Critical(**data)
        elif priority == 'medium':
            issue = MediumPriority(**data)
        elif priority == 'low':
            issue = LowPriority(**data)
        else:
            issue = Issue(**data)
        return Response({"issue": issue.describe()})


