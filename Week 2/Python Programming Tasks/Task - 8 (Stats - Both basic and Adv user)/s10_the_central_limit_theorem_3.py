# s10-the-central-limit-theorem-3

n = float(input())
pop_mean = float(input())
pop_std = float(input())
interval = float(input())
z_score = float (input())

sample_std = pop_std / (n ** 0.5)
print(round(pop_mean - sample_std * z_score,2))
print(round(pop_mean + sample_std * z_score,2))