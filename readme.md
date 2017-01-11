## Dell support request creator

## Usage
dell_support.py [OPTIONS] SERVICE_TAG

SERVICE_TAG: Dell Service Tag consisting of 7 alphanumeric characters

## Dependencies
Firefox, Selenium and Click
'pip3 install selenium'
'pip3 install click'

## Contact information
Create 'form_details.py' containing your contact details/support information:

    # Primary contact
    company = ''
    address0 = ''
    address1 = ''
    city = ''
    country = ''    # 2 letter country code, eg: AU
    state = ''
    zip_code = ''
    primary_first_name = ''
    primary_last_name = ''
    primary_phone_number = ''
    primary_email = ''

    # Secondary contact
    secondary_first_name = ''
    secondary_last_name = ''
    secondary_phone_number = ''
    secondary_email = ''

    # Support details, examples provided
    problem_details = '900GB 10k SAS6 - hard drive predicted failure'
    error_message = 'Predictive failure reported'
    troubleshoot = 'Drive replaced with spare.'
    incident_type = 'Hard-Drive_Floppy_Zip-Drive'

## Incident types
Incident types can be:
    'Audio'
    'Audio_Speakers'
    'Battery'
    'BIOS'
    'CD-ROM'
    'Connection'
    'Damage'
    'Driver'
    'DVD_CD RW_CD ROM'
    'Fan_Temperature'
    'Fiber Channel'
    'Hard-Drive_Floppy_Zip-Drive'
    'iSCSI'
    'Keyboard_Mouse'
    'MemoryError'
    'Modem_FAX'
    'Monitor'
    'Network'
    'Network Adapter'
    'No Power'
    'OpenManage Software'
    'Operating System'
    'Other Dont Know'
    'Poor Performance'
    'Port Replicator'
    'Power Supply'
    'Printer_Scanner_Camera'
    'Processory Error'
    'Rack Hardware'
    'RAID'
    'Reboots_Locksup'
    'Tape Backup'
    'Update-Software BIOS'
    'Upgrade-Hardware'
    'Upgrade-Software'
    'Video'
    'VideoAdapter_LCD'

