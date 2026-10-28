# momaek/tolato

⭐ 21 · Go · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/momaek/tolato) · 个人维护 · 中文 README

**让已有 AI agent 用自然语言管理服务器机群的自托管平台**

由 Go 服务端（Gin+Postgres）、节点 agent、CLI 与 Vue 3 Web UI 组成的自托管服务器管理平台：在被管服务器上部署 agent 后，将一段 prompt 粘贴进 Claude Code/Codex 等编码 agent，agent 通过拉取 skill.md 与 tolato CLI 即可用自然语言执行命令、传文件、查询节点指标与网络探测。服务端自身无需配置 LLM；可选 web chat 需管理员配置 OpenAI 兼容端点。提供按密钥分级（只读/可执行）的权限控制、危险命令确认、审计日志与 SSO，Docker Compose 一行部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 服务端不配置 LLM，模型由用户已有的编码 agent 提供
- 危险命令（rm -rf/reboot 等）默认需确认，黑名单可直接拒绝，均可编辑
- 所有命令进入审计日志，密钥按只读/可执行分级并可吊销
- agent 节点支持系统指标采集与 ICMP/TCP/带宽探测

## 适用场景

- 让 Claude Code/Codex 等 AI agent 直接排查服务器磁盘、502 等问题
- 通过自然语言推送配置文件、测试并重载服务
- 小团队以用户/组粒度管理多机群的操作权限与审计

## 场景标签

 · 领域:运维基础设施/AI agent 工具

## 证据(README 行号)

> L4: Manage your server fleet from the AI agent you already use. Deploy Tolato, put a small agent on each server, paste o
> L6: There is no LLM to configure on the server: the model is whatever already runs your coding agent.
> L25: Under the hood the agent drives the CLI — `tolato nodes list`, `tolato exec web-01 -- …`, `tolato cp ./nginx.conf w

## 星数曲线

```mermaid
xychart-beta
    title "momaek/tolato 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3a18bac63c62` · [字段定义](../../DATASET.md)*
