try:
    from graphviz import Digraph
except ModuleNotFoundError:
    Digraph = None

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

print("----------------------------------")
print("DevSecOps Lifecycle Stages Generated")
for stage in stages:
    print(f"{stage:10s} -> {security_gates[stage]}")
print("----------------------------------")

if Digraph is None:
    print("Graphviz Python package is not available. Saving a text workflow summary instead.")
    with open("devsecops_lifecycle.txt", "w", encoding="utf-8") as file:
        for stage in stages:
            file.write(f"{stage} -> {security_gates[stage]}\n")
    print("Text workflow summary saved as devsecops_lifecycle.txt")
else:
    dot = Digraph(comment="DevSecOps Lifecycle", format="png")
    dot.attr(rankdir="LR", size="10,4")

    for i, stage in enumerate(stages):
        label = stage + "\n[" + security_gates[stage] + "]"
        dot.node(stage, label, shape="box", style="filled", fillcolor="lightblue")
        if i > 0:
            dot.edge(stages[i - 1], stage)

    dot.edge("Monitor", "Plan", label="Feedback Loop", style="dashed")

    try:
        dot.render("devsecops_lifecycle", cleanup=True)
        print("Diagram saved as devsecops_lifecycle.png")
    except Exception as error:
        print(f"Graphviz engine not available: {error}")
        with open("devsecops_lifecycle.txt", "w", encoding="utf-8") as file:
            for stage in stages:
                file.write(f"{stage} -> {security_gates[stage]}\n")
        print("Text workflow summary saved as devsecops_lifecycle.txt")
