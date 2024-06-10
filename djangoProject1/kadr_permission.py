from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class OnlyLoggedKadr(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_kadr or self.request.user.is_manager

class OnlyLoggedManager(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_manager