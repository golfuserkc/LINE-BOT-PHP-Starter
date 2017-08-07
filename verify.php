<?php
$access_token = 'V1W7Nva5xxPQJaJvLxj2lUFoHR8QXrhfjHvN343H2JWr0+Q6HphNbRBG/KB8TiIK2ziMKLIo5BwRWT9dwSKMMzApjKgPQCrVuF5yWkwcy9YFory4qL7HwAeVBRRWgYX40ky4kqrc0VXkbrRvhXAgiQdB04t89/1O/w1cDnyilFU=';

$url = 'https://api.line.me/v1/oauth/verify';

$headers = array('Authorization: Bearer ' . $access_token);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
$result = curl_exec($ch);
curl_close($ch);

echo $result;