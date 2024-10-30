from app import app, db
from flask import render_template, redirect, url_for
from app.models import Tarefas
from app.forms import TarefasForm

@app.route('/')
def lista_tarefas():
    tarefas = Tarefas.query.all()
    form = TarefasForm()
    print(tarefas)  
    return render_template('index.html', tarefas=tarefas, form=form)

@app.route('/adicionar/', methods=['GET', 'POST'])
def adicionar_tarefa():
    form = TarefasForm() 
    if form.validate_on_submit():  
        nova_tarefa = Tarefas(titulo=form.title.data, descricao=form.description.data)
        db.session.add(nova_tarefa)
        db.session.commit()
        return redirect(url_for('lista_tarefas'))
    return render_template('adicionar_tarefa.html', form=form)

@app.route('/atualizar/<int:tarefa_id>', methods=['GET', 'POST'])
def atualizar_tarefa(tarefa_id):
    tarefa = Tarefas.query.get_or_404(tarefa_id)
    form = TarefasForm(obj=tarefa)
    if form.validate_on_submit():
        tarefa.titulo = form.title.data  
        tarefa.descricao = form.description.data 
        db.session.commit()
        return redirect(url_for('lista_tarefas'))
    return render_template('atualizar_tarefa.html', form=form)

@app.route('/deletar/<int:tarefa_id>')
def deletar_tarefa(tarefa_id):
    tarefa = Tarefas.query.get_or_404(tarefa_id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('lista_tarefas'))

from flask import redirect, url_for, flash

@app.route('/concluir/<int:tarefa_id>', methods=['POST'])
def concluir_tarefa(tarefa_id):
    tarefa = Tarefas.query.get_or_404(tarefa_id)
    print(f"Tarefa antes da atualização: {tarefa.concluida}")  
    tarefa.concluida = True
    db.session.commit()
    print(f"Tarefa após a atualização: {tarefa.concluida}")  
    flash('Tarefa concluída com sucesso!', 'success')
    return redirect(url_for('lista_tarefas'))

