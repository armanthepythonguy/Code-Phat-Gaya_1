<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>



<main>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
	
	<div class="center">
        <h1 class="heading">Register</h1>
        <form method="post">
            <div class="text_field">
                <input type="text" required placeholder="Enter your name*">
                <label for=""></label>
            </div>
            <div class="text_field">
                <input type="password" required placeholder="Enter your email*">
                <label for=""></label>
            </div>
            <div class="text_field">
                <input type="password" required placeholder="Name of the institution*">
                <label for=""></label>
            </div>
            
            <label class="label" for="bdaymonth">Year of graduation</label>
            <input type="number" id="" name="graduation year">
            <div class="radio">
                Gender: Male <input type="radio" name="gender" id=""> Female <input type="radio" name="gender" id="">
            </div>
            
            
            <input type="submit" value="Register">
            
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
    

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
        
	}
    input[type="number"]{
        width: 10rem;
        padding: 0 5px;
        height: 30px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px wheat;
        background-color:wheat;
    }
    .radio{
        color: wheat;
        padding: 1rem;
    }
    label{
        color: wheat;

    }

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
    .heading{
        color: wheat;
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
  



</style>

