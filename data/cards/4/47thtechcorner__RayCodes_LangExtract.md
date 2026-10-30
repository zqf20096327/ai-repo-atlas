# 47thtechcorner/RayCodes_LangExtract

⭐ 17 · Python · 推送 2026-08-11 · [GitHub](https://github.com/47thtechcorner/RayCodes_LangExtract) · [官网](https://youtu.be/edwCp-cSfOc) · 个人维护

**本地 Ollama 模型驱动的文档结构化信息抽取工具，带字符级溯源**

基于 Google LangExtract 库构建的抽取项目：将非结构化文本（财报、病历、合同等）转为 schema 约束的结构化 JSON，并将每个抽取点映射到原文的精确字符偏移，输出可核验的来源片段。模型后端可在本地 Ollama、Google Gemini、OpenAI 之间配置，默认示例用本地 Ollama（如 qwen3:4b）实现零 API 成本运行。以 Python 脚本项目形式提供，需先创建输入文本文件并在 main.py 中配置 provider 后运行；未提供打包发行或 Docker 方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- schema 约束的多轮字符偏移映射，输出带来源字符区间的结构化 JSON
- 支持本地 Ollama 后端，零 API 成本运行
- 可切换 Google Gemini 云端后端
- 给出临床、金融、法律、保险、客服五类用例

## 适用场景

- 从财报或 SEC 文件抽取财务数据并核验原文出处
- 解析临床病历生成带审计轨迹的结构化诊断与用药数据
- 将合同条款（终止条件、责任上限）抽取为带字符偏移的 JSON

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L8: Google LangExtract is an open-source Python library that transforms unstructured text documents into verified struct
> L37: LangExtract supports **Ollama (local)**, **Google Gemini**, and **OpenAI**. Configure your preferred provider in `m

## 星数曲线

```mermaid
xychart-beta
    title "47thtechcorner/RayCodes_LangExtract 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `71c7e268a899` · [字段定义](../../DATASET.md)*
