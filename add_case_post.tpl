Add a new case to the list:
<form action="/scoreevent/{{action}}" method="POST">

%# disp_table.tpl
<p>The items are as follows:</p>
%hdr=None
<table border="1">

  %for subr in rows:
   
%if not hdr:
  %  hdr=subr.keys()


    %for key in hdr:
      <th>{{key.title()}}</th>
    %end
%end
 <tr>
%result = subr['result']
%id = subr['id']
%round = subr['round']
%dog = subr['dog']
%dogname = subr['dogname']
%level = subr['level']
%judge = subr['judge']
<td>{{id}}</td>
<td>{{dog}}</td>
<td>{{round}}</td>
  <td><input type="text" size="5" maxlength="50" value="{{result}}" name="{{dog}}.{{round}}"></td>

<td>{{dogname}}</td>
<td>{{level}}</td>
<td>{{judge}}</td>



    </tr>
 %end
</table>


    <input type="submit" name="add" value="Add to the list">
</form>
