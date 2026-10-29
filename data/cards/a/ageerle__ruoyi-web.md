# ageerle/ruoyi-web

⭐ 425 · Vue · MIT · 推送 2026-09-21 · [GitHub](https://github.com/ageerle/ruoyi-web) · [官网](https://web.ruoyiai.chat) · 个人维护 · 中文 README

**RuoYi-AI 的用户前端：AI 对话、Agent 交互与知识库问答界面**

基于 Vue 3 + TypeScript + Ant Design Vue + Pinia + Vite 构建的 RuoYi-AI 平台用户前端，为终端用户提供 AI 对话、Agent 交互和知识库问答的使用界面。需配套后端服务（ruoyi-ai，含 MySQL、Redis、Weaviate 向量库、MinIO 等依赖）运行，用户前端监听 5137 端口。提供 docker-compose 一键启动全部服务和分离式源码构建两种 Docker 部署方式；本地开发要求 Node.js 22.13.0+ 和 pnpm 11.0.9，npm 与 Yarn 不受支持。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Vue 3 + TypeScript + Ant Design Vue + Pinia + Vite 技术栈
- docker-compose-all.yaml 一键启动后端、管理面板、用户前端及依赖
- 本地开发仅支持 pnpm（11.0.9），npm/Yarn 安装不受支持

## 适用场景

- 作为 RuoYi-AI 平台的用户端，进行 AI 对话与知识库问答
- 通过 Docker Compose 一键部署整套 AI 服务
- 需要定制时从源码分离式构建部署

## 场景标签

`文档问答` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: ### Enterprise-Grade AI Assistant Platform - User Frontend
> L7: *The RuoYi-AI user frontend for AI conversations, agent interactions, and knowledge-base Q&A.*

## 星数曲线

```mermaid
xychart-beta
    title "ageerle/ruoyi-web 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 423 --> 426
    line [424, 425, 425]
```

2026-10-18 424 → 2026-10-29 425（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 low · 依据 README sha `7eb4dc7b1f30` · [字段定义](../../DATASET.md)*
