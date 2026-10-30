# e-kotov/rdocdump

⭐ 19 · R · NOASSERTION · 推送 2026-05-31 · [GitHub](https://github.com/e-kotov/rdocdump) · [官网](http://www.ekotov.pro/rdocdump/) · 个人维护

**将 R 包源码、文档与 vignette 汇总为单文件的导出工具**

R 语言包，把指定 R 包的源代码、文档和 vignette 导出为一个纯文本文件或 character 向量。支持已安装的包、tar.gz 压缩包和包源码目录三种输入；若包未安装，自动从 CRAN 下载源码处理。输出面向注入大语言模型（LLM）或传递给其他工具（如 {ragnar}）构建 RAG 工作流。通过 CRAN、R Universe 和 GitHub 三种途径分发，处于 stable 生命周期阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持已安装包、tar.gz 归档与源码目录三种输入
- 未安装的包自动从 CRAN 下载源码处理
- 输出单文件或 character 向量，供 LLM 或 RAG 工具使用
- CRAN / R Universe / GitHub 三渠道安装

## 适用场景

- 我想把整个 R 包的文档与源码喂给 LLM 做问答
- 为 RAG 工作流准备 R 包的完整文本语料
- 批量提取包的 vignette 与帮助文档做分析

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L23: Dump source code, documentation and vignettes of an `R` package into a
> L27: single plain text file or a `character` vector, which is useful to
> L29: model (LLM) or pass it further to other tools, such as

## 星数曲线

```mermaid
xychart-beta
    title "e-kotov/rdocdump 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `657d45e48a6a` · [字段定义](../../DATASET.md)*
