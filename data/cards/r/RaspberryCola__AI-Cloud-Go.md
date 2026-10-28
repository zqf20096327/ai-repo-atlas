# RaspberryCola/AI-Cloud-Go

⭐ 47 · Go · 推送 2026-03-21 · [GitHub](https://github.com/RaspberryCola/AI-Cloud-Go) · 个人维护 · 中文 README

**Go 开发的 LLM 应用后端：云盘存储与知识库问答平台**

基于 Go 1.23.4 与 Gin/GORM 的 LLM 应用后端服务，提供用户认证、文件上传下载、知识库文档导入与检索问答、自定义 LLM/Embedding 模型管理、Agent 配置与调试对话等 API 能力。集成 Milvus 向量检索，支持本地存储、MinIO、阿里云 OSS 三种对象存储后端。部署方式为 go run 源码运行或 Docker 构建，依赖 MySQL/MinIO/Milvus 可经 docker-compose 启动，配置经 YAML 文件或环境变量。

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

- 知识库文档导入、Milvus 向量检索与问答
- 自定义 LLM / Embedding 模型管理与 Agent 配置调试
- 本地存储 / MinIO / 阿里云 OSS 多种对象存储后端
- 提供单后端与前后端联合部署两种方式

## 适用场景

- 搭建带知识库问答的私有云盘与文件服务后端
- 为前端提供模型管理与 Agent 对话 API
- 配合自建前端做前后端一体化部署

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: AI-Cloud-Go 是一个基于 Go 的 LLM 应用后端，提供用户管理、文件存储、知识库管理、模型管理、Agent 配置与对话能力，并集成 Milvus 向量检索与多种对象存储后端。
> L12: - 自定义 LLM / Embedding 模型管理
> L13: - Agent 配置、调试对话、历史会话

## 星数曲线

```mermaid
xychart-beta
    title "RaspberryCola/AI-Cloud-Go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-28 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `54946a15c16e` · [字段定义](../../DATASET.md)*
