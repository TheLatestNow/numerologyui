<script>
    export let grid = {};
  </script>
  
  <table>
    <tr>
      <td>{grid[4]}</td>
      <td>{grid[9]}</td>
      <td>{grid[2]}</td>
    </tr>
    <tr>
      <td>{grid[3]}</td>
      <td>{grid[5]}</td>
      <td>{grid[7]}</td>
    </tr>
    <tr>
      <td>{grid[8]}</td>
      <td>{grid[1]}</td>
      <td>{grid[6]}</td>
    </tr>
  </table>  

  <style>
    table {
        width: 100%;
        height: 100%;
        table-layout: fixed;
    }

    td {
        border: 1px solid #ccc;
        text-align: center;
        vertical-align: middle;
    }
</style>