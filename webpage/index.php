<!DOCTYPE html>
<html>
    <head>
        <title>Heraeus data</title>
        <style>

            .button
            {

                background-color:red;
                
                border-color: black;
                
                text-align: center;
                
            }
            .button data
            {
                font-size: 100px;
                padding: 100px 150px;
            }
            .button script
            {
                font-size: 50px;
                padding: 50px 100px;
            }
        </style>
    </head>
    <body>
        <?php
            if(array_key_exists('execButton', $_POST))
            {
                pyCode();
            }
            function pyCode()
            {
                $command = escapeshellcmd(getData.py);
                $output = exec($command);
                echo $output;
            }
        ?>
        <h2>press this button to update the csv data (should be pressed each time before download)</h2>
        <form method="post">
            <input type="submit" name="exec" class="button" value = "execButton">
        </form>
        <h3>Below is a button that downloads and opens a csv file.</h3>
        <a href="data.php"><button class="button">Click for data!</button></a>
    </body>
</html>