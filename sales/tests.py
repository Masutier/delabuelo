<div class="col-7 mx-auto">
    <div class="row">

        <div class="col-6 mx-auto">
            <h2>Ventas del ultimo dia</h2>
            <h3>Total Ventas = {{ totalDay }}</h3>
        </div>
        <div class="col-6 mx-auto ">
            <label for="vent">Exportar a Excel</label>
            <form action="{% url 'excelSales' %}" method="POST">
            {% csrf_token %}
                <select name="vent" id="vent">
                    <option value="D">Ventas del Dia</option>
                    <option value="W">Ventas Semana Pasada</option>
                    <option value="M">Ventas Ultimo Mes</option>
                </select>
                <button class="btn btn-outline-primary btn-sm" type="submit">Envia</button>
            </form>
        </div>
    </div>
</div>

