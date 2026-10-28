# Bhanunamikaze/AI-Dataset-Generator

⭐ 21 · Python · MIT · 推送 2026-08-08 · [GitHub](https://github.com/Bhanunamikaze/AI-Dataset-Generator) · 个人维护

**给 AI 编程助手的训练数据集生成技能，产出 SFT/DPO 数据**

面向 Claude Code、Codex、Antigravity、Cursor 等 agent IDE 的数据集生成 skill：以 14 个子技能、19 个流水线脚本与 15 个共享模块，把主题、URL、网页检索或原始 JSONL/CSV 转换为 SFT/DPO 训练集。流程含证据采集（research.py，五后端搜索回退）、导入去重、LLM-judge 审查、覆盖度与漂移检测、语料审计（泄漏/合成指纹）及 OpenAI/HuggingFace/CSV/JSONL 导出并生成数据卡。内部规范 schema 固定，导出 schema 可自定义。通过 install.sh/install.ps1 一键安装到各 IDE 原生格式，Python 依赖需 pip 安装，支持对抗性语料的注入宽容模式。

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

- 19 个流水线脚本覆盖采集、生成、验证、去重、审计、导出全流程
- 多 IDE 原生格式安装（Claude Code/Codex/Cursor/Windsurf/Copilot 等 8 种）
- SFT/DPO 数据集产出，含硬负例偏好对生成
- 语料级审计：泄漏、合成指纹、split 不相交、推理多样性

## 适用场景

- 为微调准备 SFT/DPO 训练数据集并做质量审计
- 把网页检索证据或现有 CSV/JSONL 规范化为训练数据
- 在 Claude Code 或 Cursor 里用自然语言触发数据集构建流程

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: An LLM-first dataset generation skill for agent IDEs and AI coding assistants, with 14 specialized sub-skills, 19 pi
> L91: This skill is designed for reasoning-first dataset construction:
> L101: - internal canonical schema: fixed (`resources/internal-schema/canonical_schema.json`)

## 星数曲线

```mermaid
xychart-beta
    title "Bhanunamikaze/AI-Dataset-Generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `b673cef7221a` · [字段定义](../../DATASET.md)*
