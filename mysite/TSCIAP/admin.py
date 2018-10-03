from django.contrib import admin
from TSCIAP.models import SaleSummary, Comunidad, Imagen, Producto, Noticia, Video, InicioImagen, GaleriaImagen, ColaboraImagen, Valor, Politica, Somos, Vision, Mision, Colaborador, Contacto, Mensaje

# Register your models here.
admin.site.register(Comunidad)
admin.site.register(Imagen)
admin.site.register(Producto)
admin.site.register(Noticia)
admin.site.register(Video)
admin.site.register(GaleriaImagen)
admin.site.register(InicioImagen)
admin.site.register(ColaboraImagen)
admin.site.register(Valor)
admin.site.register(Politica)
admin.site.register(Somos)
admin.site.register(Vision)
admin.site.register(Mision)
admin.site.register(Colaborador)
admin.site.register(Contacto)
admin.site.register(Mensaje)

@admin.register(SaleSummary)
class SaleSummaryAdmin(ModelAdmin):
    change_list_template = "admin/sale_summary_change_list.html"
    date_hierarchy = "created"

    def get_next_in_date_hierarchy(request, date_hierarchy):
        if date_hierarchy + "__day" in request.GET:
            return "hour"
        if date_hierarchy + "__month" in request.GET:
            return "day"
        if date_hierarchy + "__year" in request.GET:
            return "week"
        return "month"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            "total": Count("id"),
            "total_sales": Sum("price"),
        }
        response.context_data["summary"] = list(
            qs
            .values("sale__category__name")
            .annotate(**metrics)
            .order_by("-total_sales")
        )

        response.context_data["summary_total"] = dict(
            qs.aggregate(**metrics)
        )
        summary_over_time = qs.annotate(
            period=Trunc(
                "created",
                "day",
                output_field=DateTimeField(),
            ),
        ).values("period")
        .annotate(total = Sum("price"))
        .order_by("period")
        summary_range = summary_over_time.aggregate(
            low=Min("total"),
            high=Max("total"),
        )
        high = summary_range.get("high", 0)
        low = summary_range.get("low", 0)
        response.context_data["summary_over_time"] = [{
            "period": x['period'],
            "total": x['total'] or 0,
            "pct": \
               ((x["total"] or 0) - low) / (high - low) * 100
               if high > low else 0,
        } for x in summary_over_time]
        period = get_next_in_date_hierarchy(
            request,
            self.date_hierarchy,
        )
        response.context_data["period"] = period
        summary_over_time = qs.annotate(
            period=Trunc(
                "created",
                period,
                output_field=DateTimeField(),
            ),
        ).values("period")
        .annotate(total=Sum("price"))
        .order_by("period")

        return response


    list_filter = (
        "device",
    )
