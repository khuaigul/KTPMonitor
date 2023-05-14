from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main', views.main, name='main'),
    path('registration', views.registration, name='registration'),
    path('continue_registration', views.continue_registration, name='continue_registration'),
    path('div_info', views.div_info, name='div_info'),
    path('divisions', views.divisions, name='divisions'),
    path('menu', views.menu, name='menu'),
    path('new_division', views.new_division, name='new_division'),
    path('students', views.students, name='students'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('signin', views.signin, name='signin'),
    path('registrationRe', views.registrationRe, name='registrationRe'),
    path('profileData', views.profileData, name='profileData'),
    path('divisionsRe', views.divisionsRe, name='divisionsRe'),
    path('сhangeDiv', views.сhangeDiv, name='сhangeDiv'),
    path('newDivisionRe', views.newDivisionRe, name='newDivisionRe'),
    path('profileData/<slug:uidb64>/<slug:token>/',
        views.profileData, name='profileData'),
    path('sendProfileData', views.sendProfileData, name='sendProfileData'),
    path('teacherProfile', views.teacherProfile, name='teacherProfile'),    
    path('editTeacherProfile', views.editTeacherProfile, name='editTeacherProfile'),    
    path('contests', views.contests, name='contests'),
    path('contest', views.contest, name='contest'),
    path('currentProfileData', views.currentProfileData, name='currentProfileData'),
    path('pupilProfile', views.pupilProfile, name='pupilProfile'),
    path('logout', views.logout, name='logout'),
    path('pupil', views.pupil, name='pupil'),
    path('students_by_div', views.students_by_div, name='students_by_div'),
    path('teachers_by_div', views.teachers_by_div, name='teachers_by_div'),
    path('pupilInfo', views.pupilInfo, name='pupilInfo'),
    path('pupilStats', views.pupilStats, name='pupilStats'),
    path('division_stats', views.division_stats, name='division_stats'),
    path('divisionStats', views.divisionStats, name='divisionStats'),
    path('contestStats', views.contestStats, name='contestStats'),
    path('contestsList', views.contestsList, name='contestsList'),
    path('deleteDivision', views.deleteDivision, name='deleteDivision'),
    path('newContest', views.newContest, name='newContest'),
    path('updateTeacherProfileData', views.updateTeacherProfileData, name='updateTeacherProfileData'),    
    path('addContest', views.addContest, name='addContest'),
    path('edit_pupil_profile', views.edit_pupil_profile, name='edit_pupil_profile'),

]
 