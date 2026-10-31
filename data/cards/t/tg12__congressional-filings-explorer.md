# tg12/congressional-filings-explorer

⭐ 16 · Python · NOASSERTION · 推送 2026-05-16 · [GitHub](https://github.com/tg12/congressional-filings-explorer) · 个人维护

**用 OpenAI Vision 分析美国议员财务披露 PDF 的 OCR 工具**

面向需要追踪美国国会众议员财务披露信息的用户（OSINT/研究者）：自动下载众议院披露服务器的 XML 元数据与 PDF 文件（20 线程并行），将 PDF 转为图片后调用 OpenAI Vision API（默认 gpt-4.1-mini）做模式识别，提取股票交易、资产持有等结构化信息并以表格和摘要展示。需配置 OPENAI_API_KEY，每份文件估计成本约 $0.01-0.05。提供仅处理数据不调 API 的测试模式。Python 3.8+ 运行，依赖 poppler 系统包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 众议院披露 XML 元数据自动刷新与 PDF 并行抓取（20 线程）
- PDF 转图片后经 OpenAI Vision 做模式识别与结构化提取
- --test 模式仅做数据处理、不调用 API
- API key 通过环境变量配置，无硬编码凭据

## 适用场景

- 批量分析近期议员股票交易与资产披露文件
- OSINT / 政治资金透明度调查
- 定期跟踪众议院财务披露更新并生成汇总

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L6: An intelligent pattern-matching tool for analyzing publicly available Congressional financial disclosure documents u
> L143: 7. **AI Analysis**: Sends images to OpenAI Vision API for pattern recognition

## 星数曲线

```mermaid
xychart-beta
    title "tg12/congressional-filings-explorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2ebc88effe79` · [字段定义](../../DATASET.md)*
