# earthwalker17/agent-os

⭐ 26 · Python · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/earthwalker17/agent-os) · 个人维护

**本地优先的 AI 项目操作系统：把编码模型变成可靠软件代理**

面向单人开发者的 local-first 项目驾驶舱：通过单一 Web 聊天界面运行多个长期软件项目。以 FastAPI + React + SQLite + 文件系统本地运行，无云端队列。核心机制：Main Agent（规划/记忆/编排）与沙箱化 Coding Agent（六工具受限执行）双代理分离；六家模型提供商可选（Claude、GPT、Gemini、DeepSeek、Kimi、智谱 GLM）；构建→验证→交付→部署闭环，真实构建通过才算完成；外部与破坏性操作均需人工审批门。含类型化恢复矩阵、Playwright 浏览器验证与 Git/GitHub、Vercel/Supabase/Stripe 连接器。明确声明不做通用助手或重量级代理平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Main Agent/Coding Agent 双代理分离，沙箱单一执行边界，仅六个受限工具
- 六家模型提供商注册表（Claude/GPT/Gemini/DeepSeek/Kimi/智谱 GLM）
- 构建→验证→交付→部署闭环：真实构建通过才标记完成，Playwright 浏览器验证与视觉模型审查
- 类型化恢复矩阵与预授权限额（≤2）的自愈修复
- 外部/破坏性操作（推送、部署、支付）全部需显式人工审批

## 适用场景

- 独立开发者用聊天界面长期托管并推进多个软件项目
- 让编码模型在沙箱内执行任务并经真实构建与浏览器验证后才交付
- 通过 Git/Vercel/Supabase/Stripe 审批合同将项目交付到生产环境

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L36: **Agent OS is a local-first cockpit for running multiple long-term software projects through a single web chat surf
> L43: - **A capability-aware provider registry** — six model providers (**Claude, GPT, Gemini, DeepSeek, Kimi, Zhipu GLM*

## 星数曲线

```mermaid
xychart-beta
    title "earthwalker17/agent-os 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `962c3c0b4481` · [字段定义](../../DATASET.md)*
