# azadhmhd/interview-command-center

⭐ 3 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/azadhmhd/interview-command-center) · 个人维护

**自托管求职跟踪与 AI 辅助面试准备工具**

面向求职者的自托管应用：管理投递（表格/看板/时间线视图）、按公司记录面试问题与答案、维护带间隔重复复习队列的知识库，并基于职位描述与个人弱点生成冲刺课程、简历定制、编码练习与 AI 评分。AI 部分可选：接入任意 OpenAI 兼容端点，或复用 Claude Code / Cursor 订阅通过 agent 任务包执行，无 AI 时跟踪与复习功能仍可离线使用。技术栈为 Next.js + NestJS + PostgreSQL，提供 Docker Compose 一键启动与本地开发模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面试日志记录真实被问问题，SM-2 间隔重复复习队列
- 基于 JD 与记录弱点的定制冲刺课程与模拟面试
- Auto Apply 通过 SerpApi/Jooble 找职并经本地浏览器 runner 或 Claude in Chrome 提交
- AI 可选：OpenAI 兼容端点或 Claude Code/Cursor 订阅任务包

## 适用场景

- 集中跟踪多公司投递进度与后续跟进提醒
- 把每轮面试被问的问题沉淀为下一次备考材料
- 面试前按 JD 自动生成时间盒冲刺计划与闪卡
- 用本地 Ollama 端点离线做简历定制与练习评分

## 场景标签

 · 领域:求职/个人效率

## 证据(README 行号)

> L3: **Self-hosted job search tracker, interview journal and AI-assisted interview preparation.**
> L59: - **Bring your own AI:** one OpenAI-compatible client (Ollama, vLLM, LM Studio, hosted providers) **or** your
> L161: ### Option 1: an OpenAI-compatible LLM (Ollama, vLLM, LM Studio, hosted)

## 星数曲线

```mermaid
xychart-beta
    title "azadhmhd/interview-command-center 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `860666408234` · [字段定义](../../DATASET.md)*
