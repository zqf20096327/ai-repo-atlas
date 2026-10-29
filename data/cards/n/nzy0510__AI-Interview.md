# nzy0510/AI-Interview

⭐ 21 · Java · Apache-2.0 · 推送 2026-09-27 · [GitHub](https://github.com/nzy0510/AI-Interview) · [官网](https://interwise.net.cn) · 个人维护 · 中文 README

**面向技术面试训练的可自部署 AI 模拟面试平台**

InterWise 是自部署的模拟面试系统，提供文字/视频面试、简历画像、动态 RAG 追问、岗位/题库管理、历史报告与 AI Mentor 复盘。后端 Spring Boot 3 + LangChain4j + MySQL + Qdrant，前端 Vue 3；面试阶段由服务端规则状态机推进，结合 Qdrant 语义检索题库知识原子决定追问/补救/换题，再由用户自配的 OpenAI-compatible 模型流式生成下一问。用户需自备 API Key，项目不提供系统兜底；通过 Docker Compose 与 PowerShell 脚本部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则状态机 + 动态 RAG 决定追问/补救/换题路径
- 文字/视频面试、简历画像、AI Mentor 与知识覆盖率复盘闭环
- 公共与私有题库并存，受控文档入库与人工终审发布
- 内置离线检索评测工具链与请求级 RAG 日志

## 适用场景

- 求职前进行技术/HR 模拟面试并获取追问训练
- 基于自己的简历与岗位题库做定制化面试
- 面试后复盘评分、知识覆盖与风险点

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: InterWise 是一个面向技术面试训练的 AI 模拟面试平台。项目把规则驱动的面试流程、简历画像、文字面试、视频面试、数据库题库、动态 RAG 追问、面试复盘和 AI Mentor 打通到同一条学习闭环中，重点解决“只会单轮问答
> L11: - 动态面试 RAG：在规则计算出的技术 / HR 阶段检索岗位题库，把候选人真实回答、历史已用知识点和召回结果转成下一问的证据与提示。
> L35: |OpenAI-compatible Chat API|用户自配 DeepSeek / Kimi / GLM / Qwen / OrcaRouter / 自定义兼容模型|

## 星数曲线

```mermaid
xychart-beta
    title "nzy0510/AI-Interview 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f85891a71d58` · [字段定义](../../DATASET.md)*
