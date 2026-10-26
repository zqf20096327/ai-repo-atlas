# wahyudesu/Fastapi-AI-Production-Template

⭐ 114 · Jupyter Notebook · MIT · 推送 2026-04-16 · [GitHub](https://github.com/wahyudesu/Fastapi-AI-Production-Template) · 个人维护

**ML/AI 项目 FastAPI 生产级启动模板**

面向机器学习/AI 项目的 FastAPI 起步模板仓库：内置安全与 API 端点保护、限流与中间件、轻量 Dockerfile、Kubernetes 清单（Deployment/Service/HPA/Ingress）、loguru 日志与 ruff 格式化；依赖与虚拟环境用 uv 管理，本地通过 uvicorn 运行，支持 MCP 端点与 Jupyter notebook 实验。路由层用于 ML/AI 模型与 AI agent 的服务化，可部署到 DigitalOcean、Google Cloud、Render、Railway 等云平台或 VPS。无内置数据库，可自行添加。

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

- ML/AI 模型与 AI agent 的 router 服务化支持
- 轻量 Dockerfile 与 Kubernetes 部署清单（HPA/Ingress）
- uv 管理依赖，MCP 端点与 Jupyter 实验 notebook
- 内置安全、限流、中间件与 loguru 日志

## 适用场景

- 把 ML 模型封装成生产可用的 REST API 服务
- 搭建基于 FastAPI 的 AI Agent 后端
- 快速获得带 Docker/K8s 配置的可部署项目骨架

## 场景标签

 · 领域:ML/AI 后端工程/模板

## 证据(README 行号)

> L3:  Simple starter repo for your Machine Learning/AI projects
> L40: - ✅Router serving support for ML, AI models and AI agents
> L32: - Build and serve machine learning models via production-ready APIs

## 星数曲线

```mermaid
xychart-beta
    title "wahyudesu/Fastapi-AI-Production-Template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-26 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `36c9f2892f57` · [字段定义](../../DATASET.md)*
