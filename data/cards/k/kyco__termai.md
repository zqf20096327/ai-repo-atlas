# kyco/termai

⭐ 37 · Rust · MIT · 推送 2026-08-28 · [GitHub](https://github.com/kyco/termai) · 个人维护

**Rust 编写的多供应商终端 AI 助手**

用 Rust 实现的命令行 AI 助手，支持接入 Anthropic Claude、OpenAI GPT-5.x 与 OpenAI Codex（经 ChatGPT 订阅 OAuth）。功能包括：git 式对话分支的会话管理、可复用 prompt 预设、AI 辅助 Git 操作（提交、代码审查、冲突解决）、代码库上下文发现、SQLite 存储与隐私脱敏；可选启用 web 搜索/抓取工具。通过 cargo 从源码构建安装，需 Rust/Cargo 前置环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商接入：Anthropic Claude、OpenAI GPT-5.x、OpenAI Codex（ChatGPT OAuth）
- git 式对话分支的本地会话管理与全文搜索
- AI 辅助 Git 操作（提交、审查、冲突解决）
- SQLite 存储与隐私脱敏，每轮即时落盘

## 适用场景

- 在终端里向 AI 提问并携带代码文件上下文
- 让 AI 协助生成提交信息、做代码审查、解决合并冲突
- 保存并检索过往对话，用分支方式管理会话

## 场景标签

`AI 助手` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: A multi-provider AI assistant for your terminal, written in Rust. TermAI works with Anthropic Claude, OpenAI GPT-5.x
> L19: termai auth login claude         # Or: openai, codex (ChatGPT OAuth)

## 星数曲线

```mermaid
xychart-beta
    title "kyco/termai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `53a8fb14583d` · [字段定义](../../DATASET.md)*
