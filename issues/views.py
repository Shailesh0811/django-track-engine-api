from django.http import HttpResponse
from issues.models import (
    Critical,
    Issue,
    LowPriority,
    MediumPriority,
    Reporter,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view



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

    #POST  /api/issues/  —  Create a new issue and in message describe the issue on the basis of priority

    elif request.method == 'POST':
        data = request.data
        priority = data.get('priority', '')
        if priority == 'high':
            issue = Critical(**data)
        elif priority == 'medium':
            issue = MediumPriority(**data)
        elif priority == 'low':
            issue = LowPriority(**data)
        else:
            issue = Issue(**data)
        try:
            saved = issue.persist()
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
        return Response(
            {
                "issue Created Successfully": saved,
                "issue": issue.describe(),
            }
        )


@api_view(['POST', 'GET'])
def reporters_handler(request):
    if request.method == 'GET':
        id = request.query_params.get('id')
        if id:
            reporter = Reporter.get_reporter_by_id(Reporter,id)
            if reporter:
                return Response(reporter)
            else:
                return Response({"error": "Reporter not found"}, status=404)
        else:
            reporters = Reporter.get_all_reporters(Reporter)
            return Response(reporters)
    if request.method == 'POST':
        data = request.data
        reporter = Reporter(**data)
        saved = reporter.persist()
        return Response({"reporter Created Successfully": saved})