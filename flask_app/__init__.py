from flask import Flask, redirect, session, render_template

app = Flask(__name__)
app.secret_key="shooout"