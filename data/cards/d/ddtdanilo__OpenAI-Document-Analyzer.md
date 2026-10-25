# ddtdanilo/OpenAI-Document-Analyzer

⭐ 40 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/ddtdanilo/OpenAI-Document-Analyzer) · 个人维护

**用 OpenAI Responses API 对本地文档做问答分析的 Python CLI/库**

面向需要对 TXT、Markdown、PDF 文档提问的使用者：本地提取 PDF 文本后调用 OpenAI Responses API（gpt-5.6 系列或兼容模型 ID）生成回答，支持设定推理力度、回答详略、输出 token 数与输入大小限制。提供 CLI 与可复用的 DocumentAnalyzer Python 类，可注入自定义 OpenAI 客户端。默认禁用响应存储、将文档内容标记为不可信数据、以类型化错误上报 API 失败；限制包括 20 MiB 文件上限与 20 万字符文本上限。需 OpenAI API key，API 调用可能产生费用，仅支持文本型 PDF（扫描件需先 OCR）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地提取 PDF 文本后再发送 OpenAI Responses API 分析
- gpt-5.6-sol/terra/luna 三档模型配置，--model 亦接受兼容模型 ID
- 安全默认：响应存储默认关闭、文档内容标记为不可信、类型化应用错误
- 可注入自定义 OpenAI 客户端，测试套件全程 mock 网络调用

## 适用场景

- 对合同、报告等文档按提示词提取决策、责任人与风险
- 在 Python 项目中集成可复用的文档问答分析类
- 通过 CLI 快速对本地文本文档提问

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L9: A privacy-conscious Python CLI and library for asking focused questions about
> L10: TXT, Markdown, and PDF documents with the
> L11: OpenAI Responses API.

## 星数曲线

```mermaid
xychart-beta
    title "ddtdanilo/OpenAI-Document-Analyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d43b9a563439` · [字段定义](../../DATASET.md)*
