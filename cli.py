if __name__ == '__main__':

    from cookiecutter.prompt import read_user_variable, read_user_choice, read_repo_password
    from cookiecutter.main   import cookiecutter

    context = {}

    context['project_name']                = read_user_variable('project_name', 'my_project_name')
    context['django_template']             = read_user_choice('django_template', ['django'])
    context['db_backend']                  = read_user_choice('db_backend', ['mysql', 'postgresql'])
    context['db_password']                 = read_repo_password('db_password')
    context['docker_compose_file_version'] = read_user_variable('docker_compose_file_version', '3.8')

    if context['db_backend'] == 'mysql':

        context['db_user'] = 'root'

    elif context['db_backend'] == 'postgresql':

        context['db_user'] = 'postgres'

    repo       = 'https://github.com/otto-torino/webapp-boilerplate/'
    template   = 'templates/base'
    output_dir = '.'

    cookiecutter(repo, no_input=True, extra_context=context, directory=template, output_dir=output_dir)

    template   = '/'.join(['templates', context['django_template']])
    output_dir = '/'.join([output_dir, context['project_name']])

    cookiecutter(repo, no_input=True, extra_context=context, directory=template, output_dir=output_dir)