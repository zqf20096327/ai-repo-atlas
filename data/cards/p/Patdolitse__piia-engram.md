# Patdolitse/piia-engram

⭐ 166 · Python · AGPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/Patdolitse/piia-engram) · [官网](https://pypi.org/project/piia-engram/) · 个人维护 · 中文 README

**给 AI 编程工具用户提供可查看、可编辑的本地化身份/记忆层**

以 pip 安装的本地优先 MCP 服务，将用户身份、偏好、质量标准、经验教训与关键决策存为 ~/.engram/ 下的 JSON/Markdown 文件，供 Claude Code、Codex、Cursor 等多个 MCP 编码工具读取同一份知识。写入采用分级审批策略（高风险项待用户复核，可设 strict 模式全部把关），提供 Memory Lens 预览对外暴露的内容与被隐去项，支持可选字段级 AES-256-GCM 加密、跨工具连续性验证分级、会话洞察提取与 playbook 自动起草。README 自述非 agent 记忆数据库，聚焦用户层而非任务上下文存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 JSON/Markdown 存储，用户可查看、编辑、备份、迁移
- 分级写入审批与 Memory Lens 暴露内容预览
- 支持 16 个 AI 工具接入（MCP over stdio 及 Markdown 兜底），证据分级标注
- 19 个核心 MCP 工具 + 40 个高级工具，含跨项目知识继承与 playbook 自动提取

## 适用场景

- 在多个 AI 编码工具间保持同一份用户偏好与项目上下文
- 为敏感字段设置审批与脱敏，控制 AI 可见内容
- 沉淀项目经验教训并跨项目复用

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: ### Local-first AI work identity you can see, edit, and override — portable across your MCP coding tools.
> L29: > **TL;DR:** piia-engram is a local-first personal AI identity layer. It helps multiple coding agents start from th
> L92: |Claude Code|MCP over stdio|L4 partial continuity proof (Claude Code -> Codex)|

## 星数曲线

```mermaid
xychart-beta
    title "Patdolitse/piia-engram 星数(近 7 点)"
    x-axis ["2026-10-25", "2026-10-29", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-13", "2026-11-27"]
    y-axis "stars" 162 --> 167
    line [163, 164, 165, 163, 165, 166, 166]
```

2026-10-25 163 → 2026-11-27 166（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `fdd872bd73fe` · [字段定义](../../DATASET.md)*
