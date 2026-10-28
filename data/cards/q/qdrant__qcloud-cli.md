# qdrant/qcloud-cli

⭐ 20 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/qdrant/qcloud-cli) · 组织维护

**Qdrant Cloud 官方命令行管理工具**

Qdrant 官方维护的 CLI，用于在终端中管理 Qdrant Cloud 的集群、认证等 API 提供的资源。支持通过 Homebrew（macOS/Linux）、安装脚本、GitHub Releases 二进制或 go install 源码安装。提供命名 context 切换多套凭据、配置文件与环境变量三级配置（优先级递增）、--json 机器可读输出。代码基于 hetznercloud/cli 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 管理 Qdrant Cloud 集群与认证等 API 资源
- 三级配置：配置文件 / 命名 context / 环境变量
- 任何命令可加 --json 输出机器可读结果
- 四种安装途径（Homebrew/安装脚本/Release 二进制/go install）

## 适用场景

- 在终端创建和管理 Qdrant Cloud 集群
- 在 CI 或容器中用脚本安装并自动化云资源管理
- 多账号/多环境间切换凭据

## 场景标签

 · 领域:数据库/云基础设施管理

## 证据(README 行号)

> L5:  The official command-line interface for managing Qdrant Cloud
> L7: `qcloud` is the CLI for Qdrant Cloud. It lets you manage clusters, authentication and anything the API has to offer 

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/qcloud-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `21d19854c09f` · [字段定义](../../DATASET.md)*
