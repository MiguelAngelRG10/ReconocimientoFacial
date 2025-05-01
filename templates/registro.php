<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "usuarios";

// Conexión a la base de datos
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

$user = $_POST['username'];
$pass = $_POST['password'];

// Verificar si el usuario ya existe
$sql_check_user = "SELECT * FROM registros WHERE username = '$user'";
$result_user = $conn->query($sql_check_user);

if ($result_user->num_rows > 0) {
    echo "<script>
        alert('El usuario ya se encuentra registrado. Intenta con otro nombre de usuario.');
        window.location.href='registro.html';
    </script>";
} else {
    // Verificar si la contraseña ya existe
    $sql_check_pass = "SELECT * FROM registros WHERE password = '$pass'";
    $result_pass = $conn->query($sql_check_pass);

    // Insertar el usuario si pasa las verificaciones
    $sql_insert = "INSERT INTO registros (username, password) VALUES ('$user', '$pass')";

    if ($conn->query($sql_insert) === TRUE) {
        echo "<script>
                alert('Usuario registrado con éxito. Redirigiendo al login.');
                window.location.href='login.html';
            </script>";
    } else {
        echo "Error: " . $sql_insert . "<br>" . $conn->error;
    }
}

$conn->close();
