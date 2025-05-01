<?php
session_start();
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "usuarios";

// Conexión a la base de datos
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Verifica si se envió el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = ($_POST['password']);
    
    // Verifica si el usuario y la contraseña coinciden
    $sql = "SELECT * FROM registros WHERE username='$user' AND password='$pass'";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        echo "<script>
            alert('Inicio de sesión exitoso.');
            window.location.href='index.html';
        </script>";
    } else {
        echo "<script>
            alert('Usuario o contraseña incorrectos.');
            window.location.href='login.html';
        </script>";
    }
}

$conn->close();
?>
