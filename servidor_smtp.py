import smtplib

servidor_email = smtplib.SMTP('smtp.gmail.com', 587)

print(servidor_email.starttls())

servidor_email.login("weidyane.study@gmail.com", 'rs')

remetente = 'weidyane.study@gmail.com'
destinatarios = ['gleison.batista@prozeducacao.com.br']

conteudo = 'ja ta na hora de ir embora'

servidor_email.sendmail(remetente, destinatarios, conteudo)

servidor_email.quit()