from django.conf.urls import patterns, url, include
from viewflow import views as viewflow
from studentapply.flows import HelloWorldFlow, StudentApplyFlow
from studentapply import views

urlpatterns = [
    url(r'^helloworld/', include([
        HelloWorldFlow.instance.urls,
        url('^$', viewflow.ProcessListView.as_view(), name='index'),
        url('^tasks/$', viewflow.TaskListView.as_view(), name='tasks'),
        url('^queue/$', viewflow.QueueListView.as_view(), name='queue'),
        url('^details/(?P<process_pk>\d+)/$', viewflow.ProcessDetailView.as_view(), name='details'),
    ], namespace=HelloWorldFlow.instance.namespace), {'flow_cls': HelloWorldFlow}),

    url(r'^studentapply/', views.index, name='indexform')
    ]
#        url(r'^studentapply/', include([
#        StudentApplyFlow.instance.urls,
#        url('^$', viewflow.ProcessListView.as_view(), name='index'),
#        url('^tasks/$', viewflow.TaskListView.as_view(), name='tasks'),
#        url('^queue/$', viewflow.QueueListView.as_view(), name='queue'),
#        url('^details/(?P<process_pk>\d+)/$', viewflow.ProcessDetailView.as_view(), name='details'),
#    ], namespace=StudentApplyFlow.instance.namespace), {'flow_cls': StudentApplyFlow})
#    ]