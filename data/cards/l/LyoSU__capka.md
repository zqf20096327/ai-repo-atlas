# LyoSU/capka

⭐ 53 · TypeScript · AGPL-3.0 · 推送 2026-10-08 · [GitHub](https://github.com/LyoSU/capka) · [官网](https://capka.app) · 个人维护

**自托管的 AI 协作者：把任务和文件交给它，取回成品文件**

单项目开发者构建的开源自托管 AI agent 平台：用户上传文件或由 agent 在对话中下载/创建文件，每个聊天或项目获得独立的 Linux 沙箱容器（内含 Python、Node、FFmpeg、LibreOffice、Playwright 等工具），agent 在其中执行并返回报告、表格、PDF、转换文档等成品。任务以队列作业形式在服务器端逐步保存，关闭浏览器或重启后可恢复。支持云端厂商或经 Ollama 接本地模型，多用户、注册默认关闭，管理员可配置厂商、模型、MCP 工具、安全策略与审计日志。在 Linux 服务器上以 Docker 部署，单条命令安装，可选 gVisor 内核级隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个聊天/项目独立 Linux 沙箱容器，沙箱内预装 Python/Node/FFmpeg/LibreOffice/Playwright 等工具
- 任务为服务端队列作业，逐步保存，断连或重启后可恢复
- 支持云端厂商 API 密钥或经 Ollama 接本地模型
- 多用户与管理面板：用户、模型、MCP、安全策略（allow/ask/deny）、审计日志、用量

## 适用场景

- 团队在自有服务器上跑 AI 处理文件任务，文件不出内部基础设施
- 合并数据导出、生成报告/PDF/表格等产出文件的办公任务
- 让非开发者同事直接使用，无需了解模型厂商与密钥

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L17: You hand Capka a task and some files, and it hands back the finished thing: a
> L35: 2. Each chat (or each project, for chats inside one) gets its own Linux sandbox and file storage
> L58: |**Models**|Cloud providers or local models through Ollama|

## 星数曲线

```mermaid
xychart-beta
    title "LyoSU/capka 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `45f7b7ebc7b9` · [字段定义](../../DATASET.md)*
