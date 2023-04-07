%.zip:
	zip -r "KnutZuidema_$*_$(shell python scripts/get_parts.py $*).zip" $*
