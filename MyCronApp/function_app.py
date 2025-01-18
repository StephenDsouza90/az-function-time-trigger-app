import azure.functions as func
import logging

app = func.FunctionApp()

@app.timer_trigger(schedule="0 0 10 1 * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def main(myTimer: func.TimerRequest):
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    # Add business logic here
