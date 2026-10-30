# Jai0401/docSmith

⭐ 16 · JavaScript · MIT · 推送 2026-05-24 · [GitHub](https://github.com/Jai0401/docSmith) · [官网](https://doc-smith.vercel.app) · 个人维护

**从 GitHub 仓库 URL 生成文档、Dockerfile 与 Compose 的 API 服务**

基于 FastAPI 的 RESTful API 服务，输入 GitHub 仓库 URL，经 OpenRouter 的 LLM 分析代码库后生成 Markdown 文档、Dockerfile 与 Docker Compose 配置；内部使用 Repomix 处理仓库内容。前后端分离（FastAPI + Vite），支持 Render/Vercel 部署，模型与 API 端点可通过环境变量配置。运行需要 OpenRouter API key、Python 3.7+、Node.js/npm 与 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个生成端点：文档（Markdown）、Dockerfile、Docker Compose（YAML）
- 通过 OpenRouter 调用 LLM，模型与 Base URL 可经环境变量配置
- 提供 RESTful API 供其他工具集成
- 支持 Render（后端）/Vercel（前端）部署配置

## 适用场景

- 给已有 GitHub 项目快速生成 README/文档
- 为项目生成 Dockerfile 与 Compose 配置
- 把文档生成能力以 API 形式接入自己的工具链

## 场景标签

`代码生成` `AI 写作` · 领域:编码与开发

## 证据(README 行号)

> L2: docSmith is an API designed to generate documentation, Dockerfiles, and Docker Compose configurations from a GitHub 
> L6: * **Documentation Generation:** Automatically generates comprehensive documentation for a given GitHub repository.

## 星数曲线

```mermaid
xychart-beta
    title "Jai0401/docSmith 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `206e2e089285` · [字段定义](../../DATASET.md)*
