from flask import redirect, flash

class authenticationController:
    def login(form):
        flash(f"o usuario {form.username.data} faz login, lembrar={form.remember_me.data}")
        usuario = {
            'name': form.username.data
        }
        return redirect('/')
