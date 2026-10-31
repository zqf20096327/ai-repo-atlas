# microsoft/GUI-Agent-RL

⭐ 44 · Python · MIT · 推送 2026-07-02 · [GitHub](https://github.com/microsoft/GUI-Agent-RL) · 组织维护

**微软提出的免环境强化学习 GUI Agent 训练框架（VEM）**

VEM（Value Environment Model）研究框架：通过离线数据预训练价值环境模型来估计状态-动作长期价值，再以冻结的 VEM 信号引导策略探索，将价值估计与策略优化解耦，实现无需环境反馈的 GUI 自动化强化学习训练。流程包括构建 conda 环境、基于 LLaMA-Factory 用 LoRA 训练 critic 模型（按说明需 8 张 A100）、训练 AutoGUI 策略模型，并支持在 AITW 数据上离线评测与 Android 环境在线评测。面向 GUI Agent 研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段框架：离线预训练 VEM 估计动作长期价值，再用冻结 VEM 信号引导策略探索
- 无需 next-state 预测与环境反馈的价值估计
- 基于 LLaMA-Factory + LoRA 训练 critic，支持 AITW general/webshopping 任务
- 提供离线评测与 Android 在线评测（Appium + Gradio demo）路径

## 适用场景

- 研究 GUI Agent 的免环境强化学习训练方法
- 复现论文中 AITW general/webshopping 任务的训练与评测
- 在 Android 环境中在线评估 GUI Agent 策略

## 场景标签

`GUI 自动化` `强化学习` `微调` · 领域:效率与自动化

## 证据(README 行号)

> L6: We propose an environment-free RL framework that decouples value estimation from policy optimization by leveraging a
> L41: We use the LLaMA-Factory to train the critic model. Based on our settings, this requires 8 A100 GPUs and uses LoRA 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/GUI-Agent-RL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `77dbbf8617b9` · [字段定义](../../DATASET.md)*
