# SnowLeopard-io/CogitoAgent

⭐ 33 · TypeScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/SnowLeopard-io/CogitoAgent) · [官网](https://snowleopard-io.github.io/CogitoAgent/) · 组织维护 · 中文 README

**本地优先的自主 AI 智能体，替用户持续思考并操作工作区**

基于 TypeScript/Electron 的桌面端自主 AI agent：接入任意 OpenAI 兼容 LLM API，以事件驱动思维循环持续在本地工作区反思与行动。内置 120+ 工具（文件、代码执行、Git、SQL、OCR、Office、图像生成、浏览器自动化、微信集成），支持子代理集群协作（派发/投票/流水线），提供 CLI/WebSocket 无头模式。安全机制含 isolated-vm 沙箱、危险操作确认门、工作区路径边界校验。仅对话上下文发送至 LLM API，文件不出本机。通过 git clone + npm 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 120+ 内置工具，覆盖文件/代码/Git/数据库/OCR/Office/图像生成等 23 类
- 事件驱动持续思维循环，无轮询间隔
- isolated-vm 进程级沙箱与危险操作确认门
- Agent 集群：子代理派发、并行执行、面板讨论与投票

## 适用场景

- 让 AI 持续整理本地文件并回答工作区相关提问
- 自动搜索网页、起草文档并写入工作区
- 通过子代理集群拆分并并行处理复杂任务
- 在服务器上以 CLI/WebSocket 模式常驻运行 agent

## 场景标签

`AI 助手` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L26: Cloud-based AI assistants send your files, code, and conversations to third-party servers. **CogitoAgent takes a di
> L30: - **Thinks continuously** — automatically reflects and acts on your workspace even while you're away

## 星数曲线

```mermaid
xychart-beta
    title "SnowLeopard-io/CogitoAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `66fcc0cfbccf` · [字段定义](../../DATASET.md)*
