# Nikit117/kynex-harness

⭐ 4 · Python · NOASSERTION · 推送 2026-11-11 · [GitHub](https://github.com/Nikit117/kynex-harness) · [官网](https://www.extractbench.ai/#leaderboard) · 个人维护

**把 PDF、扫描件与表格转成符合 schema 的 JSON 的本地 agent**

KYNEX 是一个 agentic 文档抽取工具：对文档分页后让模型调用页面文本、表格、版面分析、渲染页等工具，返回可通过请求 schema 校验的 JSON。运行于任意 OpenAI 兼容端点，支持 Azure OpenAI 与本地 vLLM/Ollama/LM Studio 服务器，提供 TUI 与脚本入口，可选接入 Azure Document Intelligence 做表格行读取与 OCR 兜底。内置六条可开关的后处理规则（分页枚举、非记录剪枝、OCR 兜底等），在 ExtractBench 排行榜有三条经 LlamaIndex 验证的条目，README 附证据包与复现脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型可调用工具读取页面文本、表格、版面与渲染页
- 输出通过请求 schema 校验的 JSON
- 六条规则均带环境变量开关，可单独测量
- 支持任意 OpenAI 兼容端点与交互式 TUI 配置

## 适用场景

- 把发票、报表等文档批量抽取为结构化 JSON
- 处理无文本层的扫描页并输出结构化数据
- 在本地 vLLM/Ollama 端点上运行文档抽取流程

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L31: KYNEX is an **agentic document-extraction harness**. It stages a document, lets
> L33: pages — and returns JSON that validates against the requested schema. It is
> L155: kynex run invoice.pdf --prompt "Extract the vendor, invoice date and every line item as JSON"

## 星数曲线

```mermaid
xychart-beta
    title "Nikit117/kynex-harness 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-18", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-02 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0666b65317cb` · [字段定义](../../DATASET.md)*
