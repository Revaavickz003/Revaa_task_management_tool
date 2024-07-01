# shop/views.py

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse

from frontend.models import *
from util.charts import weeks, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_week_dict

from django.shortcuts import render





def get_filter_options(request):
    grouped_purchases = TaskSheet.objects.annotate(project=ExtractYear("time")).values("year").order_by("-year").distinct()
    options = [purchase["year"] for purchase in grouped_purchases]

    return JsonResponse({
        "options": options,
    })



# date chart
@staff_member_required
def get_sales_chart(request, year):
    purchases = TaskSheet.objects.filter(time__year=year)
    grouped_purchases = purchases.annotate(price=F("item__price")).annotate(month=ExtractMonth("time"))\
        .values("month").annotate(average=Sum("item__price")).values("month", "average").order_by("month")

    sales_dict = get_week_dict()

    for group in grouped_purchases:
        sales_dict[weeks[group["month"]-1]] = round(group["average"], 2)

    return JsonResponse({
        "title": f"Sales in {year}",
        "data": {
            "labels": list(sales_dict.keys()),
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(sales_dict.values()),
            }]
        },
    })



# # Nothing
# @staff_member_required
# def spend_per_customer_chart(request, year):
#     purchases = Purchase.objects.filter(time__year=year)
#     grouped_purchases = purchases.annotate(price=F("item__price")).annotate(month=ExtractMonth("time"))\
#         .values("month").annotate(average=Avg("item__price")).values("month", "average").order_by("month")

#     spend_per_customer_dict = get_year_dict()

#     for group in grouped_purchases:
#         spend_per_customer_dict[months[group["month"]-1]] = round(group["average"], 2)

#     return JsonResponse({
#         "title": f"Spend per customer in {year}",
#         "data": {
#             "labels": list(spend_per_customer_dict.keys()),
#             "datasets": [{
#                 "label": "Amount ($)",
#                 "backgroundColor": colorPrimary,
#                 "borderColor": colorPrimary,
#                 "data": list(spend_per_customer_dict.values()),
#             }]
#         },
#     })


# @staff_member_required
# def payment_success_chart(request, year):
#     purchases = Purchase.objects.filter(time__year=year)

#     return JsonResponse({
#         "title": f"Payment success rate in {year}",
#         "data": {
#             "labels": ["Successful", "Unsuccessful"],
#             "datasets": [{
#                 "label": "Amount ($)",
#                 "backgroundColor": [colorSuccess, colorDanger],
#                 "borderColor": [colorSuccess, colorDanger],
#                 "data": [
#                     purchases.filter(successful=True).count(),
#                     purchases.filter(successful=False).count(),
#                 ],
#             }]
#         },
#     })


@staff_member_required
def complited_task_types_count(request, year):
    purchases = TaskSheet.objects.filter(time__year=year)
    grouped_purchases = purchases.values("payment_method").annotate(count=Count("id"))\
        .values("Task_Type", "count").order_by("payment_method")

    payment_method_dict = dict()

    for payment_method in TaskSheet.PAYMENT_METHODS:
        payment_method_dict[payment_method[1]] = 0

    for group in grouped_purchases:
        payment_method_dict[dict(TaskSheet.PAYMENT_METHODS)[group["payment_method"]]] = group["count"]

    return JsonResponse({
        "title": f"Payment method rate in {year}",
        "data": {
            "labels": list(payment_method_dict.keys()),
            "datasets": [{
                "label": "Count ($)",
                "backgroundColor": generate_color_palette(len(payment_method_dict)),
                "borderColor": generate_color_palette(len(payment_method_dict)),
                "data": list(payment_method_dict.values()),
            }]
        },
    })


def statistics_view(request):
    return render(request, "statistics.html", {})