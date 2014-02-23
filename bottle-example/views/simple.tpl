%if name and age:
	<p>Your BioData</p>
    <h3>Hello {{name}}</h3>
    <h4>Age {{age}}!</h4>

%else:
    <p>Oops !! Name and/or Age empty :(</p>
%end