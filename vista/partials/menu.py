<nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Login con py</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="index.py">Principal</a></li>
            <?py if (!isset($_SESSION["usuario"])) {?>
            <li><a href="login.py">Login</a></li>
            <li><a href="registro.py">Registro</a></li>
            <?py } else {
    ?>
              <?py if ($_SESSION["usuario"]["privilegio"] == 1) {?>
              <li><a href="admin.py">Admin</a></li>
              <?py } else {?>
              <li><a href="usuario.py">Usuario</a></li>
            <?py }

}?>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
