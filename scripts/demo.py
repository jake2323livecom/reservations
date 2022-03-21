from django.contrib.auth.models import User
from summer_picnic.models import PicnicReservation as PR
from jcu_ball.models import BallReservation as BR


def run():
	User.objects.create_superuser('admin',password='?Js0c2kld')
	user1 = User.objects.create_user('jake', 'jake.2323@live.com', '?Js0c2kld')
	user2 = User.objects.create_user('josh', 'josh@gmail.com', '?Js0c2kld')

	for _ in range(100):
		BR.objects.create(first_name='jake',middle_initial='a',last_name='richman',created_by=user1)
		PR.objects.create(first_name='josh',middle_initial='b',last_name='brolin',created_by=user2)

