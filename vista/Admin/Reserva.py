<!DOCTYPE html>
<html lang="es">
<head>
    <title>Reservas</title>

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
              <h2>Registro de reservas</h2>
            </center>
              <p>
                <table class="table table-bordered" id="dataTable" width="100%">

	            <tr>
	              <td>id_reserva</td>
	              <td>fecha_reserva</td>
	              <td>cantidad</td>
	              <td>precio_total</td>
	              <td>estado</td>
	              <td>observaciones</td>
	              <td>cliente</td>
	            </tr>

	            <?py 
	            $sql="SELECT * from reservas";
	            $result=mysqli_query($conexion,$sql);

	            while($mostrar=mysqli_fetch_array($result)){
	             ?>

	            <tr>
	              <td><?py echo $mostrar['id_reserva'] ?></td>
	              <td><?py echo $mostrar['fecha_reserva'] ?></td>
	              <td><?py echo $mostrar['cantidad'] ?></td>
	              <td><?py echo $mostrar['precio_total'] ?></td>
	              <td><?py echo $mostrar['estado'] ?></td>
	              <td><?py echo $mostrar['observaciones'] ?></td>
	              <td><?py echo $mostrar['cliente'] ?></td>
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