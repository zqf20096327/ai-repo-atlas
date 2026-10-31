# ASEpochs/epochflow

⭐ 15 · Python · 推送 2026-10-30 · [GitHub](https://github.com/ASEpochs/epochflow) · [官网](https://epochflow-web.onrender.com/) · 个人维护 · 中文 README

**面向客服场景的多 Agent 编排与模型实验平台**

EpochFlow（纪流）是 Vue 工作台 + FastAPI 后端的多 Agent 工程项目：将一次请求拆为意图识别、Agent 路由、Skills 注入、工具调用、知识检索、回复合成与运行评测的可观察链路。包含 4 类 Agent 角色、多协议模型网关（Anthropic/OpenAI 风格，接入 SiliconFlow 50 个模型标识）、轻量知识库（字符 n-gram 检索，云端版不引入付费数据库）与 LLM-as-Judge 评测。提供在线演示与本地运行方式；Render 免费版存在无持久磁盘、限流与重启清空数据等边界。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 意图识别→路由→工具→检索→合成的可观察执行链路
- 多协议模型网关接入 50 个模型标识、9 类实验入口
- LLM-as-Judge 评测与意图/对话质量用例
- 38 项后端测试 + 6 项 Playwright 端到端测试

## 适用场景

- 观察多 Agent 系统的路由决策与工具执行过程
- 在统一界面实验文字、视觉、向量、重排等多类模型
- 验证带知识检索与评测闭环的 Agent 工程方案

## 场景标签

`多智能体` `模型网关` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L29: EpochFlow 是一个面向客服与知识服务场景的 Agent 工程项目，将一次模型请求拆成可观察的工程链路：**意图识别 → Agent 路由 → Skills 注入 → 工具调用 → 知识检索 → 回复合成 → 运行评测**。
> L31: 项目关注的不只是“让大模型多回答一句话”，而是让 Agent 系统具备清晰的角色边界、可追踪的执行过程、可替换的模型能力和可重复的质量验证。系统包含 Vue 工作台、FastAPI 后端、多 Agent 编排器、轻量知识库、模型网

## 星数曲线

```mermaid
xychart-beta
    title "ASEpochs/epochflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3ca62210e824` · [字段定义](../../DATASET.md)*
