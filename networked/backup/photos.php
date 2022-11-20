<html>
<head>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-0lax{text-align:left;vertical-align:top}
@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
</head>
<body>
Welcome to our awesome gallery!</br>
See recent uploaded pictures from our community, and feel free to rate or comment</br>
<?php
require '/var/www/html/lib.php';
$path = '/var/www/html/uploads/';
$ignored = array('.', '..', 'index.html');
$files = array();

$i = 1;
echo '<div class="tg-wrap"><table class="tg">'."\n";

foreach (scandir($path) as $file) {
  if (in_array($file, $ignored)) continue;
  $files[$file] = filemtime($path. '/' . $file);
}
arsort($files);
$files = array_keys($files);

foreach ($files as $key => $value) {
  $exploded  = explode('.',$value);
  $prefix = str_replace('_','.',$exploded[0]);
  $check = check_ip($prefix,$value);
  if (!($check[0])) {
    continue;
  }
  // for HTB, to avoid too many spoilers
  if ((strpos($exploded[0], '10_10_') === 0) && (!($prefix === $_SERVER["REMOTE_ADDR"])) ) {
    continue;
  }
  if ($i == 1) {
    echo "<tr>\n";
  }

echo '<td class="tg-0lax">';
echo "uploaded by $check[1]<br>";
echo "<img src='uploads/".$value."' width=100px>";
echo "</td>\n";


  if ($i == 4) {
    echo "</tr>\n";
    $i = 1;
  } else {
    $i++;
  }
}
if ($i < 4 && $i > 1) {
    echo "</tr>\n";
}
?>
</table></div>
</body>
</html>
