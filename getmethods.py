import speech_recognition as sr

a = sr.Recognizer()

object_methods = [method_name for method_name in dir(a)
                  if callable(getattr(a, method_name))]
print(object_methods)