# Totoro-qaq/Cobsidian

⭐ 13 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/Totoro-qaq/Cobsidian) · 个人维护 · 中文 README

**供编码 Agent 安全维护 Obsidian 知识库的工作流技能**

面向任意编码 Agent（Claude Code、Codex CLI、Copilot CLI 等）的独立工作流技能：在写入 Obsidian/Markdown 知识库前先扫描已有笔记、构建标题/别名身份，产出 create/append/blocked 决策与补丁预览，经一句人类确认后原子写入并校验、可回滚；完整性哈希留在执行层，用户无需复制校验码。非托管服务、非 Obsidian 插件，需本地 Python 3.10+ 与 Markdown 库运行；另提供只读 MCP 服务器与可选的 DeepSeek Harness 原生扩展包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 写入前扫描知识库并给出 create/append/blocked 决策与补丁预览
- 基于完整性哈希的原子写入、单变更确认与回滚
- 确定性 CLI 工具：重复检测、反链建议、校验、事务化写入
- 支持 MCP（只读 stdio 服务器）与 DeepSeek Harness 原生扩展

## 适用场景

- 让编码 Agent 把 AI 对话整理成带 wiki 链接的 Obsidian 笔记
- 防止 Agent 在知识库中写入重复或未审计的修改
- 接入 MCP 的宿主以只读方式检查和预演笔记变更

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L16: Cobsidian is an agent-agnostic workflow skill for maintaining an Obsidian or Markdown vault. It searches before cre
> L22: Use the agent you already know: Claude Code · Codex CLI · GitHub Copilot CLI · Kimi Code · OpenCode · Pi · Antigrav

## 星数曲线

```mermaid
xychart-beta
    title "Totoro-qaq/Cobsidian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `421d254f8bd0` · [字段定义](../../DATASET.md)*
