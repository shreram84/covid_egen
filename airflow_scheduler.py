import pendulum
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta
local_tz = pendulum.timezone("America/New_York")


args={
        'owner': 'shreram,',
        'depends_on_past': False,
        'start_date': datetime(2019,10,17,0,0,0,tzinfo=local_tz),
        'retries':0,
        'trigger_rule':'all_success',
        'email_':['shreram@gmail.com'],
        'email_on_failure': True,
        'email_on_retry': False,
      
}

dag = DAG('COVID',catchup= False, default_args=args,schedule_interval='00 09 * * *')

# Generate your tasks

task1 = BashOperator(task_id='script1',bash_command='python3 covid.py',dag=dag)
task2 = BashOperator(task_id='script2',bash_command='python3 covid.py',dag=dag)
task3 = BashOperator(task_id='script3',bash_command='python3 covid.py',dag=dag)
task4 = BashOperator(task_id='script4',bash_command='python3 covid.py',dag=dag)
task5 = BashOperator(task_id='script5',bash_command='python3 covid.py',dag=dag)
task6 = BashOperator(task_id='Sscript6',bash_command='python3 covid.py',dag=dag)
task7 = BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task8 = BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task9 = BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task10 = BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task11 = BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task12= BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task13 = BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task14= BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task15= BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task16 = BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task17= BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task18= BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task19= BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)
task20= BashOperator(task_id='Sscript1',bash_command='python3 covid.py',dag=dag)

#multiple tasks can be organized using ">>". The airflow will sequentially run the tasks
task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7 >> task8 >> task9 >> task10 >> task11 >> task12 >> task13 >> task14 >> task15 >> task16 >> task17 >> task18 >> task19 >> task20
