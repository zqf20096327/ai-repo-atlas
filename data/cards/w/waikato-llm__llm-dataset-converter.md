# waikato-llm/llm-dataset-converter

⭐ 22 · Python · MIT · 推送 2025-11-12 · [GitHub](https://github.com/waikato-llm/llm-dataset-converter) · [官网](https://waikato-llm.github.io/llm-dataset-converter-examples/) · 组织维护

**LLM 数据集格式转换与清洗的 Python 工具库**

Waikato LLM 团队维护的数据集转换工具：以插件化 reader/filter/writer 架构，在 classification、pairs、pretrain、translation 四类任务的 CSV/JSON Lines/Parquet/TSV/TXT/Alpaca/XTuner 等格式间转换，支持 bz2/gzip/xz/zstd 压缩。附带 llm-convert、llm-download、llm-append、llm-paste、llm-find、llm-file-encoding、llm-registry 等 CLI 工具，通过 seppl 库的 class lister 注册机制扩展插件，另有 faster-whisper 转录、OpenAI/Google 集成、PDF/Word/HTML 处理等附加库。经 PyPI 与 Docker 镜像分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类任务（classification/pairs/pretrain/translation）多种格式互转，插件化 reader/filter/writer 架构
- 支持 bzip2/gzip/xz/zstd 压缩与文件编码检测/覆盖
- 提供 llm-convert/llm-download/llm-append/llm-find 等 CLI 工具集
- 附加库覆盖 faster-whisper 音频转录、OpenAI/Google 集成、PDF/Word/HTML 处理

## 适用场景

- 把已有语料转换成目标训练框架要求的数据集格式
- 转换时对数据做过滤清洗
- 合并、拆分与批量定位数据文件以组织训练数据

## 场景标签

 · 领域:LLM 数据工程

## 证据(README 行号)

> L2: For converting large language model (LLM) datasets from one format into another.
> L40: |Domain|Format|Read|Write|Compression|

## 星数曲线

```mermaid
xychart-beta
    title "waikato-llm/llm-dataset-converter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1cb1cba7582b` · [字段定义](../../DATASET.md)*
