# chuanqisun/iter

⭐ 14 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/chuanqisun/iter) · [官网](https://chuanqisun.github.io/iter/) · 个人维护

**面向提示词快速迭代的 Gen AI 聊天前端**

极简风格的生成式 AI 聊天模型前端，定位为提示词工程师的试验场：凭据存于浏览器、请求直连 API 无中间层；支持在对话中途热切换 API 端点与模型而不丢进度。功能包括 Markdown 渲染与代码高亮、SVG/HTML/Mermaid/TS/React 的 Artifacts 实时预览、TypeScript 解释器（可访问 NPM 注册表与虚拟文件系统）、视觉/语音/PDF 输入，以及通过 run/edit/search/fetch 代码块改变 LLM 行为的指令机制。支持 OpenAI、Anthropic、Google、xAI、Cerebras、Inception、OpenRouter 等多家模型提供商。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 凭据存浏览器、请求直连 API 无中间层、无追踪
- API 端点与模型热切换且不丢失对话进度
- Artifacts 实时编辑预览 SVG/HTML/Mermaid/TypeScript/React
- run/edit/search/fetch 指令代码块改变 LLM 行为并启用代码执行与联网

## 适用场景

- 快速对比不同提示词和模型的效果
- 让 LLM 生成代码并直接在应用内运行预览
- 通过截图或 PDF 输入做 UI 复刻等任务
- 在一个界面里切换多家 API 提供商调试提示词

## 场景标签

`提示工程` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L3: A minimalist frontend for Gen AI Chat models, optimized for rapid prompt iteration.
> L25: ## Supported model providers

## 星数曲线

```mermaid
xychart-beta
    title "chuanqisun/iter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b925fc836326` · [字段定义](../../DATASET.md)*
