# zhoujun94511/TestPilot-vue

⭐ 16 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/zhoujun94511/TestPilot-vue) · [官网](https://github.com/zhoujun94511/TestPilot-vue) · 个人维护 · 中文 README

**基于 LLM+RAG 的测试用例生成与管理 Web 平台**

Flask + Vue 3 的 Web 应用：读取 TXT/DOC/PDF/Markdown 等需求文档，自动提取测试要点与业务规则，调用大语言模型生成含负面与边界场景的测试用例，并通过 RAG 知识库（历史用例、测试规范）增强生成。内置自研幻觉检测（模式匹配、逻辑分析、置信度分级处理）、多策略检索（FTS5 关键词召回 + sqlite-vec 向量精排）与可视化配置中心。支持 OpenAI、Gemini、DeepSeek、Qwen、Ollama 及 OpenAI 兼容模型；Embedding 用 FastEmbed（ONNX/CPU），无需 GPU 与 PyTorch，向量库为 SQLite 单文件，需 pip 安装依赖并初始化数据库后以 python run.py 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 需求文档解析→测试用例自动生成（含负面/边界用例与优先级分配）
- RAG 知识库 + 两阶段混合检索（FTS5 召回 + sqlite-vec 精排），SQLite 单文件向量存储
- 多维度幻觉检测，按置信度分级自动警告/修正/重新生成/过滤
- 支持 OpenAI/Gemini/DeepSeek/Qwen/Ollama 及 OpenAI 兼容 API，配置中心可视化动态管理

## 适用场景

- 测试工程师从需求文档批量生成测试用例，替代手工编写
- 沉淀历史用例与测试规范为知识库，供后续需求检索复用
- 对 AI 生成内容做幻觉与质量检测，减少人工审核量

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L20: TestPilot 是一个的智能测试用例生成工具，基于大语言模型（LLM）技术，能够自动分析需求文档并生成高质量的测试用例。该工具集成了先进的幻觉检测系统，确保AI生成内容的准确性和可靠性，旨在提高软件测试效率，减少手工编写测试用
> L284: - **多模型支持**：支持OpenAI、Google Gemini、DeepSeek、Ollama等多种AI模型
> L298: - **智能生成**：基于需求描述自动生成测试用例

## 星数曲线

```mermaid
xychart-beta
    title "zhoujun94511/TestPilot-vue 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `90363c1d24d0` · [字段定义](../../DATASET.md)*
