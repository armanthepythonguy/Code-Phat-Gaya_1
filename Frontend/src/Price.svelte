<script>

  let name = ""
  let _replyto = ""
  let msg = ""
  let result = ""
  async function doPost () {
    document.getElementById("submitBtn").classList.add("disabled")
    document.getElementById("submitBtn").innerHTML = "Sending..."
		fetch('https://formspree.io/f/xpzbqqaa', {
			method: 'POST',
			body: JSON.stringify({
				name,
				_replyto,
        msg
			}),
      headers: {
        'Accept': 'application/json'
      }
    }).then(response => {
      result = "Quote will be in your email !";
      document.getElementById("submitBtn").classList.remove("disabled")
      document.getElementById("submitBtn").innerHTML = "Send"
      this.reset()
    }).catch(error => {
      result = "There was an error!";
      document.getElementById("submitBtn").classList.remove("disabled")
      document.getElementById("submitBtn").innerHTML = "Send"
    });
  }
</script>
<div class="imgtop">
    <img src="img/contact.jpg" class="img_real" alt="contact_image">
    <div class="img-overlay">
      <form class="nav-prbl" on:submit|preventDefault={doPost}>
        <div class="container">
          <div class="row">
              <div class="content">
                <h3> Get a Quote <img src="https://img.icons8.com/flat-round/48/000000/quote.png" alt="quote_icon"/></h3>
                  <div class="input">
                    <div class="input-group">
                      <input type="name" class="form-control btn0" name="name" bind:value={name} placeholder="Your name" required>
                      <input type="email" class="form-control btn1" name="_replyto" bind:value={_replyto} placeholder="Your email" required>
                    <div class="input-group">
                      <textarea id="btn2" name="msg" rows="2" cols="85" class="form-control" bind:value={msg} placeholder="Suggest your ideal car with modifications 🚀" required></textarea>
                      <span class="input-btn">
                        <button class="btn text-center" id="submitBtn" type="submit">SUBMIT</button>
                      </span>
                    </div>
                  </div>
                  <div class="response">{result}</div>
                <br>
                <hr style="color: white;">
              </div>
            </div>
            <h4>Hate doing mails and doing quotation ?</h4><br>
            <p>Social Media Handles,</p>
            <p><a href="https://twitter.com/Chidam333" target="_blank" class="link-primary"><img src="https://img.icons8.com/color/48/000000/twitter--v1.png" alt="twitter icon"/></a></p>
            <p><b>ID: </b><a href="https://twitter.com/Chidam333" target="_blank" class="link-primary">@chidam333</a></p>
            </div>    
          </div>
      </form>
    </div>
</div>


<style>
    .nav-prbl{
      margin-top:5%;
    }
    .response{
      background: rgba(173, 255, 47,0.5);
      font-family: "roboto";
      border-radius: 17px;
      text-transform: lowercase;
      color: rgb(0, 29, 0);
      text-align: center;
      margin-top: 2% ;
    }
    .imgtop{
        position: relative;
    }
    .img_real{
        display: block;
        width: 100%;
        height: 900px;
        object-fit: cover;
        object-position: bottom;
    }
    .img-overlay{
        position: absolute;
        top: 0%;
        left: 0%;
        width: 100%;
        height: 100%;
        background: rgba(20, 34, 36, 0.8);
        display: grid;
        justify-content: center;
        align-content: center;
        grid-auto-flow: row;
        margin:0 auto;
        text-align: center;
    }
.row{
    padding-left:5%;
    padding-right: 5%;
    padding-top: 20%;
    padding-bottom: 20%;
}
.row .content{
    max-width: 650px;
    margin:0 auto;
    text-align: center;
}
.row .content h3{
    margin-bottom:40px;
    color: rgb(240, 214, 166);
}
.row .btn0{
    height: 50px;
    border-color: #68035b ;
    border: 3px solid #0ca3c9;
    font-family: "roboto" ;
    color: #67990a;
}
.row .btn1{
    height: 50px;
    border-color: #68035b ;
    border: 3px solid #0ca3c9;
    font-family: "roboto" ;
    color: #67990a;
}
.row .btn0:focus{
    border: 3px solid rgb(223, 103, 103);
    color:black;
}
.row .btn1:focus{
    border: 3px solid rgb(223, 103, 103);
    color:black
}
.row #btn2{
    height: 50px;
    border-color: #68035b ;
    border: 3px solid #0ca3c9;
    font-family: "roboto" ;
    color: #67990a;
}
.row #btn2:focus{
    border: 3px solid rgb(223, 103, 103);
    color:black;
}
.row .content .btn{
    height: 50px;
    border-radius: 0;
    background-color: rgb(0, 100, 75) ;
    padding-right: 40px;
    padding-left: 40px;
    font-family: "roboto";
    color: wheat;
}
.row .content .btn:focus{

    background-color: rgb(153, 106, 4);
    border: 3px solid black;
}
.row h4{
  color: rgb(240, 214, 166);
  font-family: "ele";
  word-spacing: 0.6rem;
  font-weight: 900;
}
.row p{
  color: rgb(198, 248, 248);
  font-family: "robo";
  font-size: 25px;
}
</style>