# pdsuwwz/chatgpt-vue3-light-mvp

⭐ 582 · Vue · MIT · 推送 2026-07-31 · [GitHub](https://github.com/pdsuwwz/chatgpt-vue3-light-mvp) · [官网](https://botkit.likemashang.com) · 个人维护 · 中文 README

**基于 Vue3 的 Chat Bot 单轮对话 Web 端 MVP 原型模板**

面向二次开发的纯前端 AI 对话原型模板：基于 Vue 3、Vite 8、TypeScript、Pinia、Naive UI、UnoCSS 构建，采用单轮问答模式（每次提问独立响应，不保留上下文），支持 SSE 流式打字机输出、Markdown/代码高亮/KaTeX 公式/Mermaid 图表渲染。通过模型映射表适配 DeepSeek V3/R1、星火、SiliconFlow、Moonshot、Ollama 等 API，提供无需真实 API 的本地模拟开发模式，并附可将工程经验复用到其他项目的 Agent Skill（架构蓝图）。限制：仅单轮对话，多轮暂无计划；纯前端架构，生产部署需自行处理跨域。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型映射机制统一适配 DeepSeek/星火/SiliconFlow/Moonshot/Ollama 的响应格式
- SSE 流式打字机输出，网络读取与 UI 渲染速度解耦
- Markdown 代码高亮 + KaTeX 数学公式 + Mermaid 图表渲染管线，兼容 <think> 推理标签
- 本地模拟开发模式，无需真实 API 即可开发

## 适用场景

- 快速搭建可二次开发的 Chat 类 LLM 产品原型
- 参考 SSE 流式渲染与多模型适配实现
- 在本地 Ollama 或国内大模型 API 上验证对话界面

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L13: 💭 一个可二次开发 Chat Bot 对话 Web 端原型模板, 基于 Vue 3、Vite 8、TypeScript、Naive UI、Pinia、UnoCSS 等主流技术构建, 🧤简单集成大模型 API, 采用单轮 AI 问答
> L36: * 🌍 **大语言模型 API**：兼容 Deepseek V3/R1, Spark 星火认知大模型、Kimi Moonshot 月之暗面大模型、SiliconFlow、Ollama 等，允许自由扩展
> L274: 由于不同大模型的 API 响应数据结构存在差异，本项目通过**统一的模型映射机制**和**响应转换函数**实现了多模型的无缝集成。核心逻辑封装在 详见代码 中，支持灵活扩展和定制

## 星数曲线

```mermaid
xychart-beta
    title "pdsuwwz/chatgpt-vue3-light-mvp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 581 --> 583
    line [582, 582]
```

2026-10-18 582 → 2026-10-22 582（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3457823906ad` · [字段定义](../../DATASET.md)*
