 class="badge badge-light"<br/>
<br/>

<div>
  <nav class="navbar navbar-light navbar-expand-lg fixed-top" style="background-color: #009BDB;">
    <a href="../usuario.py" class="navbar-brand">
    <img src="../../assets/icon/Logo.png" width="40" height="40" alt="HSD PLUS"></a>
    <a class="badge badge-light" style="color: #000000">
        <?py echo $_SESSION["usuario"]["privilegio"] == 1 ? 'Admin' : 'Cliente'; ?>
    </a>
   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
          &nbsp;
          &nbsp;
          &nbsp;
          <a href="../usuario.py" class="nav-link" style="color: #ffffff;">Inicio
          </a>
          &nbsp;
          &nbsp;
          &nbsp;
          <a href="Catalogo.py" class="nav-link" style="color: #ffffff;">Catalogo
          </a>
          &nbsp;
          &nbsp;
          &nbsp;
          <a href="ConsultarCompras.py" class="nav-link" style="color: #ffffff;">Consultar Compras
          </a>
          &nbsp;
          &nbsp;
          &nbsp;
          <a href="reservar.py" class="nav-link" style="color: #ffffff;">Reservaciones
          </a>
          &nbsp;
          &nbsp;
          &nbsp;
        </li>
      </ul>

      <ul class="nav navbar-left navbar-top-links">
        <li class="dropdown navbar-inverse">
          <div>
            <button type="button" class="btn btn-link" >
              <a href="../Error404.py"  >
                <img src="../../assets/icon/ingles.png" width="40" height="40" alt="">
              </a>
            </button>
          </div>
        </li>
      </ul>


      <ul class="nav navbar-right navbar-top-links">
        <li class="dropdown navbar-inverse">
          <button  class="btn btn-light" class="btn btn-sec"  data-toggle="dropdown" aria-haspopup="false" aria-expanded="false">
              <a >
                  <img src="../../assets/icon/Usuario.png" width="30" height="30">
                  <?py echo $_SESSION["usuario"]["nombre"]; ?>
              </a>
          </button>
          <ul class="dropdown-menu dropdown-user">
              <li><a href="../error500.py" class="badge badge-light" style="color: #000000;"><i class="fa fa-user fa-fw"></i>Usuario</a></li>
              <li><a href="../Error404.py" class="badge badge-light" style="color: #000000;"><i class="fa fa-gear fa-fw"></i> Ajustes</a></li>
              <li><a href="../cerrar-sesion.py" class="badge badge-light" style="color: #000000;"><i class="fa fa-sign-out fa-fw"></i>Cerrar Sesión</a></li>
          </ul>
        </li>
      </ul>

    </div>
  </nav>
</div>