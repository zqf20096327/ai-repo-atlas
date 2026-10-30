# X-T-E-R/kiki

⭐ 31 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/X-T-E-R/kiki) · [官网](https://x-t-e-r.github.io/kiki/) · 个人维护 · 中文 README

**多模型 AI agent 工作台：桌面/TUI/Web 三端调度子代理完成任务**

面向需要 agent 代办任务的用户：给它一个文件夹与任务（梳理代码库、读 PDF/表格、改稿、提交变更），主 agent 拆分任务并派发子代理，每个子代理可绑定不同厂商模型（Kimi、Anthropic、OpenAI、Gemini、Vertex AI），同一会话内混合调度。桌面应用、终端 TUI 与浏览器 UI 连接同一本地守护进程，会话互通；支持微信/QQ 远程回复与审批、目标与记忆跨轮续作。文件留在本地，MIT 开源。PDF/Office 抽取需另装插件（依赖 Python 与 MarkItDown），Windows 首次启动前需安装 Git for Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一调度树中为不同子代理绑定不同厂商模型
- 桌面/TUI/Web 三界面连接同一本地守护进程
- 微信/QQ 配对远程回复、引导当前轮次与审批
- Markdown 文件定义 agent（前置元数据+系统提示词），保存即生效

## 适用场景

- 让 AI agent 在本地代码库中规划并提交变更
- 多模型分工处理文档堆（PDF/表格）并产出带出处的摘要
- 通过手机微信/QQ 审批并继续桌面上的 agent 任务

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L8: Hand Kiki a folder and a task: map an unfamiliar codebase, work through a stack of PDFs and spreadsheets, finish a d
> L14: - **Several models in one dispatch tree**: a strong model plans, cheaper models run routine work, and a review on a


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f47e483f83ad` · [字段定义](../../DATASET.md)*
