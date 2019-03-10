from django.contrib.auth.tokens import PasswordResetTokenGenerator


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, access_token, timestamp):
        """
        replace user by access_token
        """
        # Truncate microseconds so that tokens are consistent even if the
        # database doesn't support microseconds.
        login_timestamp = '' if access_token.updated_at is None else access_token.updated_at.replace(
            microsecond=0, tzinfo=None)
        return str(access_token.pk) + str(login_timestamp) + str(timestamp)


token_generator = TokenGenerator()
