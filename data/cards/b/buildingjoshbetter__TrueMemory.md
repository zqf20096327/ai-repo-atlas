# buildingjoshbetter/TrueMemory

⭐ 382 · Python · AGPL-3.0 · 推送 2026-10-14 · [GitHub](https://github.com/buildingjoshbetter/TrueMemory) · [官网](https://truememory.net) · 个人维护

**本地优先的 AI agent 自动记忆层：自动捕获与召回对话记忆**

面向 Claude Code、Cursor、Codex CLI、Gemini CLI 等 AI 编码工具与 Python 开发者的记忆系统：通过生命周期钩子自动从对话中捕获记忆，自动注入后续会话，数据存于本地单个 SQLite 文件。检索采用 6 层管线加重排序，分 Edge/Base/Pro 三档（Pro 的 HyDE 查询扩展需 LLM API key）。默认开启匿名使用遥测（不含记忆内容，可用环境变量关闭）。AGPL-3.0，商业使用需另行授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动捕获对话记忆并自动注入后续会话，无需手动存储
- 全部数据存于本地单个 SQLite 文件，Edge/Base 档零外部调用
- 6 层检索管线 + 重排序，Edge 档仅 CPU 即可运行
- 提供 11 个 MCP 工具与 Python API，附带可复现的基准测试脚本

## 适用场景

- 让 Claude Code/Cursor 等编码助手跨会话记住我的偏好和技术栈
- 作为 Python 库为自研 agent 添加记忆能力
- 在完全离线环境中为 agent 提供记忆检索

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L26: **It works without you thinking about it.** TrueMemory automatically captures memories from your conversations and 
> L138: Lifecycle hooks capture conversations automatically. No manual work needed. Your memories stay local in a single S

## 星数曲线

```mermaid
xychart-beta
    title "buildingjoshbetter/TrueMemory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 380 --> 383
    line [381, 382]
```

2026-10-18 381 → 2026-10-23 382（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `73ab9ed2c7ea` · [字段定义](../../DATASET.md)*
