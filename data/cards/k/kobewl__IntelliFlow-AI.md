# kobewl/IntelliFlow-AI

⭐ 21 · Vue · MIT · 推送 2026-09-23 · [GitHub](https://github.com/kobewl/IntelliFlow-AI) · [官网](https://github.com/kobewl) · 个人维护 · 中文 README

**面向中小团队的全栈 AI 对话平台（Vue+Spring Boot）**

前后端分离的智能对话平台：后端 Spring Boot 3.5 + Java 17，前端 Vue 3 + TypeScript。已实现 SSE 流式对话、Markdown/代码高亮渲染、用户体系与 JWT 鉴权、对话历史、MinIO 文件上传，并通过 Provider 抽象（AIPlatformService 接口）集成 DeepSeek 与豆包，可经 OrcaRouter（OpenAI 兼容网关）接入更多模型。知识库 RAG、多模型智能路由、Agent 编排处于规划阶段。运行依赖 MySQL、Redis、RabbitMQ 等，需配置后端 application.yml 并分别启动前后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Provider 抽象接口统一接入 DeepSeek/豆包，新增模型只需实现接口
- SseEmitter + EventSource 实现流式打字机输出
- 自带用户体系、JWT、对话历史与 MinIO 文件上传
- 可选经 OrcaRouter（OpenAI 兼容）接入更多模型

## 适用场景

- 中小团队或学习场景搭建自有 AI 对话服务
- 在 DeepSeek/豆包等多模型间切换进行流式对话
- 作为 Spring Boot + Vue 全栈 AI 应用二次开发的基础

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L12:  一个面向学习与中小团队场景的全栈 AI 对话平台
> L17: - **流式对话** — SSE 流式输出,Markdown / 代码高亮渲染,体验接近 ChatGPT
> L37: |**智能对话**|✅|SSE 流式输出、Markdown 渲染、代码高亮|

## 星数曲线

```mermaid
xychart-beta
    title "kobewl/IntelliFlow-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `afe8455d8abe` · [字段定义](../../DATASET.md)*
