import json
import logging 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}") 
        repo_name = event['repository']['full_name']
        pull_request = event['pull_request']
        changed_files = []

        for commit in pull_request['commits']:
            for file in commit['added']:
                changed_files.append(f"Added: {file}")
            for file in commit['removed']:
                changed_files.append(f"Removed: {file}")
            for file in commit['modified']:
                changed_files.append(f"Modified: {file}")

        logger.info(f"Repository: {repo_name}")
        logger.info(f"Changed files: {changed_files}")

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully logged the changed files')
        }
    except Exception as e:
        logger.error(f"Error processing the event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing the request')
        }
