# nidhi-singh02/honcho-local-setup

⭐ 10 · 推送 2026-06-24 · [GitHub](https://github.com/nidhi-singh02/honcho-local-setup) · 个人维护

**在 Mac+树莓派本地部署 Honcho 记忆服务的配置集**

作者自用的配置层仓库：包含 `.env.local` 与 Docker Compose override 两个文件，用于在 Mac 上以 Docker Compose 运行 Honcho、通过 `host.docker.internal` 连接同机 Ollama（Qwen 3 Embedding 4B 与 Qwen 3.5 27B），并让树莓派上的 Hermes Agent 经局域网 IP 访问 Honcho API。非 Honcho 分叉，需配合官方 Honcho 仓库使用；提供健康检查验证步骤与关闭认证的安全提示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两文件配置层：.env.local 与 docker-compose.override.yml，复制即用
- Mac 端 Docker Compose 运行 Honcho，容器经 host.docker.internal 访问 Ollama
- 树莓派 Hermes Agent 经 LAN IP 接入 Honcho API
- 附健康检查与容器内连通性验证命令

## 适用场景

- 在 Mac 上自托管 Honcho 为树莓派上的 Hermes 提供记忆服务
- 用 Ollama 本地模型驱动 Honcho 的嵌入与派生流程
- 搭建局域网内 Pi-to-Mac 的 agent 记忆后端

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: It is not a Honcho fork. You still use the official Honcho repo. These files only show the local `.env` values and t
> L9: - Honcho runs on your Mac with Docker Compose.
> L13: - Honcho's Docker containers talk to Ollama through `host.docker.internal`.

## 星数曲线

```mermaid
xychart-beta
    title "nidhi-singh02/honcho-local-setup 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `04042d5759db` · [字段定义](../../DATASET.md)*
