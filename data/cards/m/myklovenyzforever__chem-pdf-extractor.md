# myklovenyzforever/chem-pdf-extractor

⭐ 18 · Python · MIT · 推送 2026-07-25 · [GitHub](https://github.com/myklovenyzforever/chem-pdf-extractor) · 个人维护 · 中文 README

**从化学化工文献 PDF 抽取实验数据为 Excel/CSV 的本地 LLM 工具**

面向化工、催化、材料、能源与环境领域研究者：将论文 PDF 转为 Markdown/文本，按可配置字段用 LLM 抽取实验条件与结果（温度、压力、转化率、产率等），一篇论文可产出多行记录并导出 Excel/CSV。支持本地 Ollama 模型与可选的 OpenAI 兼容云 API（需自备 key），提供本地 Web UI 与 CLI，三种 PDF 解析后端可切换。输出定位为需人工核验的初筛数据，附 source_evidence 等核验辅助列；Web UI 仅限 127.0.0.1 本地使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可配置 LLM 抽取字段，一篇论文多记录多行导出
- 本地 Ollama 或 OpenAI 兼容云 API 双通道
- 三种 PDF 解析后端（mineru/pymupdf4llm/pypdf_text）可选
- source_evidence/page_hint 等核验辅助列与坏行过滤、断点续跑

## 适用场景

- 文献综述时批量整理实验条件与结果数据
- 构建初筛数据集后再人工核验
- 本地模型处理未发表或保密 PDF 不外发

## 场景标签

`科研工具` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: Chem-PDF-Extractor is an open-source tool for extracting structured experimental data from chemical engineering, cat
> L11: The project provides an inspectable, local-first workflow for converting PDF papers to Markdown/text, defining conf
> L24: 4. Run extraction with local Ollama or an OpenAI-compatible cloud provider.

## 星数曲线

```mermaid
xychart-beta
    title "myklovenyzforever/chem-pdf-extractor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `306009cab770` · [字段定义](../../DATASET.md)*
