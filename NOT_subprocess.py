"""here we're learning to call externall commands using the subprocess module"""

"""YOU SHOULD NEVER CALL THIS FILE SUBPROCESS.PY!!!! THIS CAUSES OTHER MODULES WHO NEED IT IMPORT IT AND FAIL!!!!""""


# note you need to be using shell=True to pass in arguments;
# however note that that's a security hazard if you're accepting untrusted input
import subprocess
subprocess.run('ls -la', shell=True)

# alternatively
subprocess.run(['ls', '-la'])

# if we wanted to capture what comes out rather than just sending it to python console
print('-'*100)
output1 = subprocess.run(['ls', '-la'], capture_output=True)
# note1 - we need to add .stdout at the end
# note2 - we need to add .decode() at the end because it's captured as bytes
print(output1.stdout.decode())

# lets write the above to a file
with open('recording_ls.txt', 'w') as f:
    output1 = subprocess.run(['ls', '-la'], capture_output=True)
    f.write(output1.stdout.decode())

# we can be smart about how we check for errors
# intentionally passing wrong filename
output2 = subprocess.run(['ls', '-la', 'fake_filename'], capture_output=True)

# returncode == 0 means no errors
if output2.returncode == 0:
    print('hooray')
else:
    print('nooooo')


# lets concatenate two commands together
c1 = subprocess.run(['cat', 'dogz.txt'], capture_output=True)
print(c1.stdout)
c2 = subprocess.run(['rg', '-i', 'inko'], capture_output=True, input=c1.stdout)
print(c2.stdout)

# alternative
c3 = subprocess.run('cat dogz.txt | rg -i inko', capture_output=True, shell=True)
print(c3.stdout)
