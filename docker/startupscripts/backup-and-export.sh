#!/bin/bash
set -e

REPO_DIR=~/dify
EXPORT_DIR=$REPO_DIR/dsl_exports
DROPBOX_UPLOADER=~/dropbox_uploader.sh  # path to your Dropbox CLI script

cd $REPO_DIR

# 1. Backup DB dump
pg_dump -U postgres -d dify > $REPO_DIR/dify_db_backup_$(date +%F).sql

# 2. Export workflows as DSL files
mkdir -p $EXPORT_DIR
psql -U postgres -d dify -Atc "SELECT id, graph FROM workflows;" | while IFS='|' read -r id graph; do
  echo "$graph" > "$EXPORT_DIR/workflow_${id}.dsl.json"
done

# 3. Git add & commit if changes exist
if ! git diff --quiet || ! git diff --cached --quiet; then
  git add .
  git commit -m "Auto backup and DSL export on $(date +'%Y-%m-%d %H:%M:%S')"
  git push origin main
fi

# 4. Upload backups and exports to Dropbox
$DROPBOX_UPLOADER upload $REPO_DIR/dify_db_backup_$(date +%F).sql /Backups/
$DROPBOX_UPLOADER upload -r $EXPORT_DIR /Backups/dsl_exports/

echo "Backup, export, git push, and Dropbox upload complete."
