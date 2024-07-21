#!/bin/bash

# Variables
REMOTE_USER="ismo"
REMOTE_PASS="2359Koura@ismael"
REMOTE_HOST="localhost"
REMOTE_DB="cars_store"
DUMP_FILE="/path/to/backup.sql"

LOCAL_USER="ismo"
LOCAL_PASS="2359Koura@ismael"
LOCAL_DB="local_database_name"
LOCAL_DUMP_FILE="/local/path/to/backup.sql"

# Dump the remote database
ssh ${REMOTE_USER}@${REMOTE_HOST} "mysqldump -u ${REMOTE_USER} -p${REMOTE_PASS} ${REMOTE_DB} > ${DUMP_FILE}"

# Transfer the dump file to local machine
scp ${REMOTE_USER}@${REMOTE_HOST}:${DUMP_FILE} ${LOCAL_DUMP_FILE}

# Import the dump file into the local database
mysql -u ${LOCAL_USER} -p${LOCAL_PASS} ${LOCAL_DB} < ${LOCAL_DUMP_FILE}

# Cleanup (optional)
ssh ${REMOTE_USER}@${REMOTE_HOST} "rm ${DUMP_FILE}"
rm ${LOCAL_DUMP_FILE}

echo "Database transfer complete!"
