# MinimalFuture/linkai-cli

⭐ 20 · Go · MIT · 推送 2026-07-08 · [GitHub](https://github.com/MinimalFuture/linkai-cli) · [官网](https://link-ai.tech/) · 组织维护 · 中文 README

**终端里访问 LinkAI 智能体平台资源的命令行工具**

LinkAI 平台的官方 CLI，用 Go 编写、npm/脚本分发的预编译二进制。命令覆盖平台资源管理（AI 应用、知识库向量检索与文件导入、数据库查询与 SQL 执行、工作流、插件、账户额度）与模型能力（多轮对话、文生图、文生视频、TTS、模型列表）。面向人类与 AI agent 双端使用：内置 agent skill（安装到 Claude Code、Cursor、Codex、CowAgent 等工具目录），支持 --json 与 --dry-run；登录采用 scope 权限模型，令牌存 macOS Keychain。需 LinkAI 账号登录方可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- app/knowledge/database/workflow/plugin/account 六类平台资源命令
- chat/image/video/audio/model 模型能力命令，视频生成内置轮询
- 随 CLI 捆绑 agent skill，可被 Claude Code 等工具直接驱动
- scope 权限体系：读与生成默认授权，写操作需显式申请

## 适用场景

- 在终端管理与调用 LinkAI 平台上的应用、知识库和工作流
- 让 Claude Code、Cursor 等 AI agent 通过 skill 使用平台能力
- 命令行生成文本对话、图片、视频与语音

## 场景标签

`图像生成` `语音合成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3:  The command-line interface for the LinkAI agent platform.
> L11: **LinkAI CLI** brings the full LinkAI platform to the terminal for both agents and people — models, apps, knowledge
> L97: Once installed, agents learn how to drive the CLI through its bundled skill — no extra setup required. The skill li

## 星数曲线

```mermaid
xychart-beta
    title "MinimalFuture/linkai-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `67583a433904` · [字段定义](../../DATASET.md)*
