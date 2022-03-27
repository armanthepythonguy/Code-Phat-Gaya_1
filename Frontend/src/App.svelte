<<<<<<< HEAD
<script>
	import { routes, Router } from 'svelte-hash-router';
	import Footer from "./Footer.svelte";
	import Nav from "./Nav.svelte";
	import Dash1 from "./Dash1.svelte";
	import Dash2 from "./Dash2.svelte";
	import Alink from "./Alink.svelte";
	import Login from "./Login.svelte";
	import Reg from "./Reg.svelte";
	routes.set({
		'/':Alink,
		'/dash1':Dash1,
		'/dash2':Dash2
	}) 
</script>
<main>
	<Reg/>
=======
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>



<main>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
	
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
            <input type="submit" value="Login">
            <div class="sign_uplink">
                Not a member? <a href="#">sign up</a>
            </div>
        </form>
    </div>
	
>>>>>>> 9ce945db0c34d06892534f1e31cc6c3c9008bb4b
</main>
<style>
<<<<<<< HEAD
	main{
		position: relative;
=======
	
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
        
>>>>>>> 9ce945db0c34d06892534f1e31cc6c3c9008bb4b
	}
	.foot{
		position: absolute;
		left: 0px;
		bottom: 0px;

	}
    .heading{
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
    input[type="submit"]{
        width: 5rem;
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

