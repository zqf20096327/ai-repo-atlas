# BovmantH/cn-company-research-agent

⭐ 16 · Python · Apache-2.0 · 推送 2026-08-12 · [GitHub](https://github.com/BovmantH/cn-company-research-agent) · [官网](https://cn-company-research-agent.onrender.com/) · 个人维护 · 中文 README

**多 Agent 中文公司调研 Web 服务：输入公司名产出调研报告**

基于 FastAPI 后端与 React 前端的公司调研 Web 服务，用 LangGraph 编排 10 节点流水线（Grounding、4 个并行 Researcher、过滤、摘要、编辑），从官网、新闻、财报等公开来源采集并合成中文调研报告，面向投资、BD 与竞品分析场景。三段式 LLM 架构按角色绑定模型，服务端支持 DeepSeek/Kimi/Qwen/GLM/MiniMax/MiMo 原厂直连及 OpenRouter/OpenAI 兼容入口，也支持任务级用户自带 Key（不持久化）。工商司法专业数据为默认关闭的预览能力。部署要求 Python 3.11+、Node.js 18+，提供 Docker 与源码两种运行方式。

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

- LangGraph 编排 10 节点调研流水线，含 4 个并行 Researcher 与相关性过滤（阈值 0.4）
- 六家国产模型原厂直连 + OpenCode Zen 免费优先 + OpenRouter/OpenAI 兼容入口
- 任务级用户 Key 仅驻留内存，不持久化、不写应用日志
- 可重放 SSE 进度流与 PDF 生成下载

## 适用场景

- 输入公司名自动生成投资、BD 前置调研报告
- 在中国大陆网络环境下用国产模型原厂直连做公司调研
- 自部署调研服务并让成员自带各厂商 API Key 使用

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L21: 一个**多 Agent 架构**的中文公司调研工具：输入公司名称，自动产出面向投资、BD 和竞品分析场景的调研报告。项目基于 LangGraph 编排多个 AI 节点，按流水线采集、过滤并合成公开信息。
> L9: > - 🇨🇳 **国产原厂直连** —— 服务端支持 DeepSeek、Kimi、Qwen、GLM、MiniMax、MiMo，无需经过聚合平台

## 星数曲线

```mermaid
xychart-beta
    title "BovmantH/cn-company-research-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a190df0d3677` · [字段定义](../../DATASET.md)*
