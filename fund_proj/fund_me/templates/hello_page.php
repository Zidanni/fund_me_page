{% extends "base.php" %}

{% block content %}
<?php

$host = "localhost";
$username = "zclerigo";
$password = "D3vT3ch545";
$database = "donations";

  


?>

<html>

<h1> WHATS UP {{name}}!!!!!</h1><br>

<form action="" method = "POST">{% csrf_token %}
    <label for="first_name">First Name:</label>
    <input type="text" id="first_name" name="first_name"><br><br>
    <label for="last_name">Last Name:</label>
    <input type="text" id="last_name" name="last_name"><br><br>
    <label for="quantity">How much ETH do you want to donate?:</label>
    <input type="number" step = "any" id="quantity" name="quantity" min="0"><br><br>
    <label for="quantity">Any Note?:</label>
    <input type="text" id="note" name="note"><br><br>
    <input type="submit" value = "Post">
</form>


<h1>THANK YOU FOR YOUR DONATION {{first_name}}!!!!!!</h1>
</html>


{% endblock content %}