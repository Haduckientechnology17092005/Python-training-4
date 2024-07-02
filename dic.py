dictTV ={
    "brand":"Samsung",
    "model":"QA85Q90T",
    "year":2020
}
print(dictTV)
print("year: ",dictTV["year"])
print("model: ",dictTV["model"])
print("year: ",dictTV.get("year"))
print("model: ",dictTV.get("model"))
if("model" in dictTV):
    print("model: ",dictTV["model"])
else:
    print("invalid")
