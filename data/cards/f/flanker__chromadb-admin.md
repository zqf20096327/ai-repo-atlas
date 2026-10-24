# flanker/chromadb-admin

⭐ 284 · TypeScript · MIT · 推送 2025-11-16 · [GitHub](https://github.com/flanker/chromadb-admin) · [官网](https://chromadb-admin.com/) · 个人维护

**Chroma 向量数据库的 Web 管理界面（Next.js）**

用 Next.js 构建的 Chroma 嵌入向量数据库管理 UI：支持连接本地或 Docker 化的 ChromaDB 实例进行浏览管理，带认证支持。提供三种运行方式：npm/yarn 本地开发服务器、拉取官方 Docker 镜像直接运行、本地构建 Docker 镜像运行。README 声明本项目为社区项目而非 Chroma 官方产品，采用 MIT 许可。

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

- 提供 Chroma 数据库的图形化管理界面
- 支持认证
- 提供 Docker 镜像与本地构建两种容器运行方式
- 可连接 host.docker.internal 上的本地 ChromaDB 实例

## 适用场景

- 我想用 Web 界面浏览管理 Chroma 向量数据库
- 在 Docker 环境中快速启动一个 Chroma 管理界面

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: Admin UI for the Chroma embedding database, built with Next.js
> L34: docker run -p 3001:3001 fengzhichao/chromadb-admin

## 星数曲线

```mermaid
xychart-beta
    title "flanker/chromadb-admin 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 283 --> 286
    line [285, 284, 284]
```

2026-10-18 285 → 2026-10-24 284（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7cd5b148cfb9` · [字段定义](../../DATASET.md)*
