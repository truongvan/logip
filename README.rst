Website cập nhật ip
===================

.. image:: https://travis-ci.org/truongvan/logip.svg?branch=master
    :target: https://travis-ci.org/truongvan/logip
    
.. image:: https://coveralls.io/repos/github/truongvan/logip/badge.svg?branch=master
    :target: https://coveralls.io/github/truongvan/logip?branch=master

Website này dựa trên nền django. Chức năng chính là tự cập nhật ip của bất kỳ truy cập nào.

Đường dẩn để cập nhật ip:
https://example.com/update/?access_id=<uuid>&access_token=<token>

Đường dẩn để kiểm tra ip vừa cập nhật mới nhất:
https://example.com/?access_id=<uuid>

Với:

* <uuid> là id của cập nhật
* <token> là token bắt được để cập nhật ip

Cài logip trên heroku
---------------------
#. Đăng ký tài khoản trên github và Heroku
#. Sao chép mã nguồn này vào tài khoản Github của bạn
#. Link mã nguồn bạn vừa sao chép vào heroku
#. thêm `DJANGO_SETTINGS_MODULE=config.settings.production` vào Settings/Config Vars
#. Vào Resources tạo `Heroku Postgres` và liên kết vào 'app' bạn vừa tạo trên Heroku
#. Để tạo uuid và token mới, bạn vào 'More/Run Console' và nhập './src/manage.py new_token' vào ô trống và bấm `Run`

Hoặc bạn có thể gửi email đến tôi để tạo uuid trên heroku tôi đang dùng.
