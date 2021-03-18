<?php

header('Content-Type: text/csv; charset=UTF-8');
header('Content-Disposition: attachment; filename=Data.csv');
$csv = 'example.csv';
readfile($csv);

?>