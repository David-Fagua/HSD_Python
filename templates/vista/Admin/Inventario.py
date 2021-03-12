<!DOCTYPE html>
<html lang="es">
<head>
    <title>Inventario General</title>

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
              <h2>Inventario General</h2>
            </center>
              <p>
                <table class="table table-bordered" id="dataTable" width="100%">

				<tr>
					<td>id_articulo</td>
					<td>nombre</td>
					<td>fecha_entrada</td>
					<td>preciode_compra</td>
					<td>disponibilidad</td>
					<td>peso_libra</td>
					<td>cantidad_unitaria</td>
					<td>color</td>
					<td>estado</td>
					<td>proveedor</td>
					<td>responsable</td>
				</tr>

				<?py 
				$sql="SELECT * from inventario_general";
				$result=mysqli_query($conexion,$sql);

				while($mostrar=mysqli_fetch_array($result)){
				 ?>

				<tr>
					<td><?py echo $mostrar['id_articulo'] ?></td>
					<td><?py echo $mostrar['nombre'] ?></td>
					<td><?py echo $mostrar['fecha_entrada'] ?></td>
					<td><?py echo $mostrar['preciode_compra'] ?></td>
					<td><?py echo $mostrar['disponibilidad'] ?></td>
					<td><?py echo $mostrar['peso_libra'] ?></td>
					<td><?py echo $mostrar['cantidad_unitaria'] ?></td>
					<td><?py echo $mostrar['color'] ?></td>
					<td><?py echo $mostrar['estado'] ?></td>
					<td><?py echo $mostrar['proveedor'] ?></td>
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