# ctx-o1/lazyllama

⭐ 19 · Python · MIT · 推送 2026-05-31 · [GitHub](https://github.com/ctx-o1/lazyllama) · [官网](https://pypi.org/project/lazyllama/) · 个人维护

**发现并列出 HuggingFace/Ollama/LM Studio 本地模型的 CLI 工具**

Python 编写的本地模型管理小工具：扫描 HuggingFace、Ollama 与 LM Studio 三种来源的本地模型，输出概览列表；支持添加自定义扫描目录，--json 输出含模型元数据（名称、来源、大小、文件数）、文件详情（路径、格式、量化等）与缓存信息的结构化数据，--raw 输出纯文本。以 pip 安装的 CLI 形式提供，面向在本地运行多个模型来源的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描 HuggingFace / Ollama / LM Studio 三种来源的本地模型
- 支持自定义扫描目录（--add-dir）
- --json 输出结构化模型元数据与文件详情（含量化信息）

## 适用场景

- 盘点本机各来源已下载的模型与占用空间
- 以 JSON 形式导出模型清单供脚本处理
- 为自定义目录下的模型生成统一列表

## 场景标签

 · 领域:开发者工具/本地模型管理

## 证据(README 行号)

> L3: Local models management utility - discovers and lists models from HuggingFace, Ollama, and LM Studio.
> L10: pip install lazyllama

## 星数曲线

```mermaid
xychart-beta
    title "ctx-o1/lazyllama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `06379134217f` · [字段定义](../../DATASET.md)*
