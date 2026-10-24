# ozbillwang/openclaw-in-docker

⭐ 63 · Shell · 推送 2026-04-04 · [GitHub](https://github.com/ozbillwang/openclaw-in-docker) · [官网](https://medium.com/p/bf75c4eb1887) · 个人维护

**初学者用 Docker 安全运行 OpenClaw 的实践指南与脚本**

面向初学者的操作指南仓库：通过 git clone 拉取后运行 docker-setup.sh 脚本，该脚本拉取 OpenClaw 网关镜像、启动引导向导、以 Docker Compose 启动网关并生成 token 存入 .env。提供镜像版本切换（latest/main）、升级流程（配置文件 ~/.openclaw/openclaw.json 不受影响）与故障排查条目。前置要求为已安装 Docker 与 Bash v4+。另附博客链接说明如何配合本地 LLM 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- docker-setup.sh 一键完成拉取镜像、引导向导、Compose 启动与 token 生成
- 提供 latest/main 镜像切换与升级、故障排查说明
- 升级不影响 ~/.openclaw/openclaw.json 配置文件

## 适用场景

- 按步骤在 Docker 中部署 OpenClaw 网关
- 升级已部署的 OpenClaw 版本并保留配置
- 排查启动失败等常见问题

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This guide helps you run OpenClaw quickly and safely with Docker.
> L46: * pull openclaw gateway image

## 星数曲线

```mermaid
xychart-beta
    title "ozbillwang/openclaw-in-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cb114df7fa5c` · [字段定义](../../DATASET.md)*
