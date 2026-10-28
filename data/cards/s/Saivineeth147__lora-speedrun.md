# Saivineeth147/lora-speedrun

⭐ 150 · Python · MIT · 推送 2026-09-12 · [GitHub](https://github.com/Saivineeth147/lora-speedrun) · 个人维护

**LoRA 微调竞速基准：固定任务与硬件的公开 wall-clock 排行榜**

面向小模型微调研究者的竞赛式基准（自述为“微调版 modded-nanogpt”）：设定两条固定赛道（GSM8K/Qwen2.5-1.5B、SQuAD/SmolLM2-1.7B），在 1× L40S 上比拼达到目标精度的训练 wall-clock。每个纪录需在 Modal 沙箱中换种子重跑 3 次验证，附带防篡改审计与 Claude 安全筛查。官方计时运行在 Modal L40S 上（Modal 免费额度可覆盖），本地 24GB 显卡可迭代但不计成绩。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两条冻结赛道：固定模型、数据、目标精度与硬件，以训练 wall-clock 计名次
- 纪录需 3× 换种子在断网 Modal 沙箱重跑验证，附 adapter 参数量与哈希审计
- 提供 submissions/TEMPLATE 与 CI 验证流程，PR + /verify 即可挑战
- 官方计时在 Modal L40S 免费沙箱进行，任何人可一条命令复验

## 适用场景

- 验证某个 LoRA/QLoRA 训练技巧在受控条件下是否真的更快
- 以竞赛形式寻找并公开可复现的微调加速技术
- 查阅各纪录的机制说明与被否定变体作为实验参考

## 场景标签

`模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L9: This is modded-nanogpt for fine-tuning: a
> L10: frozen task, frozen hardware, and a public leaderboard of wall-clock records. Every record is
> L21: ### Track 1 — GSM8K · Qwen2.5-1.5B · target ≥ 57.0% · 1× L40S

## 星数曲线

```mermaid
xychart-beta
    title "Saivineeth147/lora-speedrun 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 148 --> 150
    line [149, 149]
```

2026-10-18 149 → 2026-10-28 149（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e3da2bfa7a81` · [字段定义](../../DATASET.md)*
