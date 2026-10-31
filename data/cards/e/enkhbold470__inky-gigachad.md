# enkhbold470/inky-gigachad

⭐ 14 · TypeScript · 推送 2026-08-10 · [GitHub](https://github.com/enkhbold470/inky-gigachad) · 个人维护

**跨多个 AI 编码工具共享的本地 MCP 记忆服务器**

一个本地运行的 MCP 服务器，为 Cursor、Claude Code、Codex 与 Windsurf 提供共享记忆存储：记忆与规则保存在本地文件 ~/.inky-gigachad/memory.json，通过 11 个 MCP 工具（save_memory、search_memories、save_rule、import_project_rules 等）读写。安装方式有 npx（尚未发布到 npm）与 git clone 后 pnpm 构建；也可在 MCP 配置中用 node 直接指向构建产物。面向使用多个 AI 编码工具并希望保持上下文一致的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单个 MCP 服务器同时接入 Cursor、Claude Code、Codex、Windsurf
- 11 个记忆/规则工具（保存、检索、导入项目规则、删除等）
- 记忆以本地 JSON 文件存储（~/.inky-gigachad/memory.json）
- 提供 smoke 测试与逐工具的人类式测试脚本

## 适用场景

- 在多个 AI 编码工具间共享项目记忆与规则
- 把项目既有规则导入统一记忆存储
- 团队或个人本地保存编码偏好供 agent 检索

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Local MCP memory shared across Cursor, Claude Code, Codex, and Windsurf.
> L37: `save_memory` · `get_memory` · `list_memories` · `search_memories` · `save_rule` · `list_rules` · `search_rules` · 

## 星数曲线

```mermaid
xychart-beta
    title "enkhbold470/inky-gigachad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fd4894ff2c4d` · [字段定义](../../DATASET.md)*
