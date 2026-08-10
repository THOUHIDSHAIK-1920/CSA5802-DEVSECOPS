from graphviz import Digraph

stages = ["Plan", "Code", "Build", "Test", "Release", "Deploy", "Operate", "Monitor"]

security_gates = {
    "Plan": "Threat Modelling",
    "Code": "SAST (Static Analysis)",
    "Build": "SCA (Dependency Scan)",
    "Test": "DAST (Dynamic Analysis)",
    "Release": "Container Image Scan",
    "Deploy": "IaC / Config Scan",
    "Operate": "Runtime Protection",
    "Monitor": "Continuous Auditing / SIEM"
}

dot = Digraph(comment="DevSecOps Lifecycle", format="png")
dot.attr(rankdir="LR", size="10,4")

for i, stage in enumerate(stages):
    label = f"{stage}\n[{security_gates[stage}]}"
    dot.node(stage, label, shape="box", style="filled", fillcolor="lightblue")
    if i > 0:
        dot.edge(stages[i - 1], stage)

dot.edge("Monitor", "Plan", label="Feedback Loop", style="dashed")
dot.render("devsecops_lifecycle", cleanup=True)

print("----------------------------------")
print("DevSecOps Lifecycle Stages Generated")
for stage in stages:
    print(f"{stage:10s} -> {security_gates[stage]}")
print("----------------------------------")
print("Diagram saved as devsecops_lifecycle.png")
