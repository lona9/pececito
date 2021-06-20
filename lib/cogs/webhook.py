from dhooks import Webhook

hook = Webhook("https://discord.com/api/webhooks/855557319211089970/M7_qjVMl7ZrEfgTt0ThrxnzCFq8j7e4iTJngCj-Ins7iZkV-IfFXEuLYPMZW5dkGnVI7")

data = input("Enter something: ")

hook.send(data)
