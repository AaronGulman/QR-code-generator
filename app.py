import qrcode 

def generate_qr_code(url):
        
        qr = qrcode.QRCode(
		version = 1,
  		error_correction= qrcode.constants.ERROR_CORRECT_L,
    		box_size=10,
		border=4,
	)
        
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img
        
url = input("Enter your url: ")
new_qr_code = generate_qr_code(url)
filename = "new_qr_code.png"
new_qr_code.save(filename)
