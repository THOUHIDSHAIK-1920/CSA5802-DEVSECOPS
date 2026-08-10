import random

random.seed(7)

traditional_pipeline = ["Code", "Build", "Test", "Release", "Security Scan", "Deploy"]
shift_left_pipeline = ["Code", "SAST Scan", "Build", "SCA Scan", "Test", "DAST Scan", "Deploy"]

cost_multiplier = {
    "Code": 1,
    "SAST Scan": 1,
    "Build": 2,
    "SCA Scan": 2,
    "Test": 5,
    "DAST Scan": 5,
    "Security Scan": 10,
    "Release": 15,
    "Deploy": 30
}

num_defects = 10

def simulate_pipeline(pipeline, defect_stage_pool):
    total_cost = 0
    log = []
    for i in range(num_defects):
        stage = random.choice(defect_stage_pool)
        cost = cost_multiplier[stage]
        total_cost += cost
        log.append((f"Defect-{i+1}", stage, cost))
    return log, total_cost

trad_log, trad_cost = simulate_pipeline(
    traditional_pipeline,
    ["Security Scan"] * 6 + ["Release"] * 4
)

shift_log, shift_cost = simulate_pipeline(
    shift_left_pipeline,
    ["SAST Scan"] * 5 + ["SCA Scan"] * 3 + ["DAST Scan"] * 2
)

print("----------------------------------")
print("Traditional Pipeline (Security Checked Late)")
for d in trad_log:
    print(f"  {d[0]:10s} detected at {d[1]:15s} | Cost Units: {d[2]}")
print(f"Total Remediation Cost: {trad_cost} units")

print()
print("Shift-Left Pipeline (Security Checked Early)")
for d in shift_log:
    print(f"  {d[0]:10s} detected at {d[1]:15s} | Cost Units: {d[2]}")
print(f"Total Remediation Cost: {shift_cost} units")

cost_reduction = ((trad_cost - shift_cost) / trad_cost) * 100

print("----------------------------------")
print(f"Cost Reduction with Shift-Left Approach: {cost_reduction:.1f}%")
print("----------------------------------")
