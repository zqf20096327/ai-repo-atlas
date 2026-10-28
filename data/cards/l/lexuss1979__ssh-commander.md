# lexuss1979/ssh-commander

⭐ 23 · TypeScript · MIT · 推送 2026-10-14 · [GitHub](https://github.com/lexuss1979/ssh-commander) · 个人维护

**本地运行的 AI DevOps 应用：通过 SSH 在你的 VPS 上排查与运维**

运行在用户自己电脑上的服务器管理 Web 应用：通过 SSH/SFTP 连接一台或多台 Linux VPS，提供 PTY 终端、文件管理器、Docker Explorer、PostgreSQL/MySQL 连接、systemd 服务管理、Nginx 配置查看、端口/隧道、cron 与包更新等功能。AI agent 为可选启用：走 OpenAI 兼容 API（含 DeepSeek、vLLM 等），可读取日志自主排查，变更类操作需用户批准，只读命令受白名单限制。密码与 API key 以明文存储在本地数据文件中；不支持无人值守 24/7 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI agent 通过 SSH 自主排查服务器问题，变更操作需用户批准
- 终端/SFTP/Docker/数据库/systemd/Nginx 等手动工具可在无 AI key 时使用
- Docker Compose 一条命令部署预构建镜像（amd64/arm64）
- 多服务器配置、按服务器持久记忆与阈值告警

## 适用场景

- 首次租用 VPS 后让 agent 检查环境并部署应用
- 网站故障时让 agent 读日志定位原因并提出修复方案
- 在一个应用里管理多台服务器的终端、文件与容器

## 场景标签

 · 领域:服务器运维/DevOps 工具

## 证据(README 行号)

> L20: > **Try it without AI first.** The terminal, files and Docker work without an API key. Get familiar with the app, t
> L11: Describe what you need. ssh-commander's AI agent connects to your server over SSH, investigates problems, runs audi

## 星数曲线

```mermaid
xychart-beta
    title "lexuss1979/ssh-commander 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `cb97e6de237a` · [字段定义](../../DATASET.md)*
