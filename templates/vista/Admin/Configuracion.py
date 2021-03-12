<!DOCTYPE html>
<html lang="es">
<head>
<title>Configuracion</title>


<?py include '../partials/headA.py';?>

<?py include '../partials/menuA.py';?>

</br>
</br>

<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row featurette">
            <img src="../../assets/icon/1.png" width="50" height="50">
            <?py echo $_SESSION["usuario"]["nombre"]; ?>
            <a class="badge badge-info">
                <?py echo $_SESSION["usuario"]["privilegio"] == 1 ? 'Admin' : 'Cliente'; ?>
            </a>
        </div>
    </div>
</div>

<?py include '../partials/footerA.py';?>