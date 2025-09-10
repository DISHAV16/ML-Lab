 def MCP_neuron(inputs, weights, threshold):
    total = sum(i*w for i, w in zip(inputs, weights))
    return 1 if total >= threshold else 0

# OR gate using MCP neuron
def OR_gate(x1, x2):
    return MCP_neuron([x1, x2], weights=[1, 1], threshold=1)

# AND gate using MCP neuron
def AND_gate(x1, x2):
    return MCP_neuron([x1, x2], weights=[1, 1], threshold=2)

print("OR Gate Truth Table")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} OR {b} = {OR_gate(a, b)}")

print("\nAND Gate Truth Table")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} AND {b} = {AND_gate(a, b)}")
