# Mattral/rlpost

⭐ 28 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Mattral/rlpost) · 个人维护

**LLM 后训练代码集：SFT、奖励模型、PPO、DPO 的训练实现**

面向开发者的语言模型后训练 Python 包（rlhf_platform），提供 LoRA SFT（经 Hugging Face Trainer）、偏好奖励模型训练、PPOTrainer（GAE、裁剪策略损失、KL 惩罚）与 DPOTrainer。四条 Typer 命令中仅 train-sft 与 train-reward 实际训练；run-dpo 打印占位符不训练，train.py 退出码 2。README 自述多项未完成：DPO/PPO 测试 11 个失败、PPO 的 log-prob 采集存在已知 bug、TRL 对齐未做。仅 CPU 单测，无 GPU 基准，未记录安装运行（pip install -e . 未执行）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- PPOTrainer 实现 GAE、裁剪策略损失、价值损失、熵与 KL 项
- DPOTrainer 实现序列级 DPO 损失（冻结参考策略）
- toy 模式切 Anthropic HH-RLHF 至 1,000 行
- 四条 CLI 命令：train-sft/train-reward 可训练，run-ppo/run-dpo 未接线

## 适用场景

- 学习或审查 PPO/DPO/RM/SFT 的后训练参考实现
- 在 CPU 上跑 toy 模式（distilgpt2 + bert-tiny）熟悉流程
- 按 ROADMAP.md 跟踪修复进度后做二次开发

## 场景标签

`微调` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: Code for language-model post-training: supervised fine-tuning, a reward model, PPO, and DPO.
> L33: |`src/rlhf_platform/ppo_engine.py`|The only PPO implementation: `PPOTrainer`. GAE, a clipped policy loss, an unclip
> L35: |`src/rlhf_platform/sft_engine.py`|LoRA SFT through the Hugging Face `Trainer`.|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `befd6c4d04aa` · [字段定义](../../DATASET.md)*
