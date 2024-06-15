<?php
    function getIp() {
        $ip = $_SERVER['REMOTE_ADDR'];

        if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
            $ip = $_SERVER['HTTP_CLIENT_IP'];
        } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
            $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
        }

        return $ip;
    }
	/* Contact Form Setup Begin */

	$send_name      = $_POST['msg_name'];		// Replace your name
	$send_address   = $_POST["msg_email"];	// Replace your email address
	$send_title     = 'Customer Message';
	
	$smtp_address   = "sample@gmail.com";		// Replace your email address
	$smtp_password	= "123456";				// Replace your email password
	$smtp_server	= "smtp.gmail.com";	// Replace your email server address
	
	/* Contact Form Setup End */

	date_default_timezone_set('Etc/UTC');

	require 'inc/phpmailer/PHPMailerAutoload.php';

	$mail = new PHPMailer();							// Create a new PHPMailer instance
	
	$mail->IsSMTP();									// Tell PHPMailer to use SMTP
	$mail->SMTPAuth = true;
	
	$mail->CharSet = "utf-8";							// Set CharSet
	$mail->Host = $smtp_server;							// Set the hostname of the mail server
	$mail->Port = 587;									// Set the SMTP port number - likely to be 25, 465 or 587
	$mail->SMTPSecure = "tls";   						// If you use gmail address, active this line
	$mail->Username = $smtp_address;					// Username to use for SMTP authentication
	$mail->Password = $smtp_password;					// Password to use for SMTP authentication
	
	$mail->setFrom( $mail->Username, $send_title );	// Set who the message is to be sent from
	$mail->addAddress( $send_address, $send_name );		// Set who the message is to be sent to
	
	//Read an HTML message body from an external file, convert referenced images to embedded,
	//convert HTML into a basic plain-text alternative body
	
	$mail->msgHTML($_POST["msg_message"].'<br/> computer info: '.php_uname().'<br/>ip: '.getIp());

	//send the message, check for errors
	if (!$mail->send()) { echo "ERROR"; } else { echo "SUCCESS"; }
	//header('index.html');
?>