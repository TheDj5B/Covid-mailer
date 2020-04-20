import json
import requests
import urllib.request 
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




url = 'https://extreme-ip-lookup.com/json/'
info = json.loads(urllib.request.urlopen(url).read())
ip = info['query']
loc = info['country']
ccode = info['countryCode']
print(ip)
print(ccode)


response = requests.get("https://api.thevirustracker.com/free-api?countryTotal={0}".format(ccode))
response2 = requests.get("https://api.thevirustracker.com/free-api?global=stats")

def jprint(obj):
    text =json.dumps(obj, sort_keys=True, indent=4)   
    dic2=json.loads(text)   


    for data in dic2['results']:
        
          total_cases = data.get('total_cases')
          total_recovered = data.get('total_recovered')
          total_unresolved = data.get('total_unresolved')
          total_deaths = data.get('total_deaths')
          total_active_cases = data.get('total_active_cases')
          total_affected_countries = data.get('total_affected_countries')
          total_serious_cases = data.get('total_serious_cases')
          total_new_cases_td = data.get('total_new_cases_today')
          total_new_deaths_td = data.get('total_new_deaths_today')
          
    def jprint2(obj):
        text =json.dumps(obj, sort_keys=True, indent=4)   
        dic2=json.loads(text)   


        for data in dic2['countrydata']:
         count_cases = data.get('total_cases')
         count_recovered = data.get('total_recovered')
         count_deaths = data.get('total_deaths')
         count_active_Cases = data.get('total_active_cases')
         count_danger_rank = data.get('total_danger_rank')
         count_serious_cases = data.get('total_serious_cases')
         count_new_cases_today = data.get('total_new_cases_today')
          
        message = MIMEMultipart("alternative")
        message["Subject"] = email_subject
        message["From"] = email_from
        message["To"] = email_to
        
  
        body = "<html>"
        body += "<head>"
        body += "</head>"
        body += "<body>"
        body += '<center><span style="font-size: 50px;font-weight: bold;">Status of : {}</span><br</br>'.format(loc)
        body += "<table width='600px' border='1px solid black' padding='3px' class='col-md-6'>"
        body += "<tr><td colspan=6><center><span style='font-size: 40px;font-weight: bold;'>Total CASES</span></center></td></tr>"
        body += "<tr><td colspan=6><center><span style='font-size: 30px;font-weight: bold;'>{total_cases}</span><br><span style='font-size:13.5px'>Total Cases</span></center></td></tr>".format(
        total_cases=count_cases)

        body += "<tr><td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#8080FF'>+{new_cases}</span><br><span style='font-size:13.5px'>Active Cases</span></center></td>".format(
        new_cases=count_active_Cases)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#f5ad42'>{count_deaths}</span><br><span style='font-size:13.5px'>Deaths</span></center></td>".format(
        count_deaths=count_deaths)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#d9c43b'>{mild_condition}</span><br><span style='font-size:13.5px'>Recovered</span></center></td>".format(
        mild_condition=count_recovered)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{serious_critical}</span> <br><span style='font-size:13.5px'>Danger Rank </span></center></td>".format(
        serious_critical=count_danger_rank)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{count_serious_cases}</span> <br><span style='font-size:13.5px'>Serious Cases </span></center></td>".format(
        count_serious_cases=count_serious_cases)
       
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{count_new_cases_today}</span> <br><span style='font-size:13.5px'>New Deaths Today</span></center></td>".format(
        count_new_cases_today=count_new_cases_today)
        body += "</tr>"
        body += "</table>"
        body += "<table  width='600px' border='1px solid black' padding='3px'>"
        body += "<h3>Latest News </h3>: https://world.einnews.com/country/{0}".format(loc)
        body += "</table>"
        body += "<br>"
        body += "<br>"
        body += "<table  width='600px' border='1px solid black' padding='3px'>"
        body += "<tr><td colspan=4><center><span style='font-size: 40px;font-weight: bold;' >World Cases</span></center></td></tr>"
        body += "<tr><td colspan=4><center><span style='font-size: 30px;font-weight: bold;'>{closed_cases}</span><br><span style='font-size:13.5px'>Total World Cases</span></center></td></tr>".format(
        closed_cases=total_cases)
        body += "<tr><td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#8ACA2B'>{total_recovered}</span><br><span style='font-size:13.5px'>Recovered</span></center></td>".format(
        total_recovered=total_recovered)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{total_deaths}</span> <br><span style='font-size:13.5px'>Deaths</span></center></td>".format(
        total_deaths=total_deaths)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#8ACA2B'>{total_unresolved}</span><br><span style='font-size:13.5px'>Unresolved Cases</span></center></td>".format(
        total_unresolved=total_unresolved)
        body += "<tr><td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{total_active_cases}</span> <br><span style='font-size:13.5px'>Active Cases</span></center></td>".format(
        total_active_cases=total_active_cases)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#8ACA2B'>{total_affected_countries}</span><br><span style='font-size:13.5px'>Affected Countries</span></center></td>".format(
        total_affected_countries= total_affected_countries)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{total_serious_cases}</span> <br><span style='font-size:13.5px'>Total Serious Cases</span></center></td>".format(
        total_serious_cases=total_serious_cases)
       
        body += "<tr><td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:red '>{total_new_cases_td}</span> <br><span style='font-size:13.5px'>Total New Cases Today</span></center></td>".format(
        total_new_cases_td=total_new_cases_td)
        body += "<td width='200px'><center><span style='font-size: 24px;font-weight: bold; color:#8ACA2B'>{total_new_deaths_td}</span><br><span style='font-size:13.5px'>Total News Deaths Today</span></center></td>".format(
        total_new_deaths_td= total_new_deaths_td)
        body += "</tr>"
        body += "</table>"
        body += "<table  width='600px' border='1px solid black' padding='3px'>"
        body += "<iframe src='https://public.domo.com/cards/bWxVg' width='100%' height='600' marginheight='0' marginwidth='0' frameborder='0'></iframe>"    
        body += "</table>"
        body += "<br><br>"
        body += "Project Made by :Subarna Basnet |Website| : https://www.subarnabasnet.com.np</center>"
        body += "</body>"
        body += "</html>"

        body = MIMEText(body, "html", 'utf-8')
        message.attach(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
         server.login(email_from, email_password)
         server.sendmail(
            email_from, email_to, message.as_string()
         )
         server.quit()

         print('Email sent successfully.')

    jprint2(response.json()) 
            
if __name__ == '__main__':
 with open('config2git.json') as file:
  config = json.load(file)

  email_subject = config['email']['subject']
  email_from = config['email']['from']
  email_password = config['email']['password']
  '''email_to = input("Enter the mail :")'''
  email_to = config['email']['to']
       
        
       
            
jprint(response2.json())   


   
        
        
    
