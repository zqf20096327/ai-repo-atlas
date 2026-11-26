# YHD-yhd-coder/nl2tex

⭐ 14 · JavaScript · MIT · 推送 2026-11-24 · [GitHub](https://github.com/YHD-yhd-coder/nl2tex) · 个人维护 · 中文 README

**把中英文公式描述/截图转成可编译 LaTeX 的本地工具**

一个只做公式转写的本地 Web 工具：输入中文或英文描述（或粘贴截图），输出经 KaTeX 当场编译校验的 LaTeX，失败自动带错误重试；描述有歧义时返回低置信度、说明与最多 3 个候选解读，不计算不求值。支持 MathML、Word OMML 导出，提供 CLI 与 HTTP 接口。需 Node ≥ 20，模型调用自备 API Key（多家供应商预设），只监听 127.0.0.1。只做转写：不解方程、复杂排版需人工微调。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条结果过 KaTeX 编译校验，失败自动带错误重试
- 歧义显式化：confidence + note，最多 3 个候选解读
- 截图 OCR 识别与 LaTeX/$...$/MathML/OMML 多格式导出
- 六个学科专属规则（如化学强制 \ce{}）

## 适用场景

- 写作论文时用中文口语描述生成规范的 LaTeX 公式
- 把公式截图批量转成可编辑的 LaTeX/MathML/Word 公式
- 本地部署转写服务，通过 HTTP 接口集成到编辑器流程

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: 用一句中文（或英文）描述一个公式，得到**能直接编译**的 LaTeX。
> L35: 手写 LaTeX 的门槛不在语法，而在"想到那个符号叫什么"。你知道要写求和，但不确定是 `\sum_{k=1}^{n}` 还是 `\sum\limits_{k=1}^n`；你知道要写下标，但多字母下标忘了 `\mathrm{}`
> L45: - **多家供应商**：DeepSeek / Kimi / 智谱 / 通义千问 / SiliconFlow / OpenRouter，或任何 OpenAI 兼容网关


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `19745ccc1ef2` · [字段定义](../../DATASET.md)*
