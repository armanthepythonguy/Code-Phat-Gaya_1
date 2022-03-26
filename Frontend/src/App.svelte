<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>



<main>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
	
	<div class="center">
        <h1 class="heading">login</h1>
        <form method="post">
            <div class="text_field">
                <input type="text" required placeholder="Enter your username*">
                <label for=""></label>
            </div>
            <div class="text_field">
                <input type="password" required placeholder="Enter youe password*">
                <label for=""></label>
            </div>
            <div class="pass">forgot password?</div>
            <input type="submit" value="login">
            <div class="sign_uplink">
                not a member? <a href="#">sign up</a>
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
        	background: black;
        	height: 100vh;
        	overflow: hidden;
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
        width: 25%;
        padding: 0 5px;
        height: 30px;
        border-radius: 10px;
    }
    .text_field label{
        position: absolute;
        top: 50%;
        /* left: 5px; */
        color: #413d3d;
    }
    input[type="submit"]{
        width: 7%;
        /* height: 30px; */
        border: 1px solid #6d777e;
        background: #2691d9;
        border-radius: 10px;
        cursor: pointer;

    }
    .signup_link{
        margin: 30px 0;
        text-align: center;
        font-size: 16px;
        color: #a6a6a6;
}
.signup_link a{
  color: #2691d9;
  text-decoration: none;
}
.signup_link a:hover{
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
