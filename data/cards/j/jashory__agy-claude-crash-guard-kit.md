# jashory/agy-claude-crash-guard-kit

⭐ 4 · Python · MIT · 推送 2026-11-19 · [GitHub](https://github.com/jashory/agy-claude-crash-guard-kit) · [官网](https://jashory.github.io/agy-claude-crash-guard-kit/) · 组织维护

**为 AI 编码代理防护 HTTP 400/30MB 崩溃的钩子工具包**

面向 Claude Code、Antigravity、Cursor 等 AI 编码代理的防护工具包：通过 PreToolUse 钩子拦截加密 PDF、0 字节媒体、伪装 HTML 图片与超大截图进入 transcript.jsonl，避免轨迹污染导致 HTTP 400 或 30MB 消息上限的会话永久崩溃；附 Stop 验证门要求编辑后运行验证命令、Dark-Mode Crash Doctor GUI 解析日志定位出错步骤，以及 session_sync.py 在 Claude Desktop 与 VS Code/IDE 间同步会话。可作为 Agent Skill、独立 CLI（agy-crash-guard）或 GitHub Action 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PreToolUse 防火墙在二进制写入 transcript.jsonl 前拦截并返回修复命令
- Loop-Safe Stop 验证门：每轮最多触发一次的编辑后验证检查
- Crash Doctor GUI（--diagnose auto）解析 transcript.jsonl 与 language_server.log 定位错误步骤
- session_sync.py 跨 IDE 会话同步（UserPromptSubmit 钩子，防重复注入）

## 适用场景

- AI 编码代理读取加密 PDF/损坏图片后会话永久报错时做防护
- 长会话（500+ 步）中防止轨迹被超大截图撑爆
- 在 Claude Desktop 与 Claude Code VS Code 之间同步缺失的对话轮次
- CI/CD 工作流中以 GitHub Action 形式运行防护检查

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L35: 1. **`crash_guard.py` (Full 760-Line Engine)**:
> L36:  - **`PreToolUse` Firewall**: Blocks locked PDFs, 0-byte media, fake HTML-disguised images, and `>450 KB` uncompres
> L39: 2. **`session_sync.py` (Cross-IDE Session Memory Bridge)**:

## 星数曲线

```mermaid
xychart-beta
    title "jashory/agy-claude-crash-guard-kit 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-21"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-08 4 → 2026-11-21 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `5b88f3c6b3dc` · [字段定义](../../DATASET.md)*
