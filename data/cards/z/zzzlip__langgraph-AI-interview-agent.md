# zzzlip/langgraph-AI-interview-agent

⭐ 58 · Java · 推送 2026-07-10 · [GitHub](https://github.com/zzzlip/langgraph-AI-interview-agent) · 个人维护 · 中文 README

**面向求职者的 AI 面试辅助平台：简历评估/优化与模拟面试**

Java 平台层（Spring Boot 3 模块化单体）+ Python AI Worker（LangGraph、DashScope SDK）+ 静态前端 + Docker Compose 基础设施组成的面试辅助系统，支持多用户认证、异步任务与 SSE 进度。功能包括五维度简历评估与雷达图报告、简历优化、通过 Codeforces 端口的算法测试、多类型问题的模拟面试与追问，以及调用 ASR/多模态 provider 的音视频分析。产物统一存储到 MinIO。默认启用 deepseek/dashscope provider，历史 LangGraph 原型代码不作为 V1 发布内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五维度简历评估（未来潜力/教育/技术栈匹配/经历匹配/结构）输出报告与雷达图
- 模拟面试支持追问决策、任务内记忆压缩与最终报告生成
- 通过 Codeforces 正式端口生成算法训练任务并异步确认提交状态
- Java 平台 + Python Worker + RabbitMQ/MinIO/Redis 的 Docker Compose 编排

## 适用场景

- 上传简历并对照目标岗位获得评分与优化建议
- 进行带追问与多模态信号的模拟面试练习
- 按岗位方向生成算法题并跟踪练习进度

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: 面向求职准备的 AI 面试辅助平台。V1 采用 Java 平台层 + Python AI Worker + 静态前端 + Docker Compose 基础设施的组合，支持多用户认证、文件管理、异步任务、SSE 进度、简历评估、简历
> L29: - 根据简历和岗位信息生成技术基础、项目经历、业务理解、软技能等不同类型的问题。
> L91: |Python Worker|Python 3.10、LangGraph、httpx、DashScope SDK|复用 AI 工作流生态，执行真实模型、ASR、多模态和外部查询|

## 星数曲线

```mermaid
xychart-beta
    title "zzzlip/langgraph-AI-interview-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-26 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `8f308340f98c` · [字段定义](../../DATASET.md)*
