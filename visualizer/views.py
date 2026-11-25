from django.shortcuts import render


def box_model(request):
    return render(request, 'visualizer/box_model.html', {'active_page': 'css_box_model'})


def flexbox(request):
    return render(request, 'visualizer/flexbox.html', {'active_page': 'flexbox'})


def css_grid(request):
    return render(request, 'visualizer/css_grid.html', {'active_page': 'css_grid'})


def positioning(request):
    return render(request, 'visualizer/positioning.html', {'active_page': 'css_positioning'})


def css_properties(request):
    return render(request, 'visualizer/css_properties.html', {'active_page': 'css_properties'})


def elements(request):
    return render(request, 'visualizer/elements.html', {'active_page': 'html_elements'})
