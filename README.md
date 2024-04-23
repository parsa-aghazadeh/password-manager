# نرم افزار مدیریت پسورد تحت CLI
این نرم افزار با دریافت شماره موبایل از طریق سامانه sms.ir یک کد 5 رقمی ارسال میکند، در صورتی که کاربر کد را بدرستی وارد کند از طریق وبکم به کمک کتابخانه opencv تصویر کاربر در فولدر storage و زیر فولدری با مقدار شماره موبایل کاربر ذخیره میگردد.
دیتابیس بکار رفته در این پروژه MySQL میباشد لذا اطلاعات لازم برای اتصال را در فایل database.py وارد نمایید.
برای ارسال sms میبایست در فایل Notifier.py کلید API و شماره خط دریافتی از سامانه sms.ir را وارد کنید.
توجه نمایید که تمامی پسورد ها در دیتابیس با رمزنگاری نگهداری میشوند و کلید رمزنگاری در فایل key.key ذخیره میشود، لذا پس از راه اندازی پروژه در حفظ و نگهداری از این کلید دقت کافی داشته باشید.
همچنین تمامی فعالیت ها توسط فایل Logger.py در فایلی با نام activity.log به شکل رخداد ذخیره میشوند.
ضمنا در این پروژه از کل عملیات CRUD استفاده شده است.

