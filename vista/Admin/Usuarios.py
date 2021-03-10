<!DOCTYPE html>
<html lang="es">
<head>
    <title>Usuarios</title>

<?py include '../partials/headA.py';?>

<?py include '../partials/menuA.py';?>

<?py 

	$conexion=mysqli_connect('localhost','david','qwerty12','hsd_plus');

 ?>

</br>
</br>

<br></br>

<div id="body" class="row">
  <div class="col-md-1">
  </div>
    <div class="col-md-10">

      <div class="card mb-3">
          <div class="table-responsive">
            <center>
              <h2>Usuarios</h2>
            </center>
              <p>
                <table class="table table-bordered" id="dataTable" width="100%">
				<tr>
					<td>id</td>
					<td>nombre</td>
					<td>usuario</td>
					<td>email</td>
					<td>password</td>
					<td>privilegio</td>	
					<td>fecha_registro</td>	
				</tr>

				<?py 
				$sql="SELECT * from usuarios";
				$result=mysqli_query($conexion,$sql);

				while($mostrar=mysqli_fetch_array($result)){
				 ?>

				<tr>
					<td><?py echo $mostrar['id'] ?></td>
					<td><?py echo $mostrar['nombre'] ?></td>
					<td><?py echo $mostrar['usuario'] ?></td>
					<td><?py echo $mostrar['email'] ?></td>
					<td><?py echo $mostrar['password'] ?></td>
					<td><?py echo $mostrar['privilegio'] ?></td>
					<td><?py echo $mostrar['fecha_registro'] ?></td>
				</tr>
			<?py 
			}
			 ?>
			</table>
	  		</p>
          </div>
      </div>
    </div>
  <div class="col-md-3">
  </div>
</div>

<?py include '../partials/footerA.py';?>