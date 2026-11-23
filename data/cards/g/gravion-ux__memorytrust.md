# gravion-ux/memorytrust

⭐ 4 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/gravion-ux/memorytrust) · 个人维护

**审计 AI agent 记忆库中不可信内容的命令行工具**

MemoryTrust 读取 agent 的记忆存储文件，按规则目录检查其中无出处声明、过期事实、同 id 内容冲突、凭据/隐私敏感信息以及注入形态文本，输出 0–100 信任分（A+ 到 F 等级）及 JSON 或 Markdown 报告。定位为人工复核的辅助工具，报告中证据会被脱敏以避免泄露密钥。以 npm 包分发，无需任何运行时或开发依赖，仅使用 Node 内置模块，支持 --fail-on 阈值等参数以集成到流水线。

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

- 17 条规则覆盖溯源、时效、冲突、敏感、隐私、结构、注入七类检查
- 输出 0–100 信任评分（A+ 到 F）及 JSON/Markdown 报告
- 零依赖：仅使用 Node 内置模块
- 报告写入前对证据脱敏，不完整打印泄露的密钥

## 适用场景

- CI 流水线中按 --fail-on 阈值拦截高风险记忆内容
- 定期清理 agent 记忆库中的过期与矛盾条目
- 检测记忆库中混入的凭据与提示注入文本

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: MemoryTrust audits an AI agent's **memory store** — the files an agent writes when it
> L21: MemoryTrust reads the store, applies a catalogue of rules, and produces a trust score
> L26: Node.js 18 or newer. No runtime or dev dependencies — Node built-ins only.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `a2097f766ec6` · [字段定义](../../DATASET.md)*
