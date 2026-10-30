# NVIDIA-AI-Blueprints/retail-shopping-assistant

⭐ 103 · Python · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/NVIDIA-AI-Blueprints/retail-shopping-assistant) · 组织维护

**NVIDIA 出品的零售购物助手 AI 蓝图：多智能体导购应用**

基于 LangGraph 编排的多智能体零售购物助手参考应用，微服务架构含 Chain Server（主 API）、Catalog Retriever（商品检索推荐）、Memory Retriever（用户上下文与购物车）、Guardrails（内容安全）与 React 前端。功能覆盖自然语言与图像商品搜索、购物车管理、流式响应与内容审核。部署需 Docker Compose 与 NVIDIA NGC 账号：本地模式需 4x H100（或最低 4x A100）GPU 运行 NIM 容器，云模式经 NVIDIA API Catalog 免本地 GPU；也可经 NVIDIA Brev 一键部署。当前为单操作员本地蓝图，无终端用户认证，官方声明不可暴露给不可信用户或使用真实客户数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体架构：检索、记忆、护栏、编排分离的微服务设计
- 自然语言与图像视觉搜索商品，流式响应生成
- 内置内容安全与审核（Guardrails）
- 支持本地 NIM（多 GPU）与云端 API Catalog 两种部署模式

## 适用场景

- 搭建带商品检索与导购对话的电商购物助手
- 参考多智能体+RAG+护栏的零售 AI 应用架构
- 在本地 GPU 集群或云端部署可运行的导购原型

## 场景标签

`多智能体` `RAG` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L21: The Retail Shopping Assistant is an AI-powered blueprint that provides a comprehensive interface for an intelligent
> L37: The application follows a microservices architecture with specialized agents for different tasks:

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-AI-Blueprints/retail-shopping-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-30 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `969be65e4d10` · [字段定义](../../DATASET.md)*
