# ravitemer/codecompanion-history.nvim

⭐ 194 · Lua · MIT · 推送 2026-01-22 · [GitHub](https://github.com/ravitemer/codecompanion-history.nvim) · 个人维护

**codecompanion.nvim 的会话历史管理扩展：保存、浏览、恢复 AI 聊天**

Neovim Lua 插件，作为 codecompanion.nvim 的扩展运行：自动或手动保存聊天会话，保存并恢复完整上下文（消息历史、系统提示词、LLM 适配器与设置、工具 schema 与输出、引用等），提供历史浏览器与摘要系统（手动 gcs 生成、gbs 浏览），支持按项目过滤、聊天复制与可选过期清理。可选安装 VectorCode CLI 后提供 @memory 工具，对摘要建索引供 LLM 检索过往对话。标题与摘要生成复用聊天当前的适配器和模型，README 提示可配置更便宜的模型。通过 lazy.nvim 安装并加入 CodeCompanion 配置的 extensions 段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 保存/恢复完整聊天状态：消息、系统提示词、适配器设置、工具 schema 与输出、引用
- 摘要系统：分块摘要生成、摘要浏览器、可插入当前聊天
- 可选 VectorCode 集成的 @memory 工具，支持向量检索过往聊天摘要
- 标题自动生成与按 N 条提示刷新（可限制刷新次数）

## 适用场景

- 在 Neovim 中保存并恢复与 AI 的编程对话会话
- 跨项目浏览、检索过往 AI 聊天与摘要
- 让新聊天引用以往对话摘要中的上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: A history management extension for codecompanion.nvim that enables saving, browsing and restoring chat sessions.
> L64: > [!NOTE]
> L70: - codecompanion.nvim

## 星数曲线

```mermaid
xychart-beta
    title "ravitemer/codecompanion-history.nvim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 193 --> 195
    line [194, 194]
```

2026-10-18 194 → 2026-10-23 194（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7a8c18c5d91c` · [字段定义](../../DATASET.md)*
