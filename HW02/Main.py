data = 2,4,6,8,10
methods = (
  ("Arithmetic", lambda d: sum(d) / len(d)),
  ("Geometric", lambda d: (eval('*'.join(map(str, d)))) ** (1 / len(d))),
  ("Harmonic", lambda d: len(d) / sum(1 / x for x in d))
)

def analyze_methods(data_tuple, method_tuple):
  results = tuple((name, func(data_tuple)) for name, func in method_tuple)
  best_name, best_value = max(results, key=lambda item: item[1])
  return results, best_name, best_value

results, best_name, best_value = analyze_methods(data, methods)

print("Data:", data)
print("Result:")
for name, value in results:
  print("%s: %.6f" % (name, value))
print("Best result: %.6f (%s)" % (best_value, best_name))
