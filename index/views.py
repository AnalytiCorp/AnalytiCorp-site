from django.shortcuts import render
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from .forms import ContactForm

# Create your views here.
def about(request):
  return render(request, 'about.html')

def analyze(request):
  return render(request, 'analyze.html')

def automation(request):
  return render(request, 'automation.html')

def security(request):
  return render(request, 'security.html')

def course(request):
  return render(request, 'course.html')

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']
            
            # Configurações do e-mail
            msg = MIMEText(f'Nome: {first_name}\nEmpresa: {company}\nEmail: {email}')
            msg['Subject'] = "Contato do Website"
            msg['From']    = "corp.analyti@gmail.com"
            msg['To']      = "corp.analyti@gmail.com"

            # Configurações de conexão SMTP do Mailgun
            smtp_host = 'smtp.mailgun.org'
            smtp_port = 587
            username = 'corp.analyti@gmail.com'  # substitua pelo seu e-mail de domínio Mailgun
            password = '182ae380dfc1893a9413efe820cf244c-5d9bd83c-5e09f71e'  # substitua pela chave da API do Mailgun

            try:
                with smtplib.SMTP(smtp_host, smtp_port) as server:
                    server.login(username, password)
                    server.sendmail(msg['From'], msg['To'], msg.as_string())

                # Redirecionar para uma página de confirmação ou exibir uma mensagem de sucesso
                return render(request, 'confirmation.html')

            except Exception as e:
                # Lidar com qualquer exceção de envio de e-mail
                error_message = f"Erro ao enviar e-mail: {str(e)}"
                print(f"Erro ao enviar e-mail: {str(e)}")
                return render(request, 'error.html', {'error_message': error_message})

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
