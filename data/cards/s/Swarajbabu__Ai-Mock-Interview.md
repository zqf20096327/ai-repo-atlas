# Swarajbabu/Ai-Mock-Interview

⭐ 22 · JavaScript · 推送 2026-04-08 · [GitHub](https://github.com/Swarajbabu/Ai-Mock-Interview) · [官网](https://github.com/Swarajbabu/Ai-Mock-Interview) · 个人维护

**求职者用的 AI 模拟面试平台：语音视频面试加自动评分反馈**

面向求职候选人的全栈模拟面试平台：上传简历与目标职位描述后，通过 LLM 流水线生成岗位定制题库，在浏览器中以语音视频形式进行 AI 面试官实时对话（TTS 生成回应，语音识别采集回答），结束后 NLP 引擎按清晰度、相关性、深度、沟通、自信 5 个维度即时评分并自动发送反馈报告。运营流程由 3 个 n8n 工作流（排期、反馈发送、结果入库）自动化。前端 React+Vite，后端 Node.js+Express，数据库 Convex，需自备 LLM/NLP/TTS API key 与云存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 根据简历与 JD 自动生成岗位定制题库
- 语音视频实时 AI 面试官对话，TTS 回应延迟宣称低于 2 秒
- NLP 引擎按 5 个维度即时评分并自动发送反馈报告
- 3 个 n8n 工作流自动化排期、反馈发送与结果入库

## 适用场景

- 求职前按目标岗位做模拟面试练习
- 面试结束后即时获得多维度的回答反馈
- 管理员查看面试安排、成绩与反馈报告

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L17: **AI Mock Interview** is a full-stack, AI-driven platform that simulates realistic job interviews end-to-end. Candi
> L29: |🤖 **AI Avatar Responses**|TTS API delivers AI interviewer responses with sub-2s latency|
> L31: |📊 **Automated Scoring**|NLP engine scores responses across 5 dimensions instantly on completion|

## 星数曲线

```mermaid
xychart-beta
    title "Swarajbabu/Ai-Mock-Interview 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b8f4dc061da4` · [字段定义](../../DATASET.md)*
