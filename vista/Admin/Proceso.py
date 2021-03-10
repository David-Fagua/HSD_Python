<!DOCTYPE html>
<html lang="es">
<head>
    <title>Producto en Proceso</title>

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
              <h2>Producto en Proceso</h2>
            </center>
              <p>
                <table class="table table-bordered" id="dataTable" width="100%">
				<tr>
					<td>id_proceso</td>
					<td>fecha proceso</td>
					<td>estado</td>
					<td>articulo_inicial</td>
					<td>articulo_inicial2</td>
					<td>producto final</td>
					<td>responsable</td>
				</tr>

				<?py 
				$sql="SELECT * from producto_proceso";
				$result=mysqli_query($conexion,$sql);

				while($mostrar=mysqli_fetch_array($result)){
				 ?>

				<tr>
					<td><?py echo $mostrar['id_proceso'] ?></td>
					<td><?py echo $mostrar['fecha_proceso'] ?></td>
					<td><?py echo $mostrar['estado'] ?></td>
					<td><?py echo $mostrar['articulo_inicial'] ?></td>
					<td><?py echo $mostrar['articulo_inicial2'] ?></td>
					<td><?py echo $mostrar['producto_final'] ?></td>
					<td><?py echo $mostrar['responsable'] ?></td>
				</tr>
			<?py 
			}
			 ?>
			</table>
	   		</p>
          </div>
      </div>
    </div>
  <div class="col-md-1">
  </div>
</div>

<?py include '../partials/footerA.py';?>