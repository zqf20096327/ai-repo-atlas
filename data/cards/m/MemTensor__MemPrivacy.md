# MemTensor/MemPrivacy

⭐ 127 · Python · 推送 2026-06-16 · [GitHub](https://github.com/MemTensor/MemPrivacy) · 组织维护 · 中文 README

**云端 agent 长期记忆的本地可逆脱敏隐私保护框架**

面向边云协同 LLM agent 的记忆隐私管理框架：在数据离开设备前本地检测隐私片段（按 PL1–PL4 四级与类型分类），以带类型的语义占位符替换原文，映射关系存于本地 SQLite；云端仅见占位符并正常执行推理与记忆读写，响应返回后本地还原原值。发布 SFT/RL 训练的 4B/1.7B 等检测模型，附带 MemPrivacy-Bench 基准（200 合成用户、中英双语）及对 Mem0/LangMem/Memobase 的评测脚本。以 git clone + pip 依赖方式从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地可逆假名化：类型化占位符替换 + SQLite 本地映射 + 回复还原
- PL1–PL4 四级隐私分类与用户可配置保护策略
- 开源 SFT/RL 训练的隐私检测模型（4B/1.7B 等，HuggingFace/ModelScope）
- MemPrivacy-Bench 基准（200 合成用户、中英双语）与三大记忆系统评测脚本

## 适用场景

- 在云 agent 与 Mem0/LangMem 等记忆系统之间加一层隐私保护
- 评估不同脱敏策略下记忆系统的隐私泄露与效用损失
- 研究边云场景下隐私与个性化效用的权衡

## 场景标签

`Agent 记忆` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L19: MemPrivacy is a **privacy-preserving personalized memory management framework** for **edge-cloud agents**.
> L86: - works as a drop-in privacy layer for existing cloud agents / memory systems

## 星数曲线

```mermaid
xychart-beta
    title "MemTensor/MemPrivacy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 125 --> 128
    line [126, 127, 127]
```

2026-10-18 126 → 2026-10-26 127（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `943ca22be883` · [字段定义](../../DATASET.md)*
