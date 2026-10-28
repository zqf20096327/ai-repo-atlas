# TencentCloudBase/cloudbase-agent-ui

⭐ 98 · JavaScript · MIT · 推送 2026-01-29 · [GitHub](https://github.com/TencentCloudBase/cloudbase-agent-ui) · [官网](https://docs.cloudbase.net/ai/quickstart) · 组织维护 · 中文 README

**微信小程序 AI 对话 UI 组件：开箱即用接入大模型与 Agent**

腾讯云开发团队推出的微信小程序 AI 对话 UI 组件，支持 Agent 模式与大模型直连两种 chatMode。大模型直连支持 DeepSeek（deepseek-r1/deepseek-v3）与混元（hunyuan-lite），Agent 模式对接云开发平台智能体服务，并支持前端/服务端自定义工具（服务端走 LangChain 模板）。依赖微信云开发环境，获取方式为克隆仓库提取 components/agent-ui 目录或下载 Release 包。使用限制：单文件上传≤10M、图片≤30M 等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent 模式与大模型直连（DeepSeek/混元）双模式切换
- 流式输出、多轮会话等能力开箱即用
- 支持前端与服务端自定义工具（JSON Schema 参数、LangChain 适配）

## 适用场景

- 在小程序里快速加一个 AI 对话界面
- 通过配置接入 DeepSeek 或混元大模型
- 为云开发平台的智能体挂载自定义前端/后端工具

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L8: cloudbase-agent-ui 是由腾讯云开发团队推出的 AI 智能对话 UI 组件，配置简单开箱即用，助力微信小程序开发者快速集成大模型能力，打造企业级LLM应用。
> L14: - **双模式支持** `Agent模式` 与 `大模型直连` 自由选择对话策略
> L16: - **多模型支持** 深度兼容 DeepSeek、Hunyuan 等主流大模型，支持自定义模型接入

## 星数曲线

```mermaid
xychart-beta
    title "TencentCloudBase/cloudbase-agent-ui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 96 --> 99
    line [97, 98, 98]
```

2026-10-18 97 → 2026-10-28 98（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ff7464a6a310` · [字段定义](../../DATASET.md)*
