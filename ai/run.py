import os
from app import app
# from manage import manager
# from app import db
print("                            _ooOoo_               ")
print("                           o8888888o               ")
print("                           88  .  88              ")
print("                           (| -_- |)                   ")
print("                            O\\ = /O                    ")
print("                        ____/`---'\\____               ")
print("                      .   ' \\| |// `.             ")
print("                       / \\||| : |||// \\          ")
print("                     / _||||| -:- |||||- \\          ")
print("                       | | \\\\\\ - /// | |            ")
print("                     | \\_| ''\\---/'' | |           ")
print("                      \\ .-\\__ `-` ___/-. /           ")
print("                   ___`. .' /--.--\\ `. . __            ")
print("                ."" '< `.___\\_<|>_/___.' >'"".         ")
print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |     ")
print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /     ")
print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
print("                            `=---='  ")
print("  ")
print("         ......................阿弥陀佛.......................  ")

# set FLASK_APP=app.py


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'), host=os.getenv('HOST'), port=os.getenv('PORT'))