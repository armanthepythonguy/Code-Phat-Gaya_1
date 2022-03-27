<script>
    import Router from 'svelte-hash-router';
</script>
<main>	
	<div class="center">
        <h1 class="heading">Login</h1>
        <form method="post">
            <div class="text_field">
                <input type="text" required placeholder="Enter your username*">
                <label for=""></label>
            </div>
            <div class="text_field">
                <input type="password" required placeholder="Enter your password*">
                <label for=""></label>
            </div>
            <div class="pass">forgot password?</div>
            <a class="logbtn" href="#/alink">login</a><Router/>
            <div class="sign_uplink">
                Not a member? <a href="#">sign up</a>
            </div>
        </form>
    </div>
	
</main>

<style>
	
	main {
		text-align: center;
		/* padding: 1em; */
		max-width: 240px;
		margin: 0 ;
        padding: 0 ;
        background: linear-gradient( black,rgb(180, 154, 38));
        height: 100vh;
        overflow: hidden;
	}
    a {
        color: #2691d9;
    }

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
        
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
    .heading{
        font-family: "samarkan";
        color: wheat;
    }
    .form{
        padding: 0 40px;
    }
    .text_field{
        position: relative;
        
        margin: 30px 0;
    }
    .text_field input{
        width: 20rem;
        padding: 0 5px;
        height: 30px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px wheat;
        background-color:wheat;
    }
    .text_field label{
        position: absolute;
        top: 50%;
        /* left: 5px; */
        color: #413d3d;
    }
    .logbtn{
        color: wheat;
        text-decoration: none;
        font-family: "roboto";
        padding: 0.5rem 2rem;
        /* height: 30px; */
        border: 1px solid #6d777e;
        background: #2691d9;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 2px 2px 5px wheat;
        height: 2.5rem;
        font-size: 1.2rem;

    }
    .sign_uplink{
        margin: 30px 0;
        text-align: center;
        font-size: 16px;
        color: #a6a6a6;
}
.sign_uplink {
  color: #2691d9;
  text-decoration: none;
}
.sign_uplink a:hover{
  text-decoration: underline;
}
.pass{
  margin: -5px 0 20px 5px;
  color: wheat;
  cursor: pointer;
}
.pass:hover{
  text-decoration: underline;
}
</style>
