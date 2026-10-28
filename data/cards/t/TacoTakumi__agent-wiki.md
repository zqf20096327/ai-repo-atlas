# TacoTakumi/agent-wiki

⭐ 20 · Python · NOASSERTION · 推送 2026-10-12 · [GitHub](https://github.com/TacoTakumi/agent-wiki) · [官网](https://tacotakumi.github.io/agent-wiki/) · 个人维护

**给 AI agent 的 markdown 知识库：CLI 驱动的持久记忆库**

面向 AI agent 的纯 markdown 知识库工具：vault 由文件与 YAML frontmatter 组成，无数据库，agent 通过单一 CLI（awiki）检索、读取与写入知识。支持采集文件与 URL（trafilatura 抽取 HTML、支持 PDF）并写入不可变 raw/ 归档，附带 sha256 溯源；页面由 raw 源重渲染，漂移以 diff 呈现。提供 Claude Code、pi、OpenCode 的会话自动采集 hook 与 UserPromptSubmit 自动上下文 hook，`awiki serve` 可经 HTTP 共享 vault 并支持按用户角色授权。需 Python 3.10+，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 CLI（awiki/aw）统一本地与网络 vault 操作
- Claude Code / pi / OpenCode 会话自动采集 hook 与自动上下文 hook
- 文件与 URL 采集到不可变 raw/ 归档，sha256 溯源与漂移 diff 防护
- awiki serve 经 HTTP 共享 vault，按用户 reader/writer/admin 授权

## 适用场景

- 让我的编码 agent 在联网搜索前先查本地积累的知识
- 把多个 agent 的会话产出自动沉淀为可持续检索的 wiki
- 在多台机器或多个项目间共享同一个知识库

## 场景标签

`Agent 记忆` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L9: **AI agents earn hard-won knowledge in every conversation, then lose it the moment
> L16: One small CLI (`awiki`) is the only door in, so the same commands work whether the
> L36: - **Agent-first integration** - agent skills plus a self-installing `awiki guide` block that teaches any agent (via

## 星数曲线

```mermaid
xychart-beta
    title "TacoTakumi/agent-wiki 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0d6f896bea13` · [字段定义](../../DATASET.md)*
