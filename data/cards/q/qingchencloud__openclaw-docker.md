# qingchencloud/openclaw-docker

⭐ 10 · JavaScript · MIT · 推送 2026-03-09 · [GitHub](https://github.com/qingchencloud/openclaw-docker) · 组织维护 · 中文 README

**OpenClaw AI 助手平台的 Docker 容器化部署方案**

将 OpenClaw AI 助手平台封装为 Docker 镜像，一条命令启动 Gateway 与 ClawPanel Web 管理面板，支持 docker run 与 docker compose 两种部署方式，含一体与 Gateway/Panel 分离部署。提供环境变量或面板 UI 配置模型渠道（OpenAI/Anthropic/自定义 OpenAI 兼容端点），数据经 Volume 持久化，镜像提供汉化版与原版、指定版本标签，CI 构建双架构镜像，并给出国内镜像源、Nginx 反代与常见问题指引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条 docker run 命令启动 Gateway + Web 管理面板
- latest/gateway/official/版本号四种镜像标签
- CI 自动构建 linux/amd64 与 linux/arm64 双架构镜像
- 腾讯云 TCR 与 GHCR 双源镜像，国内加速

## 适用场景

- 自托管部署 OpenClaw AI 助手平台
- 生产环境将 Gateway 与管理面板分容器独立管理
- 国内网络环境快速拉取并启动服务

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: 开箱即用的 OpenClaw AI 助手平台容器化部署方案。
> L5: 一条命令启动，包含 Gateway + Web 管理面板，零配置即可使用。
> L89: |`OPENCLAW_SOURCE`|`zh`|版本源：`zh`=汉化版，`official`=原版|

## 星数曲线

```mermaid
xychart-beta
    title "qingchencloud/openclaw-docker 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `8b938c86cdd8` · [字段定义](../../DATASET.md)*
