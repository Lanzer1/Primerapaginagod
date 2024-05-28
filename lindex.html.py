<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seré buen programador</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            font-family: Arial, sans-serif;
        }
        h1 {
            margin-bottom: 20px;
        }
        .buttons {
            display: flex;
            gap: 20px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        button:disabled {
            cursor: not-allowed;
        }
    </style>
</head>
<body>

    <h1>Seré buen programador</h1>
    <div class="buttons">
        <button onclick="alert('¡Claro que sí, sigue trabajando duro!')">Sí</button>
        <button disabled>No</button>
    </div>

</body>
</html>