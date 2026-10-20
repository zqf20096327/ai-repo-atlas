# microsoft/SkillOpt

⭐ 18,529 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/microsoft/SkillOpt) · [官网](https://aka.ms/skillopt) · 组织维护

**为冻结参数的 LLM agent 训练可复用自然语言技能文档的优化器**

将技能文档视为冻结 agent 的可训练状态：由独立的优化器模型把带评分的轨迹转化为对单个技能文档的有界增/删/改编辑，默认路径下候选编辑仅在提升留出验证分数时被接受，配合文本学习率预算、被拒编辑缓冲与按 epoch 的慢/元更新。部署产物为 300–2,000 token 的 best_skill.md，推理时不增加模型调用。以 PyPI 包发布，含多后端支持、六个内置基准与可选 WebUI 仪表盘，另提供 skillopt-sleep 夜间离线自进化 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 11.6 天,年发版 2,68 位贡献者
- 涨星:近 1 天 **+39**(自 20261016 起算)
- 安装:pypi 包 `skillopt` 月下载 12,972
- 平台:WINDOWS / WEB · 协议:MCP

## 能力要点

- 技能文档作为可训练状态：rollout→reflect→aggregate→select→update→evaluate 训练循环
- 验证门控编辑接受机制与文本学习率预算、被拒编辑缓冲
- 多后端支持：OpenAI / Azure / Claude / Qwen / MiniMax 及多种 exec 后端
- 部署产物 best_skill.md（300–2,000 token），推理时零额外模型调用

## 适用场景

- 为编码 agent（Claude Code / Codex / Copilot）离线沉淀经过验证的技能
- 在基准任务上以文本优化方式提升冻结模型的 agent 表现
- 通过 WebUI 监控技能训练过程

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L17: - **[2026-06-02]** 🎉 **SkillOpt v0.1.0 is now available on PyPI!** Install with `pip install skillopt`. This initia
> L26: **SkillOpt treats the skill document as the trainable state of a frozen
> L57: A backend = a chat / exec target (e.g. `openai_chat`, `claude_chat`,

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `572bf622ef23` · [字段定义](../../DATASET.md)*
