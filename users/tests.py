{% extends 'abuemp/layout2.html' %}
{% load static %}
{% block title %} {{ title }} {% endblock %}

{% block content %}
<div class="col-11 mx-auto">
    <div class="col-7 mx-auto mt-4 backs c">
        <form method="POST" action="{% url 'UserRegister' %}">
        {% csrf_token %}
            <div class="col-lg-11 mx-auto mt-4">
                <div class="col-md-5 mt-3 mb-3 mx-auto c">
                    <label>Usuario </label>
                    <input type="text" name="username" class="form-control">
                </div>
            </div>

            <div class="col-lg-11 mx-auto mt-4">
                <div class="row">
                    <div class="col-md-5 mt-3 mb-3 mx-auto c">
                        <label>Nombres </label>
                        <input type="text" name="first_name" class="form-control">
                    </div>

                    <div class="col-md-5 mt-3 mb-3 mx-auto c">
                        <label>Apellidos </label>
                        <input type="text" name="last_name" class="form-control">
                    </div>
                </div>
            </div>

            <div class="col-lg-11 mx-auto mt-4">
                <div class="col-md-5 mt-3 mb-3 mx-auto c">
                    <label>Email </label>
                    <input type="email" name="email" class="form-control">
                </div>
            </div>

            <div class="col-lg-11 mx-auto ">
                <div class="row">
                    <div class="col-md-5 mt-3 mb-3 mx-auto c">
                        <label>Contraseña </label>
                        <input type="password" name="password" class="form-control">
                    </div>

                    <div class="col-md-5 mt-3 mb-3 mx-auto c">
                        <label>Verificar Contraseña </label>
                        <input type="password" name="password2" class="form-control">
                    </div>
                </div>
            </div>

            <div class="col-lg-10 mx-auto mt-5 row">
                <div class="col-6 mb-5">
                    <div class="d-grid gap-2">
                        <a href="{% url 'home' %}" class="btn btn-danger">Cancel</a>
                    </div>
                </div>
                <div class="col-6 mb-5">
                    <div class="d-grid gap-2">
                        <input class="btn btn-primary" type="submit" value="Crear Usuario" />
                    </div>
                </div>
            </div>
        </form>

    </div>
</div>



<h2>Sign up</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Sign up</button>
    </form>

{% endblock content %}

