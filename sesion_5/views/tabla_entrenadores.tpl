<table style="width:100%">
    <tr>
        <th>Nombre</th>
        <th>Sexo</th>
    </tr>
    % for row in it:
    <tr>
        <td style="color:red">{{row[1]}}</td>
        <td>{{row[2]}}</td>
    <tr>
    %end
</table>